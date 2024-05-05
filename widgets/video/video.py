import tkinter as tk
import webbrowser
import customtkinter as ctk
from typing import List, Union, Any
from tkinter import PhotoImage
from utils import (
    ValueConvertUtility
)
from widgets.components import ThumbnailButton
from services import ThemeManager
from settings import (
    ThemeSettings,
    GeneralSettings,
    ScaleSettings
)


class Video(ctk.CTkFrame):
    """A class representing a video widget."""

    def __init__(
            self,
            master: Any,
            width: int = 0,
            height: int = 0,
            # video info
            video_url: str = "",
            video_title: str = "-------",
            channel: str = "-------",
            thumbnails: List[PhotoImage] = (None, None),
            channel_url: str = "-------",
            length: int = 0):

        super().__init__(
            master=master,
            height=height,
            width=width,
            border_width=1,
            corner_radius=8,
        )

        self.height: int = height
        self.width: int = width
        # video details
        self.video_url: str = video_url
        self.video_title: str = video_title
        self.channel: str = channel
        self.channel_url: str = channel_url
        self.length: int = length
        self.thumbnails: List[PhotoImage] = thumbnails
        # widgets
        self.url_label: Union[tk.Button, None] = None
        self.video_title_label: Union[tk.Button, None] = None
        self.channel_btn: Union[tk.Button, None] = None
        self.len_label: Union[ctk.CTkButton, None] = None
        self.thumbnail_btn: Union[ThumbnailButton, None] = None
        self.remove_btn: Union[ctk.CTkButton, None] = None
        # initialize the object
        self.create_widgets()
        self.set_widgets_sizes()
        self.set_widgets_fonts()
        self.set_widgets_colors()
        self.set_tk_widgets_colors()
        self.set_widgets_accent_color()
        self.place_widgets()
        self.bind_widgets_events()

        # register to Theme Manger for accent color updates & widgets colors updates
        ThemeManager.register_widget(self)

    def set_video_data(self):
        """Display video data on widgets."""
        self.video_title_label.configure(text=f"Title : {self.video_title}")
        self.channel_btn.configure(text=f"Channel : {self.channel}", state="normal")
        self.url_label.configure(text=self.video_url)
        self.len_label.configure(text=ValueConvertUtility.convert_time(self.length))

        self.thumbnail_btn.stop_loading_animation()
        self.thumbnail_btn.configure_thumbnail(thumbnails=self.thumbnails)
        self.thumbnail_btn.configure(state="normal")

        def on_mouse_enter_thumbnail_btn(event):
            self.on_mouse_enter_self(event)
            self.thumbnail_btn.on_mouse_enter(event)

        def on_mouse_leave_thumbnail_btn(event):
            self.on_mouse_leave_self(event)
            self.thumbnail_btn.on_mouse_leave(event)

        self.thumbnail_btn.bind("<Enter>", on_mouse_enter_thumbnail_btn)
        self.thumbnail_btn.bind("<Leave>", on_mouse_leave_thumbnail_btn)
        self.len_label.bind("<Enter>", on_mouse_enter_thumbnail_btn)
        self.len_label.bind("<Leave>", on_mouse_leave_thumbnail_btn)

    def kill(self):
        """Destroy the widget."""
        ThemeManager.unregister_widget(self)
        self.pack_forget()
        self.destroy()

    def create_widgets(self):
        """Create widgets."""
        self.thumbnail_btn = ThumbnailButton(
            master=self,
            state="disabled",
            command=lambda: webbrowser.open(self.video_url),
        )
        self.len_label = ctk.CTkLabel(master=self, text=ValueConvertUtility.convert_time(self.length))
        self.video_title_label = tk.Label(master=self, anchor="w", text=f"Title : {self.video_title}")
        self.channel_btn = tk.Button(
            master=self,
            anchor="w",
            command=lambda: webbrowser.open(self.channel_url),
            relief="sunken",
            state="disabled",
            cursor="hand2",
            text=f"Channel : {self.channel}"
        )
        self.url_label = tk.Label(master=self, anchor="w", text=self.video_url)
        self.remove_btn = ctk.CTkButton(master=self, command=self.kill, text="X", hover=False)

    def set_widgets_fonts(self):
        """Set fonts for widgets."""
        scale = GeneralSettings.settings["scale_r"]

        self.thumbnail_btn.configure(font=("arial", int(14 * scale), "bold"))
        self.len_label.configure(font=("arial", int(10 * scale), "bold"))
        self.video_title_label.configure(font=('arial', int(10 * scale), 'normal'))
        self.channel_btn.configure(font=('arial', int(10 * scale), 'bold'))
        self.url_label.configure(font=('arial', int(10 * scale), "italic underline"))
        self.remove_btn.configure(font=("arial", 12 * scale, "bold"))

    def set_widgets_sizes(self):
        """Set sizes for widgets."""
        scale = GeneralSettings.settings["scale_r"]

        self.len_label.configure(width=1, height=1)
        self.video_title_label.configure(height=1)
        self.channel_btn.configure(bd=0, height=1)
        self.url_label.configure(height=1)
        self.remove_btn.configure(width=22 * scale, height=22 * scale, border_spacing=0)

    def set_widgets_accent_color(self):
        """Set accent color for widgets."""
        self.configure(border_color=ThemeSettings.settings["root"]["accent_color"]["normal"])
        self.thumbnail_btn.configure(
            fg=(ThemeSettings.settings["root"]["accent_color"]["normal"]),
        )
        self.channel_btn.configure(activeforeground=ThemeSettings.settings["root"]["accent_color"]["normal"])
        self.url_label.configure(fg=ThemeSettings.settings["root"]["accent_color"]["normal"])

    def update_widgets_accent_color(self):
        """Update accent color for widgets."""
        self.set_widgets_accent_color()

    def set_tk_widgets_colors(self):
        """Set colors for the Tk widgets."""
        self.thumbnail_btn.configure(
            bg=ThemeManager.get_color_based_on_theme_mode(ThemeSettings.settings["video_object"]["fg_color"]["normal"]),
            disabledforeground=ThemeManager.get_color_based_on_theme_mode(
                ThemeSettings.settings["video_object"]["text_color"]["normal"]
            ),
            activebackground=ThemeManager.get_color_based_on_theme_mode(
                ThemeSettings.settings["video_object"]["fg_color"]["normal"]
            )
        )
        self.video_title_label.configure(
            bg=ThemeManager.get_color_based_on_theme_mode(ThemeSettings.settings["video_object"]["fg_color"]["normal"]),
            fg=ThemeManager.get_color_based_on_theme_mode(
                ThemeSettings.settings["video_object"]["text_color"]["normal"]
            )
        )
        self.url_label.configure(
            bg=ThemeManager.get_color_based_on_theme_mode(ThemeSettings.settings["video_object"]["fg_color"]["normal"]),
        )
        self.channel_btn.configure(
            bg=ThemeManager.get_color_based_on_theme_mode(ThemeSettings.settings["video_object"]["fg_color"]["normal"]),
            fg=ThemeManager.get_color_based_on_theme_mode(
                ThemeSettings.settings["video_object"]["btn_text_color"]["normal"]
            ),
            activebackground=ThemeManager.get_color_based_on_theme_mode(
                ThemeSettings.settings["video_object"]["fg_color"]["normal"]
            ),
        )

    def update_widgets_colors(self):
        """Update colors for widgets."""
        self.set_tk_widgets_colors()

    def set_widgets_colors(self):
        """Set colors for widgets."""
        self.configure(fg_color=ThemeSettings.settings["video_object"]["fg_color"]["normal"])
        self.remove_btn.configure(
            fg_color=ThemeSettings.settings["video_object"]["error_color"]["normal"],
            text_color=ThemeSettings.settings["video_object"]["remove_btn_text_color"]["normal"]
        )

    def on_mouse_enter_self(self, event):
        """Handle mouse enter event for self."""
        self.configure(
            fg_color=ThemeSettings.settings["video_object"]["fg_color"]["hover"],
            border_color=ThemeSettings.settings["root"]["accent_color"]["hover"]
        )
        self.thumbnail_btn.configure(
            bg=ThemeManager.get_color_based_on_theme_mode(ThemeSettings.settings["video_object"]["fg_color"]["hover"])
        )
        self.video_title_label.configure(
            bg=ThemeManager.get_color_based_on_theme_mode(ThemeSettings.settings["video_object"]["fg_color"]["hover"])
        )
        self.channel_btn.configure(
            bg=ThemeManager.get_color_based_on_theme_mode(ThemeSettings.settings["video_object"]["fg_color"]["hover"])
        )
        self.url_label.configure(
            bg=ThemeManager.get_color_based_on_theme_mode(ThemeSettings.settings["video_object"]["fg_color"]["hover"])
        )

    def on_mouse_leave_self(self, event):
        """Handle mouse leave event for self."""
        self.configure(
            fg_color=ThemeSettings.settings["video_object"]["fg_color"]["normal"],
            border_color=ThemeSettings.settings["root"]["accent_color"]["normal"]
        )
        self.thumbnail_btn.configure(
            bg=ThemeManager.get_color_based_on_theme_mode(ThemeSettings.settings["video_object"]["fg_color"]["normal"])
        )
        self.video_title_label.configure(
            bg=ThemeManager.get_color_based_on_theme_mode(ThemeSettings.settings["video_object"]["fg_color"]["normal"])
        )
        self.channel_btn.configure(
            bg=ThemeManager.get_color_based_on_theme_mode(ThemeSettings.settings["video_object"]["fg_color"]["normal"])
        )
        self.url_label.configure(
            bg=ThemeManager.get_color_based_on_theme_mode(ThemeSettings.settings["video_object"]["fg_color"]["normal"])
        )

    def bind_widgets_events(self):
        """Bind events for widgets."""
        self.bind("<Enter>", self.on_mouse_enter_self)
        self.bind("<Leave>", self.on_mouse_leave_self)
        for child_widgets in self.winfo_children():
            child_widgets.bind("<Enter>", self.on_mouse_enter_self)
            child_widgets.bind("<Leave>", self.on_mouse_leave_self)
            try:
                for sub_child_widgets in child_widgets.winfo_children():
                    sub_child_widgets.bind("<Enter>", self.on_mouse_enter_self)
                    sub_child_widgets.bind("<Leave>", self.on_mouse_leave_self)
            except Exception as error:
                print(f"@1 Video.py > err : {error}")

        def on_mouse_enter_channel_btn(event):
            self.channel_btn.configure(
                fg=ThemeManager.get_color_based_on_theme_mode(
                    ThemeSettings.settings["video_object"]["btn_text_color"]["hover"]
                ),
            )
            self.on_mouse_enter_self(event)

        def on_mouse_leave_channel_btn(_event):
            self.channel_btn.configure(
                fg=ThemeManager.get_color_based_on_theme_mode(
                    ThemeSettings.settings["video_object"]["btn_text_color"]["normal"]
                )
            )

        self.channel_btn.bind("<Enter>", on_mouse_enter_channel_btn)
        self.channel_btn.bind("<Leave>", on_mouse_leave_channel_btn)

        def on_mouse_enter_remove_btn(event):
            self.remove_btn.configure(
                fg_color=ThemeSettings.settings["video_object"]["error_color"]["hover"],
                text_color=ThemeSettings.settings["video_object"]["remove_btn_text_color"]["hover"]
            )
            self.on_mouse_enter_self(event)

        def on_mouse_leave_remove_btn(event):
            self.remove_btn.configure(
                fg_color=ThemeSettings.settings["video_object"]["error_color"]["normal"],
                text_color=ThemeSettings.settings["video_object"]["remove_btn_text_color"]["normal"]
            )
            self.on_mouse_leave_self(event)

        self.remove_btn.bind("<Enter>", on_mouse_enter_remove_btn)
        self.remove_btn.bind("<Leave>", on_mouse_leave_remove_btn)

    def place_widgets(self):
        """Place widgets."""
        scale = GeneralSettings.settings["scale_r"]
        y = ScaleSettings.settings["Video"][str(scale)]

        thumbnail_width = int((self.height - 4) / 9 * 16)
        self.thumbnail_btn.place(x=5, y=1, width=thumbnail_width, height=self.height-4)
        self.remove_btn.place(relx=1, x=-25 * scale, y=3 * scale)
        self.len_label.place(rely=1, y=-10 * scale, x=thumbnail_width - 1, anchor="e")
        self.video_title_label.place(x=thumbnail_width + 10 * scale, y=y[0], relwidth=1, width=-500 * scale)
        self.channel_btn.place(x=thumbnail_width + 10 * scale, y=y[1], relwidth=1, width=-500 * scale)
        self.url_label.place(x=thumbnail_width + 10 * scale, y=y[2], relwidth=1, width=-500 * scale)
