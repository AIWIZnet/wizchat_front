import streamlit as st

def main():
    st.title("Wiznet 엔지니어 피드백 챗봇")

    st.write("""
    ## Wiznet 엔지니어 피드백 챗봇을 아래에서 사용할 수 있습니다.
    """)

    # HTML 코드를 사용하여 iframe을 임베딩
    st.markdown("""
    <iframe src="https://www.chatbase.co/chatbot-iframe/6gHc7VLgwpf2oti8pG28X" width="100%" style="height: 700px" frameborder="0"></iframe>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()