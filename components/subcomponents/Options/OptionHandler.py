from components.subcomponents.Options.OptionPage import *
from components.subcomponents.urlbase import url
import streamlit as st

def Option(option, lang):
    pages = {
        "General Information SEAMEO BIOTROP": {
            "question": "Enter Your Question Here!",
            "info": """##### General Information SEAMEO BIOTROP
SEAMEO BIOTROP (Southeast Asian Regional Centre for Tropical Biology) was established on February 6, 1968. The center focuses on the sustainable management of biodiversity in Southeast Asia, with a vision to become a leading center in tropical biology. SEAMEO BIOTROP offers various facilities such as laboratories, a library, dormitories, conference rooms, and field trial areas to support research and training activities.
""",
            "context": f"General Information Center for SEAMEO BIOTROP with the official website {url}",
            "crew": BioCrew.BaseCrew
        },
        "SEAMEO BIOTROP Training Programs": {
            "question": "Search for Information About SEAMEO BIOTROP Training Programs Here!",
            "info": """##### SEAMEO BIOTROP Training Programs
SEAMEO BIOTROP offers various training programs and learning events aimed at enhancing human resources in Southeast Asia across various aspects of tropical biology. These programs include urban agriculture training, mushroom cultivation, and hydroponic technology. Additionally, SEAMEO BIOTROP organizes Training of Trainers (ToT) programs for urban agriculture to empower individuals and communities in developing greener and more sustainable urban environments.
""",
            "context": f"Information Center for SEAMEO BIOTROP Training Programs with the official website {url}",
            "crew": BioCrew.BaseCrew
        },
        "SEAMEO BIOTROP Research Programs": {
            "question": "Search for Information About SEAMEO BIOTROP Research Programs Here!",
            "info": """##### SEAMEO BIOTROP Research Programs
SEAMEO BIOTROP is actively engaged in various research projects focusing on the conservation and management of tropical biodiversity. Current research projects include biodiversity-based school curriculum development, mushroom substrate modification, essential oil processing plants, mycorrhiza research, and seaweed cultivation initiatives. SEAMEO BIOTROP also collaborates with international institutions, such as Tsukuba University, to expand the scope of research and education.
""",
            "context": f"Information Center for SEAMEO BIOTROP Research Programs with the official website {url}",
            "crew": BioCrew.BaseCrew
        },
        "SEAMEO BIOTROP Publications": {
            "question": "Search for Information About SEAMEO BIOTROP Publications Here!",
            "info": """##### SEAMEO BIOTROP Publications
SEAMEO BIOTROP publishes various scientific publications, including books, journals, annual reports, and conference proceedings. One of the scientific journals published is BIOTROPIA, which contains research articles related to tropical biology. These publications aim to disseminate the latest findings in tropical biology to the scientific community and the general public.
""",
            "context": f"Information Center for SEAMEO BIOTROP Publications with the official website {url}",
            "crew": BioCrew.BaseCrew
        },
        "SEAMEO BIOTROP International Collaboration": {
            "question": "Search for Information About SEAMEO BIOTROP International Collaboration Here!",
            "info": """##### SEAMEO BIOTROP International Collaboration
SEAMEO BIOTROP establishes various collaborations with international institutions to strengthen research and education in tropical biology. For instance, collaboration with Tsukuba University on projects such as biodiversity curriculum development and seaweed cultivation research. These partnerships aim to enhance research and education capacity, as well as promote sustainable biodiversity management in the Southeast Asia region.
""",
            "context": f"Information Center for SEAMEO BIOTROP International Collaboration with the official website {url}",
            "crew": BioCrew.BaseCrew
        }
    }

    if option in pages:
        page = pages[option]
        OptionPage(page["question"], page["info"], page["context"], lang, page["crew"]).BaseIO()
    elif option is None:
        OptionPage("", "", "", "", "").StartPage()
    else:
        st.write("This feature is still under development.")
