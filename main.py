import streamlit as st
from streamlit_option_menu import option_menu
import Home, blogs, chatbot, summarizer, pdf_qa

st.set_page_config(
    page_title="LegalHawk - AI Powered Legal Assistant",
    layout="wide",
)

logo_icon = 'LegalHawk.png'
st.sidebar.image(logo_icon, width=180)

st.sidebar.markdown(
    """
    <style>
        .trackit-text {
            font-size: 45px;
            font-weight: bold;
            font-family: sans-serif;
            background: linear-gradient(to right, #0B3D2E, #4CAF50);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            position: relative;
            top: -20px;
        }
    </style>
    <div class="trackit-text">LegalHawk</div>
    """,
    unsafe_allow_html=True
)

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_apps(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):
        with st.sidebar:
            main_menu = option_menu(
                menu_title="Features", 
                options=["Home", "Legal Document Summarizer", "PDF Question Answer", "Chatbot", "Blogs"],
                icons=["house", "file-earmark-text", "file-earmark-question", "robot", "journal-text"],
                menu_icon="star", 
                default_index=0,
                styles={
                    "container": {"padding": "5!important", "background-color": "#F5F5F5"},
                    "icon": {"color": "#0B3D2E", "font-size": "18px"},
                    "nav-link": {
                        "color": "black",
                        "font-size": "16px",
                        "font-weight": "500"
                    },
                    "nav-link:hover": {"background-color": "#B0B0B0"},
                    "nav-link-selected": {
                        "background-color": "#0B3D2E",
                        "color": "white"
                    },
                }
            )

        for app in self.apps:
            if main_menu == app["title"]:
                app["function"]()

multiapp = MultiApp()
multiapp.add_apps("Home", Home.run)
multiapp.add_apps("Legal Document Summarizer", summarizer.run)
multiapp.add_apps("PDF Question Answer", pdf_qa.run)
multiapp.add_apps("Chatbot", chatbot.run)
multiapp.add_apps("Blogs", blogs.run)

multiapp.run()
