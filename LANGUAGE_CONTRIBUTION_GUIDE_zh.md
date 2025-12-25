<div id="improve-current-language-issues">

# 🌍 语言贡献指南

通过修复翻译或添加新语言来改进和扩展 **PyTube Downloader** 的多语言体验。
你的贡献将让应用程序更加易用、友好，让更多用户受益！

---

## 🧹 改进现有翻译

若要修正或优化当前语言文件：

1. **找到语言文件**

   * 打开 [`data`](/data) 目录。
   * 在 [`languages.json`](/data/languages.json) 文件中查找相关语言的键值及其路径（位于 [`data/languages/`](/data/languages) 文件夹中）。

2. **编辑翻译文件**

   * 打开对应的 JSON 文件（如 [`en.json`](/data/languages/en.json)、`fr.json` 等）。
   * 修改并更新需要改进的翻译文本。

3. **测试修改效果**

   * 启动应用程序，检查更新后的文本是否正确显示。
   * 确保文字在界面中显示完整且布局合理。

     > 💡 如果文字过长，请使用更简短的表达或换行来提高可读性。

4. **提交 Pull Request**

   * 确认无误后，提交更改并创建一个 PR，标题格式如下：

     ```
     fix(language): improved [语言名称] translations
     ```

</div>

---

<div id="adding-a-new-language">

## 🌐 添加新语言

若要贡献一种全新的语言：

1. **更新 `languages.json` 文件**

   * 打开 [`data`](/data) 目录中的 [`languages.json`](/data/languages.json) 文件。
   * 在 JSON 对象中添加语言名称及其简短代码。

     示例：

     ```json
     {
       "English": "en",
       "中文": "zh",
       "Español": "es"
     }
     ```

2. **创建语言文件**

   * 在 [`data/languages`](/data/languages) 文件夹中新建一个以语言代码命名的文件（例如 `es.json`）。
   * 根据现有文件为所有键添加对应的翻译内容。

     示例（`es.json`）：

     ```json
     {
       "video": "Video",
       "playlist": "Lista",
       "add +": "Añadir +",
       "added": "Añadido"
     }
     ```

3. **测试新语言**

   * 运行应用程序并选择你添加的新语言。
   * 检查界面中的间距和可读性是否合适。

4. **提交 Pull Request**

   * 确认无误后，提交你的新文件，并创建一个 PR，标题格式如下：

     ```
     feat(language): added [语言名称] translations
     ```

</div>

---

## 💬 最后

感谢你为改进全球用户体验所做的贡献！
你的语言支持让世界各地的用户都能更轻松地使用本应用。

> ❤️ 出色的工作——你的努力让一切变得更美好！