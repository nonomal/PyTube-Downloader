from typing import Any, Callable, List
import customtkinter as ctk
from services import (
    ThemeManager,
    LanguageManager,
    DownloadManager
)
from settings import (
    GeneralSettings,
    AppearanceSettings
)
from utils import (
    SettingsValidateUtility
)


class NetworkPanel(ctk.CTkFrame):
    def __init__(
            self,
            master: Any = None,
            general_settings_change_callback: Callable = None):

        super().__init__(
            master=master,
            fg_color=AppearanceSettings.settings["root"]["fg_color"]["normal"]
        )

        self.simultaneous_load_label = ctk.CTkLabel(
            master=self,
            text_color=AppearanceSettings.settings["settings_panel"]["text_color"]
        )
        self.dash1_label = ctk.CTkLabel(
            master=self,
            text=":",
            text_color=AppearanceSettings.settings["settings_panel"]["text_color"]
        )
        self.simultaneous_load_entry = ctk.CTkEntry(
            master=self,
            justify="right",
            fg_color=AppearanceSettings.settings["root"]["fg_color"]["normal"],
            text_color=AppearanceSettings.settings["settings_panel"]["text_color"]
        )

        self.simultaneous_load_range_label = ctk.CTkLabel(
            master=self,
            text="(1-10)",
            text_color=AppearanceSettings.settings["settings_panel"]["text_color"]
        )
        
        #----------------------------------------------------------------------
        self.simultaneous_download_label = ctk.CTkLabel(
            master=self,
            text_color=AppearanceSettings.settings["settings_panel"]["text_color"]
        )
        self.dash2_label = ctk.CTkLabel(
            master=self,
            text=":",
            text_color=AppearanceSettings.settings["settings_panel"]["text_color"]
        )
        self.simultaneous_download_entry = ctk.CTkEntry(
            master=self,
            justify="right",
            fg_color=AppearanceSettings.settings["root"]["fg_color"]["normal"],
            text_color=AppearanceSettings.settings["settings_panel"]["text_color"]
        )

        self.simultaneous_download_range_label = ctk.CTkLabel(
            master=self,
            text="(1-10)",
            text_color=AppearanceSettings.settings["settings_panel"]["text_color"]
        )
        
        #----------------------------------------------------------------------
        self.simultaneous_convert_label = ctk.CTkLabel(
            master=self,
            text_color=AppearanceSettings.settings["settings_panel"]["text_color"]
        )
        self.dash3_label = ctk.CTkLabel(
            master=self,
            text=":",
            text_color=AppearanceSettings.settings["settings_panel"]["text_color"]
        )
        self.simultaneous_convert_entry = ctk.CTkEntry(
            master=self,
            justify="right",
            fg_color=AppearanceSettings.settings["root"]["fg_color"]["normal"],
            text_color=AppearanceSettings.settings["settings_panel"]["text_color"]
        )
        
        #----------------------------------------------------------------------
        self.automatic_download_label = ctk.CTkLabel(
            master=self,
            text_color=AppearanceSettings.settings["settings_panel"]["text_color"]
        )

        self.dash4_label = ctk.CTkLabel(
            master=self,
            text=":",
            text_color=AppearanceSettings.settings["settings_panel"]["text_color"]
        )

        self.automatic_download_switch_state = ctk.StringVar(value=None)
        self.automatic_download_switch = ctk.CTkSwitch(
            master=self,
            text="",
            command=self.change_automatic_download,
            onvalue="enable",
            offvalue="disable",
            variable=self.automatic_download_switch_state
        )

        self.automatic_download_quality_label = ctk.CTkLabel(
            master=self,
            text_color=AppearanceSettings.settings["settings_panel"]["text_color"]
        )

        self.dash5_label = ctk.CTkLabel(
            master=self,
            text=":",
            text_color=AppearanceSettings.settings["settings_panel"]["text_color"]
        )

        self.automatic_download_quality_combo_box = ctk.CTkComboBox(
            master=self,
            dropdown_fg_color=AppearanceSettings.settings["root"]["fg_color"]["normal"],
            command=self.change_automatic_download_quality,
            text_color=AppearanceSettings.settings["settings_panel"]["text_color"],
            fg_color=AppearanceSettings.settings["root"]["fg_color"]["normal"],
            width=140 * AppearanceSettings.settings["scale_r"],
            height=28 * AppearanceSettings.settings["scale_r"],
            values=DownloadManager.resolutions[::-1]
        )

        self.automatic_download_info_label = ctk.CTkLabel(
            master=self,
        )

        self.load_thumbnail_label = ctk.CTkLabel(
            master=self,
            text_color=AppearanceSettings.settings["settings_panel"]["text_color"]
        )

        self.dash6_label = ctk.CTkLabel(
            master=self,
            text=":",
            text_color=AppearanceSettings.settings["settings_panel"]["text_color"]
        )
        
        self.load_thumbnail_switch_state = ctk.BooleanVar(value=None)
        self.load_thumbnail_switch = ctk.CTkSwitch(
            master=self,
            text="",
            command=self.change_thumbnail_load,
            onvalue=True,
            offvalue=False,
            variable=self.load_thumbnail_switch_state
        )
        
        # -------------------------------------------------------------
        
        self.reload_automatically_label = ctk.CTkLabel(
            master=self,
            text_color=AppearanceSettings.settings["settings_panel"]["text_color"]
        )

        self.dash7_label = ctk.CTkLabel(
            master=self,
            text=":",
            text_color=AppearanceSettings.settings["settings_panel"]["text_color"]
        )
        
        self.reload_automatically_switch_state = ctk.BooleanVar(value=None)
        self.reload_automatically_switch = ctk.CTkSwitch(
            master=self,
            text="",
            command=self.change_reload_automatically,
            onvalue=True,
            offvalue=False,
            variable=self.reload_automatically_switch_state
        )
        
        # -------------------------------------------------------------
        
        self.re_download_automatically_label = ctk.CTkLabel(
            master=self,
            text_color=AppearanceSettings.settings["settings_panel"]["text_color"]
        )

        self.dash8_label = ctk.CTkLabel(
            master=self,
            text=":",
            text_color=AppearanceSettings.settings["settings_panel"]["text_color"]
        )
        
        self.re_download_automatically_switch_state = ctk.BooleanVar(value=None)
        self.re_download_automatically_switch = ctk.CTkSwitch(
            master=self,
            text="",
            command=self.change_re_download_automatically,
            onvalue=True,
            offvalue=False,
            variable=self.re_download_automatically_switch_state
        )
        
        # -------------------------------------------------------------

        self.apply_changes_button = ctk.CTkButton(
            master=self,
            state="disabled",
            height=24,
            width=50,
            command=self.apply_network_settings,
            text_color=AppearanceSettings.settings["settings_panel"]["text_color"]
        )
        
        self.settings_reset_button = ctk.CTkButton(
            master=self, 
            text_color=AppearanceSettings.settings["settings_panel"]["text_color"],
            command=self.reset_settings
        )

        # use to track anything is changed or not
        self.automatic_download_state_changed: bool = False
        self.automatic_download_quality_changed: bool = False
        self.simultaneous_download_count_changed: bool = False
        self.simultaneous_convert_count_changed: bool = False
        self.simultaneous_load_count_changed: bool = False
        self.load_thumbnail_state_changed: bool = False
        self.reload_automatically_state_changed: bool = False
        self.re_download_automatically_state_changed: bool = False

        # track values validity
        self.simultaneous_load_count_valid: bool = True
        self.simultaneous_download_count_valid: bool = True
        self.simultaneous_convert_count_valid: bool = True

        self.general_settings_change_callback = general_settings_change_callback
        self.set_widgets_accent_color()
        self.set_widgets_fonts()
        self.set_widgets_texts()
        self.set_widgets_sizes()
        self.place_widgets()
        self.bind_widgets()
        self.configure_values()

        ThemeManager.register_widget(self)
        LanguageManager.register_widget(self)
        
    def reset_settings(self):
        self.simultaneous_load_entry.delete(0, 'end')
        self.simultaneous_load_entry.insert("end", 1)
        
        self.simultaneous_download_entry.delete(0, 'end')
        self.simultaneous_download_entry.insert("end", 1)
        
        self.simultaneous_convert_entry.delete(0, 'end')
        self.simultaneous_convert_entry.insert("end", 1)
        
        self.automatic_download_switch.deselect()
        
        self.automatic_download_quality_combo_box.configure(state="normal")
        self.automatic_download_quality_combo_box.set(
            "1080p"
        )
        self.automatic_download_quality_combo_box.configure(state="disabled")
        
        self.load_thumbnail_switch.select()
        self.reload_automatically_switch.deselect()
        self.re_download_automatically_switch.deselect()
        
        self.apply_network_settings()
        
    def apply_network_settings(self):
        GeneralSettings.settings["max_simultaneous_loads"] = int(self.simultaneous_load_entry.get())
        GeneralSettings.settings["max_simultaneous_downloads"] = int(self.simultaneous_download_entry.get())
        GeneralSettings.settings["max_simultaneous_converts"] = int(self.simultaneous_convert_entry.get())
        GeneralSettings.settings["automatic_download"]["status"] = self.automatic_download_switch_state.get()
        GeneralSettings.settings["automatic_download"]["quality"] = self.automatic_download_quality_combo_box.get()
        GeneralSettings.settings["load_thumbnail"] = self.load_thumbnail_switch_state.get()
        GeneralSettings.settings["reload_automatically"] = self.reload_automatically_switch_state.get()
        GeneralSettings.settings["re_download_automatically"] = self.re_download_automatically_switch_state.get()
        self.general_settings_change_callback()
        self.apply_changes_button.configure(state="disabled")

        self.automatic_download_state_changed = False
        self.automatic_download_quality_changed = False
        self.simultaneous_download_count_changed = False
        self.simultaneous_load_count_changed = False
        self.simultaneous_convert_count_changed = False
        self.load_thumbnail_state_changed = False
        self.reload_automatically_state_changed = False
        self.re_download_automatically_state_changed = False

    def change_re_download_automatically(self):
        if GeneralSettings.settings["re_download_automatically"] != self.re_download_automatically_switch.get():
            self.re_download_automatically_state_changed = True
        else:
            self.re_download_automatically_state_changed = False
        self.set_apply_button_state()
    
    def change_reload_automatically(self):
        if GeneralSettings.settings["reload_automatically"] != self.reload_automatically_switch.get():
            self.reload_automatically_state_changed = True
        else:
            self.reload_automatically_state_changed = False
        self.set_apply_button_state()
    
    def change_thumbnail_load(self):
        if GeneralSettings.settings["load_thumbnail"] != self.load_thumbnail_switch.get():
            self.load_thumbnail_state_changed = True
        else:
            self.load_thumbnail_state_changed = False
        self.set_apply_button_state()

    def change_automatic_download_quality(self, quality: str):
        if GeneralSettings.settings["automatic_download"]["quality"] != quality:
            self.automatic_download_quality_changed = True
        else:
            self.automatic_download_quality_changed = False
        self.set_apply_button_state()

    def change_automatic_download(self):
        if GeneralSettings.settings["automatic_download"]["status"] != self.automatic_download_switch_state.get():
            self.automatic_download_state_changed = True
        else:
            self.automatic_download_state_changed = False
        if self.automatic_download_switch_state.get() == "disable":
            self.automatic_download_quality_combo_box.configure(state="disabled")
        else:
            self.automatic_download_quality_combo_box.configure(state="normal")
        self.set_apply_button_state()

    def simultaneous_load_count_check(self, _event):
        value = self.simultaneous_load_entry.get()
        if SettingsValidateUtility.validate_simultaneous_count(value, with_range=True):
            self.simultaneous_load_count_valid = True
            if int(value) != GeneralSettings.settings["max_simultaneous_loads"]:
                self.simultaneous_load_count_changed = True
            else:
                self.simultaneous_load_count_changed = False
        else:
            self.simultaneous_load_count_valid = False
        self.set_apply_button_state()

    def simultaneous_download_count_check(self, _event):
        value = self.simultaneous_download_entry.get()
        if SettingsValidateUtility.validate_simultaneous_count(value, with_range=True):
            self.simultaneous_download_count_valid = True
            if int(value) != GeneralSettings.settings["max_simultaneous_downloads"]:
                self.simultaneous_download_count_changed = True
            else:
                self.simultaneous_download_count_changed = False
        else:
            self.simultaneous_download_count_valid = False
        self.set_apply_button_state()
        
    def simultaneous_convert_count_check(self, _event):
        value = self.simultaneous_convert_entry.get()
        if SettingsValidateUtility.validate_simultaneous_count(value, with_range=False):
            self.simultaneous_convert_count_valid = True
            if int(value) != GeneralSettings.settings["max_simultaneous_converts"]:
                self.simultaneous_convert_count_changed = True
            else:
                self.simultaneous_convert_count_changed = False
        else:
            self.simultaneous_convert_count_valid = False
        self.set_apply_button_state()

    def set_apply_button_state(self):
        if (any((self.simultaneous_download_count_changed, self.simultaneous_load_count_changed,
                 self.automatic_download_state_changed, self.automatic_download_quality_changed,
                 self.load_thumbnail_state_changed, self.reload_automatically_state_changed,
                 self.re_download_automatically_state_changed, self.simultaneous_convert_count_changed)) and
                all((self.simultaneous_load_count_valid, self.simultaneous_download_count_valid, self.simultaneous_convert_count_valid))):
            self.apply_changes_button.configure(state="normal")
        else:
            self.apply_changes_button.configure(state="disabled")

    def bind_widgets(self):
        self.simultaneous_load_entry.bind("<KeyRelease>", self.simultaneous_load_count_check)
        self.simultaneous_download_entry.bind("<KeyRelease>", self.simultaneous_download_count_check)
        self.simultaneous_convert_entry.bind("<KeyRelease>", self.simultaneous_convert_count_check)

    # set default values to widgets
    def configure_values(self):
        self.simultaneous_load_entry.insert(
            "end",
            GeneralSettings.settings["max_simultaneous_loads"]
        )
        self.simultaneous_download_entry.insert(
            "end",
            GeneralSettings.settings["max_simultaneous_downloads"]
        )
        self.simultaneous_convert_entry.insert(
            "end",
            GeneralSettings.settings["max_simultaneous_converts"]
        )
        
        self.automatic_download_quality_combo_box.set(
            GeneralSettings.settings["automatic_download"]["quality"]
        )

        if GeneralSettings.settings["automatic_download"]["status"] == "enable":
            self.automatic_download_switch.select()
            self.automatic_download_switch_state.set("enable")
        else:
            self.automatic_download_switch_state.set("disable")
            self.automatic_download_quality_combo_box.configure(state="disabled")
        
        if GeneralSettings.settings["load_thumbnail"]:
            self.load_thumbnail_switch.select()
            self.load_thumbnail_switch_state.set(True)
        else:
            self.load_thumbnail_switch_state.set(False)
        
        if GeneralSettings.settings["reload_automatically"]:
            self.reload_automatically_switch.select()
            self.reload_automatically_switch_state.set(True)
        else:
            self.reload_automatically_switch_state.set(False)
        
        if GeneralSettings.settings["re_download_automatically"]:
            self.re_download_automatically_switch.select()
            self.re_download_automatically_switch_state.set(True)
        else:
            self.re_download_automatically_switch_state.set(False)
        
    def update_widgets_accent_color(self):
        self.set_widgets_accent_color()

    def set_widgets_accent_color(self):
        self.simultaneous_load_entry.configure(
            border_color=AppearanceSettings.settings["root"]["accent_color"]["normal"]
        )
        self.simultaneous_download_entry.configure(
            border_color=AppearanceSettings.settings["root"]["accent_color"]["normal"]
        )
        self.simultaneous_convert_entry.configure(
            border_color=AppearanceSettings.settings["root"]["accent_color"]["normal"]
        )
        self.automatic_download_info_label.configure(
            text_color=AppearanceSettings.settings["root"]["accent_color"]["normal"]
        )
        self.automatic_download_switch.configure(
            button_color=AppearanceSettings.settings["root"]["accent_color"]["normal"],
            button_hover_color=AppearanceSettings.settings["root"]["accent_color"]["hover"],
            progress_color=AppearanceSettings.settings["root"]["accent_color"]["hover"]
        )
        self.automatic_download_quality_combo_box.configure(
            button_color=AppearanceSettings.settings["root"]["accent_color"]["normal"],
            button_hover_color=AppearanceSettings.settings["root"]["accent_color"]["hover"],
            border_color=AppearanceSettings.settings["root"]["accent_color"]["normal"],
            dropdown_hover_color=AppearanceSettings.settings["root"]["accent_color"]["hover"]
        )
        self.load_thumbnail_switch.configure(
            button_color=AppearanceSettings.settings["root"]["accent_color"]["normal"],
            button_hover_color=AppearanceSettings.settings["root"]["accent_color"]["hover"],
            progress_color=AppearanceSettings.settings["root"]["accent_color"]["hover"]
        )
        self.reload_automatically_switch.configure(
            button_color=AppearanceSettings.settings["root"]["accent_color"]["normal"],
            button_hover_color=AppearanceSettings.settings["root"]["accent_color"]["hover"],
            progress_color=AppearanceSettings.settings["root"]["accent_color"]["hover"]
        )
        self.re_download_automatically_switch.configure(
            button_color=AppearanceSettings.settings["root"]["accent_color"]["normal"],
            button_hover_color=AppearanceSettings.settings["root"]["accent_color"]["hover"],
            progress_color=AppearanceSettings.settings["root"]["accent_color"]["hover"]
        )
        self.settings_reset_button.configure(
            fg_color=AppearanceSettings.settings["root"]["accent_color"]["normal"],
            hover_color=AppearanceSettings.settings["root"]["accent_color"]["hover"]
        )
        self.apply_changes_button.configure(
            fg_color=AppearanceSettings.settings["root"]["accent_color"]["normal"],
            hover_color=AppearanceSettings.settings["root"]["accent_color"]["hover"]
        )

    def place_widgets(self):
        scale = AppearanceSettings.settings["scale_r"]
        pady = 16 * scale

        self.simultaneous_load_label.grid(row=0, column=0, padx=(100, 0), pady=(50, 0), sticky="w")
        self.dash1_label.grid(row=0, column=1, padx=(30, 30), pady=(50, 0), sticky="w")
        self.simultaneous_load_entry.grid(row=0, column=2, pady=(50, 0), sticky="w")
        self.simultaneous_load_range_label.grid(row=0, column=3, pady=(50, 0), padx=(20, 0), sticky="w")

        self.simultaneous_download_label.grid(row=1, column=0, padx=(100, 0), pady=(pady, 0), sticky="w")
        self.dash2_label.grid(row=1, column=1, padx=(30, 30), pady=(pady, 0), sticky="w")
        self.simultaneous_download_entry.grid(row=1, column=2, pady=(pady, 0), sticky="w")
        self.simultaneous_download_range_label.grid(row=1, column=3, pady=(pady, 0), padx=(20, 0), sticky="w")
        
        self.simultaneous_convert_label.grid(row=2, column=0, padx=(100, 0), pady=(pady, 0), sticky="w")
        self.dash3_label.grid(row=2, column=1, padx=(30, 30), pady=(pady, 0), sticky="w")
        self.simultaneous_convert_entry.grid(row=2, column=2, pady=(pady, 0), sticky="w")

        self.automatic_download_label.grid(row=3, column=0, padx=(100, 0), pady=(pady, 0), sticky="w")
        self.dash4_label.grid(row=3, column=1, padx=(30, 30), pady=(pady, 0), sticky="w")
        self.automatic_download_switch.grid(row=3, column=2, pady=(pady, 0), sticky="w")

        self.automatic_download_quality_label.grid(row=4, column=0, padx=(100, 0), pady=(pady, 0), sticky="e")
        self.dash5_label.grid(row=4, column=1, padx=(30, 30), pady=(pady, 0), sticky="w")
        self.automatic_download_quality_combo_box.grid(row=4, column=2, pady=(pady, 0), sticky="w")

        self.automatic_download_info_label.grid(
            row=5, column=0, columnspan=8,
            padx=(100 + (20 * scale), 0), pady=(10, 0), sticky="w"
        )

        self.load_thumbnail_label.grid(row=6, column=0, padx=(100, 0), pady=(pady, 0), sticky="w")
        self.dash6_label.grid(row=6, column=1, padx=(30, 30), pady=(pady, 0), sticky="w")
        self.load_thumbnail_switch.grid(row=6, column=2, pady=(pady, 0), sticky="w")

        self.reload_automatically_label.grid(row=7, column=0, padx=(100, 0), pady=(pady, 0), sticky="w")
        self.dash7_label.grid(row=7, column=1, padx=(30, 30), pady=(pady, 0), sticky="w")
        self.reload_automatically_switch.grid(row=7, column=2, pady=(pady, 0), sticky="w")
        
        self.re_download_automatically_label.grid(row=8, column=0, padx=(100, 0), pady=(pady, 0), sticky="w")
        self.dash8_label.grid(row=8, column=1, padx=(30, 30), pady=(pady, 0), sticky="w")
        self.re_download_automatically_switch.grid(row=8, column=2, pady=(pady, 0), sticky="w")
        
        self.apply_changes_button.grid(row=9, column=3, pady=(pady, 0), sticky="w")
        
        self.settings_reset_button.grid(row=9, column=4, pady=(pady, 0), padx=(20*scale, 0), sticky="w")
        
    def set_widgets_sizes(self):
        scale = AppearanceSettings.settings["scale_r"]
        self.simultaneous_load_entry.configure(width=140 * scale, height=28 * scale)
        self.simultaneous_download_entry.configure(width=140 * scale, height=28 * scale)
        self.simultaneous_convert_entry.configure(width=140 * scale, height=28 * scale)
        self.automatic_download_switch.configure(switch_width=36 * scale, switch_height=18 * scale)
        self.automatic_download_quality_combo_box.configure(width=140 * scale, height=28 * scale)
        self.load_thumbnail_switch.configure(switch_width=36 * scale, switch_height=18 * scale)
        self.reload_automatically_switch.configure(switch_width=36 * scale, switch_height=18 * scale)
        self.re_download_automatically_switch.configure(switch_width=36 * scale, switch_height=18 * scale)
        self.apply_changes_button.configure(width=50 * scale, height=24 * scale)
        
        self.settings_reset_button.configure(width=80*scale, height=24 * scale)

    def set_widgets_texts(self):
        self.simultaneous_load_label.configure(
            text=LanguageManager.data["maximum_simultaneous_loads"]
        )
        self.simultaneous_download_label.configure(
            text=LanguageManager.data["maximum_simultaneous_downloads"]
        )
        self.simultaneous_convert_label.configure(
            text=LanguageManager.data["maximum_simultaneous_converts"]
        )
        self.automatic_download_label.configure(
            text=LanguageManager.data["automatic_video/playlist_download"]
        )
        self.automatic_download_quality_label.configure(
            text=LanguageManager.data["download_quality"]
        )
        self.automatic_download_info_label.configure(
            text=LanguageManager.data["automatic_download_info"]
        )
        self.load_thumbnail_label.configure(
            text=LanguageManager.data["load_video_thumbnail"]
        )
        self.reload_automatically_label.configure(
            text=LanguageManager.data["auto-reload_failed_videos"]
        )
        self.re_download_automatically_label.configure(
            text=LanguageManager.data["auto-re-download_failed_videos"]
        )
        self.apply_changes_button.configure(
            text=LanguageManager.data["apply"]
        )
        self.settings_reset_button.configure(
            text=LanguageManager.data["reset"]
        )
        
    def update_widgets_text(self):
        self.set_widgets_texts()

    def set_widgets_fonts(self):
        scale = AppearanceSettings.settings["scale_r"]
        title_font = ("Segoe UI", 13 * scale, "bold")
        self.simultaneous_load_label.configure(font=title_font)
        self.dash1_label.configure(font=title_font)
        self.simultaneous_download_label.configure(font=title_font)
        self.dash2_label.configure(font=title_font)
        self.simultaneous_convert_label.configure(font=title_font)
        self.dash3_label.configure(font=title_font)
        self.automatic_download_label.configure(font=title_font)
        self.dash4_label.configure(font=title_font)
        self.automatic_download_quality_label.configure(font=title_font)
        self.dash5_label.configure(font=title_font)
        self.load_thumbnail_label.configure(font=title_font)
        self.dash6_label.configure(font=title_font)
        self.reload_automatically_label.configure(font=title_font)
        self.dash7_label.configure(font=title_font)
        self.re_download_automatically_label.configure(font=title_font)
        self.dash8_label.configure(font=title_font)
        
        
        self.simultaneous_download_range_label.configure(font=title_font)
        self.simultaneous_load_range_label.configure(font=title_font)

        value_font = ("Segoe UI", 13 * scale, "normal")
        self.simultaneous_download_entry.configure(font=value_font)
        self.simultaneous_load_entry.configure(font=value_font)
        self.simultaneous_convert_entry.configure(font=value_font)
        self.automatic_download_info_label.configure(font=value_font)
        self.automatic_download_quality_combo_box.configure(font=value_font, dropdown_font=value_font)
        
        button_font = ("Segoe UI", 13 * scale, "bold")
        self.apply_changes_button.configure(font=button_font)
        
        self.settings_reset_button.configure(font=("Segoe UI", 11 * scale, "bold"))

    def update_widgets_colors(self):
        """Update colors for the widgets."""
