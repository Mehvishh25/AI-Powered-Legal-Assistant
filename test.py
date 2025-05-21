import streamlit as st
import google.generativeai as genai

# ==== HARDCODE YOUR API KEY HERE ====
GOOGLE_API_KEY = "AIzaSyBb0yOnYLBoicKe8SEajKCeMxqqAzneyzI"  # Replace with your actual key

# ==== Configure Gemini ====
genai.configure(api_key=GOOGLE_API_KEY)

# ==== Create model instance ====
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

# ==== Streamlit App ====
def run():
    st.set_page_config(page_title="⚖️ Legal Q&A Chatbot", page_icon="⚖️")

    st.title("⚖️ Legal Q&A Chatbot")
    st.markdown("Ask any legal question. This chatbot uses **Gemini 1.5 Flash** to respond in simple terms.")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Text input
    user_input = st.text_input("💬 Enter your legal question:")

    if st.button("Ask") and user_input.strip() != "":
        with st.spinner("🤖 Thinking..."):
            try:
                prompt = f"You are a helpful legal assistant. Answer this question in simple terms:\n\n{user_input}"
                response = model.generate_content(prompt)
                reply = response.text.strip()

                # Save to history
                st.session_state.chat_history.append(("🧑 You", user_input))
                st.session_state.chat_history.append(("🤖 Bot", reply))

            except Exception as e:
                st.error(f"❌ Error: {e}")

    # Show chat history
    if st.session_state.chat_history:
        st.subheader("💬 Chat History")
        for sender, msg in st.session_state.chat_history:
            st.markdown(f"**{sender}:** {msg}")

    # Clear chat
    if st.button("🗑️ Clear Chat"):
        st.session_state.chat_history = []

    st.markdown("---")
    st.markdown("💡 **Note:** This chatbot provides general legal information, not professional legal advice.")

# Run the app
if __name__ == "__main__":
    run()
