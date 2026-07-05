import streamlit as st
#4B1426
#FFEED6
#17433F
#A5AF79

#f3f6f8	(243,246,248)
#2c6975	(44,105,117)
#253243	(37,50,67)
#eaf2f5	(234,242,245)
#c94c8a	(201,76,138)

def style_background_home():

    st.markdown("""
        <style>
                
            .stApp {
                background: linear-gradient(to right, #FFFFFF, #FFEED6);
            }
                
            .stApp div[data-testid="stColumn"] {
                background-color: white !important;
                padding: 1.5rem !important;
                border-radius: 1.5rem !important;    
            }

        </style>
                """
            ,unsafe_allow_html=True)
    
def style_background_dashboard():

    st.markdown("""
        <style>
                
            .stApp {
                background: linear-gradient(to right, #FFFFFF, #FFEED6);
            }

        </style>
                """
            ,unsafe_allow_html=True)

def style_base_layout():

    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');
        
        /* Hide Top bar of streamlit */

                #MainMenu, footer, header {
                    visibility: hidden
                }   

                .block-container {
                    padding-top: 1.5rem;
                }

                h1 {
                    font-family: 'Poppins', sans-serif !important;
                    font-size: 3.5rem !important;
                    line-height: 0.9 !important;
                    margin-bottom: 0rem !important;
                    color: #4B1426 !important;
                    font-weight: 900;
                }

                h2 {
                    font-family: 'Poppins', sans-serif !important;
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
                    background: #4B1426 !important;
                    color: white !important;
                    padding: 10px 20px !important;
                    border: none !important;
                    transition: transform 0.25s ease-in-out !important;
                }

                button[kind="secondary"] {
                    border-radius: 1.5rem !important;
                    background: #17433F !important;
                    color: white !important;
                    padding: 10px 20px !important;
                    border: none !important;
                    transition: transform 0.25s ease-in-out !important;
                }

                button[kind="tirtary"] {
                    border-radius: 1.5rem !important;
                    background: black !important;
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