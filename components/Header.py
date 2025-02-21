import components.subcomponents.Logo as Img
from components.subcomponents.Logo import *
import streamlit as st
import streamlit as st

def Header() :
    st.set_page_config(
        page_title="Biotrop AI",
        page_icon="./Image/Logo.png",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    
    Img.image(["./Image/MainLogo.png"])
    
    st.markdown(
        """
        <div style="text-align: center; margin-top: 20px;">
            <h1 style="font-size: 52px; color: #333;">Biotrop AI</h1>
            <p style="font-size: 18px; color: #555;">Welcome to AI Biotrop!</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.write("")