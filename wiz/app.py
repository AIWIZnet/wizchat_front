import streamlit as st

def main():
    st.title("Wiznet 엔지니어 피드백 챗봇")

    st.write("""
    ## 엔지니어 여러분들의 피드백 부탁드립니다. 질문 / 답변 / 수정되어야하는 내용
    """)

    # HTML 코드를 사용하여 iframe을 임베딩
    st.markdown("""
    <iframe src="https://www.chatbase.co/chatbot-iframe/6gHc7VLgwpf2oti8pG28X" width="100%" style="height: 700px" frameborder="0"></iframe>
    """, unsafe_allow_html=True)

    st.write("""
    ## 수정된 내용 기입 부탁 드립니다 [위즈네트 챗봇피드백 엑셀](https://wiznetio-my.sharepoint.com/:x:/g/personal/simon_wiznet_io/EWucOi1dSLdMqQcGB5SmMlsBIkVjSz_PQJDUmob05SgVMA?e=tuygrg)
    """)

if __name__ == "__main__":
    main()
