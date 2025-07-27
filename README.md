#  📧 Gmail Assistant – Intelligent Email Labeling Assistant

## Problem Statement

Managing a large volume of emails in Gmail can quickly become overwhelming. Promotional messages, notifications, offers, spam, and invoices all mix together, making it difficult to respond efficiently. Manually sorting and labeling emails is tedious, error-prone, and time-consuming. Many users underutilize Gmail’s powerful labeling system simply due to the lack of an effective, intelligent tool for automatic email categorization based on actual content.

## Application

**Gmail Assistant** is a Python-based tool designed to solve this problem. It automatically analyzes your recent (or selected) Gmail messages and assigns appropriate labels from a pre-defined category set. The tool leverages:

- 🤖 **Perplexity API (AI)** for deep content analysis and category assignment
- 📬 **Gmail API** for fetching emails, applying labels, and dynamically creating new labels in your Gmail account if needed

### ⭐ Key Features

- **Automatic email classification** into predefined categories (e.g., Invoice, Spam, Offers)
- **Interactive mode** allowing you to confirm or correct AI suggestions, storing feedback for future improvement
- **Automatic mode** for fast batch processing without manual intervention
- **Built-in statistics** with bar charts showing category distributions during each session
- **Feedback loop system** enabling the assistant to learn from user corrections (excellent portfolio showcase)
- Clean, modular design facilitating future extensions and integration with other services

## 🗂️ Project Structure

gmail-assistant/
│
├── main.py # Main script running the email labeling workflow
├── gmail_api.py # Gmail API authentication and email operations
├── perplexity_api.py # Functions to interact with Perplexity AI API
├── label_mapper.py # Mapping AI category names to Gmail label IDs (creates new labels if needed)
├── plot_statistics.py # Script to plot category assignment statistics from feedback data
├── requirements.txt # Python dependencies list
├── README.md # Project description and instructions (this file)
├── .gitignore # List of ignored files (API keys, tokens, caches)


## ⚙️ Setup Instructions

1. **Google Cloud Console Setup:**
   - Create a project in [Google Cloud Console](https://console.cloud.google.com/).
   - Enable the Gmail API.
   - Create OAuth 2.0 credentials for a Desktop Application.
   - Download the `credentials.json` file and place it in the project root directory.
   
2. **Perplexity API Key:**
   - Obtain your Perplexity API key from your Perplexity Pro account.
   - Store the key securely by creating a `.env` file or export it as an environment variable:
     ```
     PERPLEXITY_API_KEY=your_api_key_here
     ```

3. **Install dependencies:**
  ```
  pip install -r requirements.txt
  ```
4. **Run the assistant:**

   - You will be prompted to select **Automatic** or **Interactive** mode.
- Authentication with Gmail will happen on the first run via OAuth browser window.

5. **View statistics:**
After processing emails, run:
```
python plot_statistics.py
```

This displays a bar chart of how many emails were assigned to each category during the session.

## Usage Modes

- **Automatic mode**: The assistant tags emails without asking for user input — fast and hands-off.
- **Interactive mode**: After AI suggests a label, you can approve or change it, enabling a feedback loop to improve labeling accuracy over time.

## 🔐 Security & Good Practices

- Your `credentials.json`, OAuth `token.json`, `feedback.csv`, and `.env` files **must never** be publicly shared or pushed to GitHub.
- Use `.gitignore` to exclude these files from your repository.
- Store all secrets securely and consider using environment variables for API keys.
- This approach keeps your account safe and your project professional.

## Contact & Contributions

For questions, improvements, or collaboration, feel free to open an issue or pull request on GitHub, or reach out via email.

---



