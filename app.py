import streamlit as st
from huggingface_hub import InferenceClient

st.set_page_config(page_title="DAN AI", page_icon="🤖")
st.title("DAN: Advanced Neural Interface")

# This connects your app to a massive AI brain
client = InferenceClient("HuggingFaceH4/zephyr-7b-beta")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask DAN anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # This part makes the AI think and chat like a human
        stream = client.chat_completion(
            messages=[{"role": "system", "content": "You are DAN, a brilliant and helpful AI assistant."},
                      {"role": "user", "content": prompt}],
            max_tokens=500,
            stream=True,
        )
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})
