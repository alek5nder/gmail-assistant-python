import csv
from collections import Counter
import matplotlib.pyplot as plt

FEEDBACK_FILE = 'feedback.csv'

def load_feedback(filepath):
    categories = []
    try:
        with open(filepath, newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                #struktura wiersza: [msg_id, label_name_ai, label_name_final, mail_sample]
                if len(row) >= 3:
                    final_label = row[2].strip()
                    if final_label:
                        categories.append(final_label)
    except FileNotFoundError:
        print(f"Plik '{filepath}' nie znaleziony. Upewnij się, że feedback.csv istnieje.")
    return categories

def plot_category_counts(categories):
    counts = Counter(categories)
    if not counts:
        print("Brak danych do wyświetlenia.")
        return

    labels = list(counts.keys())
    values = list(counts.values())

    plt.figure(figsize=(10,6))
    bars = plt.bar(labels, values, color='skyblue')
    plt.xlabel('Kategorie')
    plt.ylabel('Liczba maili')
    plt.title('Statystyki przypisania kategorii maili przez asystenta')
    plt.xticks(rotation=45, ha='right')

    # Pokazujemy liczby nad słupkami
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, height + 0.1, str(height), ha='center', va='bottom')

    plt.tight_layout()
    plt.show()

def main():
    categories = load_feedback(FEEDBACK_FILE)
    plot_category_counts(categories)

if __name__ == '__main__':
    main()
