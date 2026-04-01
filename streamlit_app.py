"""
English Learner App - Main Streamlit Application
"""
import streamlit as st

# Import configuration and styles
from config import APP_TITLE, APP_ICON
from styles import MAIN_STYLES

# Import data management
from data.words_manager import initialize_session_state

# Import components
from components.sidebar import render_sidebar
from components.card_display import render_card_display

# Setup page configuration
st.set_page_config(page_title=APP_TITLE, page_icon=APP_ICON)

# Apply styles
st.markdown(MAIN_STYLES, unsafe_allow_html=True)

# Initialize session state
initialize_session_state()

# Render sidebar
render_sidebar()

# Main content
st.title("🗂 Мои карточки")

# Render card display
render_card_display()