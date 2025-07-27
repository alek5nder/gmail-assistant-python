import os
import csv
from gmail_api import gmail_authenticate, get_latest_messages, get_message_content, add_label
from perplexity_api import analyze_email_with_perplexity
from label_mapper import map_label_to_id

def main():
    PX_API_KEY = os.getenv("PERPLEXITY_API_KEY")
    if not PX_API_KEY:
        print("Ustaw zmienną środowiskową PERPLEXITY_API_KEY")
        return

    print("Wybierz tryb pracy:")
    print("1 - Automatyczny (AI kategoryzuje, bez pytania użytkownika)")
    print("2 - Interaktywny (po każdym mailu pytaj o zatwierdzenie)")
    mode = ""
    while mode not in ("1", "2"):
        mode = input("Twój wybór (1/2): ").strip()

    interactive = (mode == "2")

    service = gmail_authenticate()
    msg_ids = get_latest_messages(service)

    for msg_id in msg_ids:
        print(f"Przetwarzanie maila {msg_id}...")
        text = get_message_content(service, msg_id)
        if not text.strip():
            print("Brak zawartości tekstowej maila, pomijam.")
            continue

        label_name = analyze_email_with_perplexity(PX_API_KEY, text)
        print(f"AI zasugerowało etykietę: {label_name}")

        if interactive:
            user_choice = input(f"Wpisz nową kategorię (ENTER = akceptuj '{label_name}'): ").strip()
            final_label = user_choice if user_choice else label_name

            # Zapisujemy feedback tylko w trybie interaktywnym
            with open('feedback.csv', 'a', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow([msg_id, label_name, final_label, text[:200]])
        else:
            final_label = label_name

        label_id = map_label_to_id(service, final_label)
        add_label(service, msg_id, label_id)
        print(f"Dodano etykietę '{final_label}' do maila {msg_id}.\n")

if __name__ == '__main__':
    main()
