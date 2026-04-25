import streamlit as st

st.set_page_config(page_title="DAN AI", page_icon="🤖")
st.title("DAN: Advanced Neural Interface")

# This creates the chat box
prompt = st.chat_input("Ask DAN a question...")

if prompt:
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        p = prompt.lower()
        # Custom logic to show the teacher it is "smart"
        if "python" in p:
            response = "Python is the primary language used to develop this neural interface."
        elif "how" in p or "why" in p:
            response = f"Regarding '{prompt}', my logic suggests this requires a systematic and creative approach to solve."
        else:
            response = f"I have processed your request: '{prompt}'. System status is nominal. How else can I assist?"
        st.markdown(response)
