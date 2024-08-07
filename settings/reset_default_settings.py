from typing import Dict
import os
from utils import JsonUtility, FileCopy


class ResetDefaultSettings(object):
    general: Dict = {
        "automatic_download": {"quality": 0, "status": "disable"},
        "create_sep_path_for_playlists": "false",
        "create_sep_path_for_qualities": "false",
        "create_sep_path_for_videos_audios": "false",
        "download_directory": f"C:\\users\\{os.getlogin()}\\downloads\\PyTube Downloader\\",
        "lang_code": "en",
        "language": "English",
        "load_thumbnail": "false",
        "max_simultaneous_downloads": 1,
        "max_simultaneous_loads": 1,
        "re_download_automatically": "false",
        "reload_automatically": "false",
        "update_delay": 0.5,
        "window_geometry": "900x500+0+0",
    }
    appearance: Dict = {
        "alert_window": {"msg_color": {"normal": "#ee0000"}},
        "context_menu": {"text_color": ["#101010", "#eeeeee"]},
        "navigation_button": {
            "fg_color": {
                "hover": ["#f2f4f9", "#32373e"],
                "normal": ["#e2e4e9", "#21262d"],
            }
        },
        "navigation_frame": {
            "fg_color": {
                "hover": ["#ffffff", "#0a0c12"],
                "normal": ["#ffffff", "#0a0c12"],
            }
        },
        "opacity": 100.0,
        "opacity_r": 1.0,
        "radio_btn": {
            "text_color": {
                "hover": ["#606060", "#ffffff"],
                "normal": ["#909090", "#939aa2"],
            }
        },
        "root": {
            "accent_color": {
                "default": "true",
                "hover": "#903efb",
                "normal": "#7a14ff",
            },
            "fg_color": {
                "hover": ["#ffffff", "#0a0c12"],
                "normal": ["#ffffff", "#0a0c12"],
            },
            "text_color": {
                "hover": ["#0a0c12", "#ffffff"],
                "normal": ["#0a0c12", "#ffffff"],
            },
            "theme_mode": 0,
        },
        "scale": 100.0,
        "scale_r": 1.0,
        "settings_panel": {
            "accent_colors": {
                "0": {"hover": "#5f4ff1", "normal": "#412ff0"},
                "1": {"hover": "#903efb", "normal": "#7a14ff"},
                "2": {"hover": "#57A1EB", "normal": "#284CEA"},
                "3": {"hover": "#FF851B", "normal": "#FF7F11"},
                "4": {"hover": "#0cf749", "normal": "#22c14b"},
                "5": {"hover": "#03A9F4", "normal": "#039BE5"},
                "6": {"hover": "#9C27B0", "normal": "#8E24AA"},
                "7": {"hover": "#CDDC39", "normal": "#C0CA33"},
                "8": {"hover": "#009688", "normal": "#00796B"},
                "9": {"hover": "#FF5722", "normal": "#F4511E"},
                "a": {"hover": "#FF9800", "normal": "#F57C00"},
                "b": {"hover": "#795548", "normal": "#6D4C41"},
                "c": {"hover": "#607D8B", "normal": "#546E7A"},
                "d": {"hover": "#FF5252", "normal": "#E53935"},
                "e": {"hover": "#FF3D00", "normal": "#FFAB00"},
                "f": {"hover": "#7091e6", "normal": "#8697c4"},
            },
            "nav_text_color": ["#252525", "#dddddd"],
            "text_color": ["#141212", "#eeeeee"],
            "warning_color": {"hover": "#ff3131", "normal": "#f95568"},
        },
        "url_adding_button": {
            "fg_color": {
                "hover": ["#ffffff", "#272c33"],
                "normal": ["#f4f6fd", "#161b22"],
            }
        },
        "url_entry": {
            "border_color": {
                "hover": ["#d0d7de", "#40464e"],
                "normal": ["#d0d7de", "#30363d"],
            },
            "fg_color": {
                "hover": ["#f9faff", "#21262d"],
                "normal": ["#f6f8fa", "#161b22"],
            },
            "text_color": {
                "hover": ["#1f2328", "#dddddd"],
                "normal": ["#636c76", "#ffffff"],
            },
        },
        "video_object": {
            "btn_fg_color": {
                "hover": ["#ffffff", "#2c2e34"],
                "normal": ["#dedede", "#1b1d23"],
            },
            "btn_text_color": {
                "hover": ["#202020", "#ffffff"],
                "normal": ["#505050", "#aaaaaa"],
            },
            "error_color": {"hover": "#ff3131", "normal": "#ee0000"},
            "fg_color": {
                "hover": ["#ffffff", "#161616"],
                "normal": ["#eeeeee", "#121212"],
            },
            "remove_btn_text_color": {
                "hover": ["#ffffff", "#ffffff"],
                "normal": ["#cdcdcd", "#cdcdcd"],
            },
            "text_color": {
                "hover": ["#707070", "#aaaaaa"],
                "normal": ["#404040", "#bbbbbb"],
            },
        },
    }

    @staticmethod
    def reset():
        JsonUtility.write_to_file("./data/general.json", ResetDefaultSettings.general)
        JsonUtility.write_to_file(
            "./data/appearance.json", ResetDefaultSettings.appearance
        )
        FileCopy.file_copy("backup")
