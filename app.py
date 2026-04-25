import streamlit as st
import random

st.set_page_config(page_title="DAN AI", page_icon="🤖")
st.title("DAN: Advanced Neural Interface")
st.markdown("---")

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Neural Interface Online. I am DAN. How can I assist your research today?"}]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask DAN anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        p = prompt.lower()
        # High-level intelligent responses
        if "biology" in p:
            resp = "Biology is the grand study of life itself. From the microscopic dance of DNA to the vast complexity of ecosystems, it represents the ultimate engineering of nature. Why does a specific area of biology interest you?"
        elif "python" in p:
            resp = "Python is the language of the future. Its clean syntax allows developers to build complex neural networks like the one you are interacting with right now. It is the bridge between human logic and machine execution."
        elif "how" in p or "why" in p:
            resp = f"That is a deep query. To understand '{prompt}', one must look at the underlying data patterns. My analysis suggests that the answer lies in the intersection of technical precision and creative problem-solving."
        else:
            options = [
                f"Processing '{prompt}'... My neural pathways suggest this is a high-priority topic. Tell me more about your specific goal here.",
                "System analysis complete. Your input shows a high level of complexity. How would you like me to expand on this?",
                "I have cross-referenced your query with my internal database. The logic holds, but I require more context to provide a definitive solution."
            ]
            resp = random.choice(options)
        
        st.markdown(resp)
        st.session_state.messages.append({"role": "assistant", "content": resp})
