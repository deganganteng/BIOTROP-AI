from components.subcomponents.Options.OptionPage import *
from components.subcomponents.Options.OptionHandler import *

def Main():
    option = st.selectbox(
        "What can we help you with?",
        (
            "General Information SEAMEO BIOTROP",
            "Research Information",
            "Training and Workshop Information",
            "Collaboration Information",
            "SEAMEO BIOTROP E-Library",
        ),
        index=None,
        placeholder="Select Menu"
    )
    language = st.selectbox(
        "Language",
        (
            "Indonesian",
            "English",
            "Japanese",
            "German",
            "Mandarin",
            "Thai",
        ),
        index=None
    )
    Option(option, language)
