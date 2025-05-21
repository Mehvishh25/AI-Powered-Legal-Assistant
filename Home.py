import streamlit as st

if "screen_width" not in st.session_state:
    st.session_state["screen_width"] = 768

def run():
    st.markdown(
        "<h1 style='font-size:60px;background: linear-gradient(to right, #0B3D2E, #4CAF50);-webkit-background-clip: text;-webkit-text-fill-color: transparent;'>Welcome to LegalHawk</h1>",
        unsafe_allow_html=True,
    )
    st.markdown("<h3 style='color:#0B3D2E;'>Your AI Legal Assistant</h3>", unsafe_allow_html=True)

    st.markdown(
        """
        <p style="font-size: 17px; color: #333;">
            At LegalHawk, we’re revolutionizing the legal experience by combining cutting-edge AI and intelligent support, enabling you to navigate legal complexities efficiently and effectively.
        </p>
        <h2 style="font-size: 30px; color: #0B3D2E;">Features of LegalHawk:</h2>
        <ul style="font-size: 18px; color: #444;">
            <li><b>AI-Powered Legal Assistance</b></li>
            <li><b>Document Summarization</b></li>
            <li><b>PDF Question Answer</b></li>
            <li><b>Legal Queries Chatbot</b></li>
        </ul>
        <div style='background: linear-gradient(to right, #0B3D2E, #4CAF50); padding: 20px; border-radius: 10px; margin-top: 30px;'>
        <h2 style="font-size: 30px; color: white; text-align:center;">Empower Your Legal Journey with LegalHawk!</h2>
        <p style="font-size: 20px; text-align:center; color:white">
            Whether you're a student, a professional, or just someone seeking legal clarity — LegalHawk is your trusted AI companion.
        </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("""<hr style="border: 1px solid #CCC; margin-top:80px;">""", unsafe_allow_html=True)

    def render_footer():
        col1, col2, col3, col4 = st.columns([1, 1, 1, 1])

        with col1:
            st.markdown(
                """
                <div>
                    <h3 style="color: #0B3D2E;">LegalHawk</h3>
                    <p style="color: #666;">Your AI Legal Assistant</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

        with col2:
            st.markdown(
                """
                <div>
                    <h3 style='color:#0B3D2E;'>Services</h3>
                    <ul style="list-style-type: none; padding: 0; color: #444;">
                        <li>Chatbot</li>
                        <li>Legal Dashboard</li>
                        <li>Virtual Consultations</li>
                    </ul>
                </div>
                """,
                unsafe_allow_html=True,
            )

        with col3:
            st.markdown(
                """
                <div>
                    <h3 style="color: #0B3D2E;">Company</h3>
                    <ul style="list-style-type: none; padding: 0; color: #444;">
                        <li>Home</li>
                        <li>About Us</li>
                        <li>Privacy Policy</li>
                    </ul>
                </div>
                """,
                unsafe_allow_html=True,
            )

        with col4:
            st.markdown(
                """
                <div>
                    <h3 style="color: #0B3D2E;">Contact</h3>
                    <ul style="list-style-type: none; padding: 0; color: #444;">
                        <li>Gmail</li>
                        <li>LinkedIn</li>
                        <li>Facebook</li>
                        <li>Instagram</li>
                    </ul>
                </div>
                """,
                unsafe_allow_html=True,
            )

    render_footer()

    st.markdown("""<hr style="border: 1px solid #DDD;">""", unsafe_allow_html=True)

    st.markdown(
        """
        <div style="text-align:center;  color: #777; font-size: 15px;">
            &copy; 2025 LegalHawk. All rights reserved.
        </div>
        """,
        unsafe_allow_html=True,
    )

if __name__ == "__main__":
    run()
