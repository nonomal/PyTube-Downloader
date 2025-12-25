<div id="adding-a-new-theme">

# 🎨 Theme Contribution Guide

Enhance the visual experience of **PyTube Downloader** by creating or improving color themes.
Your design contributions help make the app more stylish, accessible, and enjoyable for everyone!

---

## 🌈 Add a New Theme

To add a new color theme to the application:

1. **Update `themes.json`**

   * Open the [`themes.json`](/data/themes.json) file in the [`data`](/data) directory.
   * Add a new entry with the display name as the key and the theme file name (without `.json`) as the value.

     Example:

     ```json
     {
       "Dark Default": "dark_default",
       "Light Default": "light_default",
       "Cyberpunk Black": "cyberpunk_black",
       "Gold Black": "gold_black"  // New entry
     }
     ```

2. **Create the Theme File**

   * Navigate to the [`data/themes`](/data/themes) directory.
   * Create a new JSON file using the same name you added in `themes.json`.

     Example:

     ```
     data/themes/gold_black.json
     ```

3. **Add Theme Colors**

   * Open your new theme file and define the color palette using HEX color codes.
   * You can copy and modify an existing theme for reference.

     Example (`gold_black.json`):

     ```json
     {
       "background": "#202020",
       "background_warning": "#E04848",
       "background_warning_hover": "#C54040",
       "border": "#3C3C3C",
       "foreground": "#F2F2F2",
       "primary": "#333333",
       "primary_hover": "#3D3D3D",
       "secondary": "#4A4A4A",
       "secondary_hover": "#555555",
       "text_muted": "#9B9B9B",
       "text_normal": "#F2F2F2",
       "text_warning": "#FF6B6B"
     }
     ```

4. **Test Your Theme**

   * Launch **PyTube Downloader**.
   * Open **Appearance Settings** and select your newly added theme.
   * Verify that all UI elements are visible and that colors are well balanced across components.

5. **Submit a Pull Request**

   * Once verified, commit your theme and create a PR titled:

     ```
     feat(theme): added [Theme Name] theme
     ```

</div>

---

<div id="improve-current-themes">

## 🧹 Improve Existing Themes

If you want to fix or enhance existing themes:

1. **Locate the Theme File**

   * Go to the [`data/themes`](/data/themes) directory.
   * Open the corresponding `.json` theme file you wish to modify.

2. **Edit and Adjust Colors**

   * Update the color values as needed.
   * Ensure consistent readability and contrast between UI elements.

3. **Test the Theme**

   * Verify that all text and interface components remain clear under all interface states — normal, hover, and warning.
   * Make small adjustments to improve color harmony if needed.

4. **Submit a Pull Request**

   * Once confirmed, commit your updates and create a PR titled:

     ```
     fix(theme): improved [Theme Name] theme colors
     ```

</div>

---

## 💬 Final Words

Thank you for contributing to **PyTube Downloader**!
Your creative touch helps make the app’s design more elegant and personalized for users around the world. 🌈

> 🎨 Keep experimenting — small color tweaks can make a big visual impact!
