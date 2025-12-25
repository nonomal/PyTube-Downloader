<div id="adding-a-new-theme">

# 🎨 主题贡献指南

通过创建或改进配色主题来增强 **PyTube Downloader** 的视觉体验。
你的设计贡献让应用更时尚、更易用、更令人愉悦！

---

## 🌈 添加新主题

若要向应用程序添加新的配色主题：

1. **更新 `themes.json` 文件**

   * 打开 [`data`](/data) 目录中的 [`themes.json`](/data/themes.json) 文件。
   * 添加一个新的条目，键为主题显示名称，值为主题文件名（不带 `.json` 后缀）。

     示例：

     ```json
     {
       "Dark Default": "dark_default",
       "Light Default": "light_default",
       "Cyberpunk Black": "cyberpunk_black",
       "Gold Black": "gold_black"  // 新主题
     }
     ```

2. **创建主题文件**

   * 进入 [`data/themes`](/data/themes) 目录。
   * 使用与 `themes.json` 中相同的名称创建一个新的 JSON 文件。

     示例：

     ```
     data/themes/gold_black.json
     ```

3. **添加主题颜色**

   * 打开新建的主题文件，使用 HEX 颜色代码定义配色方案。
   * 可以参考现有主题进行修改。

     示例（`gold_black.json`）：

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

4. **测试你的主题**

   * 启动 **PyTube Downloader**。
   * 打开 **外观设置（Appearance Settings）** 并选择新添加的主题。
   * 检查所有 UI 元素是否清晰可见，并确保颜色在各组件间协调一致。

5. **提交 Pull Request**

   * 确认无误后，提交你的主题文件并创建一个 PR，标题格式如下：

     ```
     feat(theme): added [主题名称] theme
     ```

</div>

---

<div id="improve-current-themes">

## 🧹 改进现有主题

如果你想修复或优化现有主题：

1. **找到主题文件**

   * 进入 [`data/themes`](/data/themes) 目录。
   * 打开需要修改的对应 `.json` 主题文件。

2. **编辑并调整颜色**

   * 按需要更新颜色值。
   * 确保界面元素之间的文字清晰、对比度良好。

3. **测试主题**

   * 检查所有文字和界面组件在不同状态（正常、悬停、警告）下的可读性。
   * 根据需要微调颜色以提升整体色彩协调性。

4. **提交 Pull Request**

   * 确认无误后，提交更改并创建一个 PR，标题格式如下：

     ```
     fix(theme): improved [主题名称] theme colors
     ```

</div>

---

## 💬 最后

感谢你为 **PyTube Downloader** 设计做出的贡献！
你的创意让应用的界面更优雅、更个性化，为全球用户带来更好的体验。 🌈

> 🎨 继续探索吧 —— 细微的配色调整也能带来巨大的视觉提升！
