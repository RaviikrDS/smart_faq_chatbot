import streamlit as st
import requests

st.set_page_config(page_title="Smart FAQ Chatbot", page_icon="🤖")

st.title("📬 Smart FAQ Chatbot")
st.write("Ask a question about company policies, shipping, support, etc.")

# Input from user
question = st.text_input("❓ Your Question:", placeholder="e.g., What is your return policy?")

if st.button("Get Answer"):
    if question.strip() == "":
        st.warning("Please enter a question.")
    else:
        with st.spinner("Thinking..."):
            try:
                response = requests.post("http://localhost:10000/query", json={"question": question})
                if response.status_code == 200:
                    answer = response.json()["answer"]
                    st.success("💬 Answer:")
                    st.write(answer)
                else:
                    st.error("⚠️ Server returned an error.")
            except Exception as e:
                st.error(f"🚫 Failed to connect to backend: {e}")
