import requests

def analyze_email_with_perplexity(api_key, email_text):
    url = "https://api.perplexity.ai/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    email_categories = {"Faktura", "Potwierdzenie zamówienia", "Podróże", "Powiadomienia", "Prywatne", "Inne"}
    prompt = (f"Przeanalizuj treść poniższego maila i wybierz jedną z kategorii  {email_categories}. Bez uzasadnienia, tylko"
              f"jedna kategoria. Treść: {email_text}")

    data = {
        "model": "sonar",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"].strip()
