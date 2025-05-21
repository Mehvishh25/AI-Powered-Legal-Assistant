import streamlit as st
import google.generativeai as genai

# ===== HARDCODED API KEY =====
GOOGLE_API_KEY = "AIzaSyBb0yOnYLBoicKe8SEajKCeMxqqAzneyzI"  # 🔐 Replace with your actual Gemini API key

# ===== Gemini Config =====
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

# ===== Main App =====
def run():

    # Custom Styles
    st.markdown("""
        <style>
            .main {
                background-color: #f0fdf4;
            }
            .chat-bubble-user {
                background-color: #d1fae5;
                color: #065f46;
                padding: 12px;
                border-radius: 10px;
                margin-bottom: 10px;
            }
            .chat-bubble-bot {
                background-color: #bbf7d0;
                color: #064e3b;
                padding: 12px;
                border-radius: 10px;
                margin-bottom: 10px;
            }
            .stTextInput > div > div > input {
                background-color: #ecfdf5;
                border: 1px solid #10b981;
            }
        </style>
    """, unsafe_allow_html=True)

    # Title
    st.markdown(
        "<h1 style='font-size:48px;background: linear-gradient(to right, #0B3D2E, #4CAF50);-webkit-background-clip: text;-webkit-text-fill-color: transparent;'>LegalHawk Chatbot</h1>",
        unsafe_allow_html=True
    )
    st.markdown("<h3 style='color:#065f46;'>AI-Powered Legal Q&A Assistant</h3>", unsafe_allow_html=True)

    # Initialize Chat History
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Input
    user_input = st.text_input("🧑‍⚖️ Ask your legal question:")

    # Ask button
    if st.button("Ask"):
        if user_input.strip():
            with st.spinner("⚖️ Thinking..."):
                try:
                    prompt = f"You are a helpful AI legal assistant. Explain the following question in simple terms:\n{user_input}"
                    response = model.generate_content(prompt)
                    reply = response.text.strip()

                    # Save chat
                    st.session_state.chat_history.append(("🧑 You", user_input))
                    st.session_state.chat_history.append(("🤖 LegalHawk", reply))

                except Exception as e:
                    st.error(f"❌ Error: {e}")

    # Display chat
    if st.session_state.chat_history:
        st.markdown("<h4 style='color:#065f46;'>Chat History:</h4>", unsafe_allow_html=True)
        for sender, message in st.session_state.chat_history:
            css_class = "chat-bubble-user" if sender == "🧑 You" else "chat-bubble-bot"
            st.markdown(f'<div class="{css_class}"><strong>{sender}:</strong> {message}</div>', unsafe_allow_html=True)

    # Clear button
    if st.button("Clear Chat"):
        st.session_state.chat_history = []

    # Footer
    st.markdown("<hr style='border: 1px solid #DDD;'>", unsafe_allow_html=True)
    st.markdown("""
        <div style="text-align:center; font-size:14px; color: #777;">
            &copy; 2025 LegalHawk. All rights reserved.
        </div>
    """, unsafe_allow_html=True)

# Run the app
if __name__ == "__main__":
    run()
