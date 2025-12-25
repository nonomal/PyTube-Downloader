<div id="improve-current-language-issues">

# 🌍 Language Contribution Guide

Improve and expand the multilingual experience of **PyTube Downloader** by fixing translations or adding new languages.
Your contributions make the app more accessible and user-friendly for everyone!

---

## 🧹 Improve Existing Translations

To correct or enhance current language files:

1. **Locate the Language File**

   * Go to the [`data`](/data) directory.
   * Open [`languages.json`](/data/languages.json) to find the relevant language key and its file path in [`data/languages/`](/data/languages).

2. **Edit the Translation File**

   * Open the corresponding JSON file (e.g., [`en.json`](/data/languages/en.json), `fr.json`).
   * Update the text with your improved translation.

3. **Test the Changes**

   * Launch the application and verify that the updated text displays correctly.
   * Ensure the translated text fits neatly within UI elements.

     > 💡 If it’s too long, use shorter words or line breaks for readability.

4. **Submit a Pull Request**

   * Once verified, commit your changes and create a PR titled:

     ```
     fix(language): improved [Language] translations
     ```
</div>

---

<div id="adding-a-new-language">

## 🌐 Add a New Language

To contribute a brand-new language:

1. **Update `languages.json`**

   * Edit the [`languages.json`](/data/languages.json) file located in the [`data`](/data) directory.
   * Add your language name and a short code to the JSON object.

     Example:

     ```json
     {
       "English": "en",
       "中文": "zh",
       "Español": "es"
     }
     ```

2. **Create the Language File**

   * In the [`data/languages`](/data/languages) directory, create a new file using your language code (e.g., `es.json`).
   * Add translations for all keys based on existing files.

     Example (`es.json`):

     ```json
     {
       "video": "Video",
       "playlist": "Lista",
       "add +": "Añadir +",
       "added": "Añadido"
     }
     ```

3. **Test the Language**

   * Run the application and select your new language.
   * Check spacing and readability in all UI components.

4. **Submit a Pull Request**

   * Once verified, commit your new file and submit a PR titled:

     ```
     feat(language): added [Language] translations
     ```

</div>

---

## 💬 Final Words

Thank you for improving our global user experience!
Your language contributions help users around the world enjoy a smoother and more inclusive application.

> ❤️ Excellent work — your effort truly makes a difference!
