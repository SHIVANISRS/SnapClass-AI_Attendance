import streamlit as st

def style_background_home():

    st.markdown("""
        <style>
                
            .stApp {
                background: #EBEDE3;
            }
                
            .stApp div[data-testid="stColumn"] {
                background-color: white !important;
                padding: 2rem !important;
                border-radius: 1.5rem !important;    
            }

        </style>
                """
            ,unsafe_allow_html=True)
    
def style_background_dashboard():

    st.markdown("""
        <style>
                
            .stApp {
                background: #EBEDE3;
            }

        </style>
                """
            ,unsafe_allow_html=True)

def style_base_layout():

    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Bungee&family=Passion+One:wght@700&family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');
                
        /* Hide Top bar of streamlit */

                #MainMenu, footer, header {
                    visibility: hidden
                }   

                .block-container {
                    padding-top: 1.5rem;
                }

                h1 {
                    font-family: 'Bungee', cursive !important;
                    font-size: 3.5rem !important;
                    line-height: 0.9 !important;
                    margin-bottom: 0rem !important;
                    color: #4B1426 !important;
                    font-weight: 900;
                }

                h2 {
                    font-family: 'Bungee', cursive !important;
                    font-size: 2.5rem !important;
                    line-height: 1 !important;
                    margin-bottom: 0rem !important;
                    color: #4B1426 !important;
                    font-weight: 900;
                }

                h3, h4, p {
                    font-family: "Outfit", sans-serif;
                }

                button {
                    border-radius: 1.5rem !important;
                    background-color: #4B1426 !important;
                    color: white !important;
                    padding: 10px 20px !important;
                    border: none !important;
                    transition: transform 0.25s ease-in-out !important;
                }

                button[kind="secondary"] {
                    border-radius: 1.5rem !important;
                    background-color: #17433F !important;
                    color: white !important;
                    padding: 10px 20px !important;
                    border: none !important;
                    transition: transform 0.25s ease-in-out !important;
                }

                button[kind="tertiary"] {
                    border-radius: 1.5rem !important;
                    background-color: black !important;
                    color: white !important;
                    padding: 10px 20px !important;
                    border: none !important;
                    transition: transform 0.25s ease-in-out !important;
                }

                button:hover {
                    transform: scale(1.05)
                }
        </style>
                """
            ,unsafe_allow_html=True)