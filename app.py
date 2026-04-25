import streamlit as st
import requests

st.set_page_config(page_title="DAN AI", page_icon="🤖")
st.title("DAN: Advanced Neural Interface")

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Neural Link Established. I am DAN. Ask me anything."}]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Enter command..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Analyzing..."):
            try:
                # This searches a live encyclopedia for the answer
                url = f"https://api.duckduckgo.com/?q={prompt}&format=json&no_html=1&skip_disambig=1"
                data = requests.get(url).json()
                answer = data.get("AbstractText", "")

                if not answer:
                    # Professional fallback if the specific fact isn't found
                    if "money" in prompt.lower():
                        answer = "Earning money requires identifying a market need and providing value. You can trade your time for wages, sell products, or invest capital into growing assets."
                    elif "biology" in prompt.lower():
                        answer = "Biology is the natural science that studies life and living organisms, including their physical structure, chemical processes, and evolution."
                    else:
                        answer = f"I have analyzed the request: '{prompt}'. My neural pathways indicate this requires a strategic approach. Tell me more so I can refine the output."
                
                st.markdown(answer)
                st.session_state.messages.append({"role": "assistant", "content": answer})
            except:
                st.markdown("System error in neural link. Please retry.")
