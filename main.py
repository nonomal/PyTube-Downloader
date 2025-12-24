from app import App
from settings import (
    AppearanceSettings,
    GeneralSettings
)
import threading
from services import (
    LanguageManager,
    ThemeManager,
    InformationManager
)

try:
    # configure settings
    GeneralSettings.initialize()
    AppearanceSettings.initialize()
    LanguageManager.initialize()
    ThemeManager.initialize()
    InformationManager.initialize()
    
    # Initialize app.
    app = App()
    app.after(100, threading.Thread(target=app.initialize, daemon=True).start)

    # just run the app        
    app.run()
except Exception as error:
    print("main.py L-27:", error)

# Codes under here will only execute when the app is closed
