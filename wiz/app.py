import streamlit as st

def main():
    st.title("Wiznet 엔지니어 피드백 챗봇 🤖")

    st.markdown("""
    <div style='background-color: #f2f2f2; padding: 10px; border-radius: 5px;'>
        <h2 style='font-size: 24px; color: #333;'>📢 엔지니어 여러분들의 피드백 부탁드립니다!</h2>
        <p style='font-size: 18px; color: #666;'>질문, 답변, 수정되어야 하는 내용 등을 공유해 주세요.</p>
    </div>
    """, unsafe_allow_html=True)

    # HTML 코드를 사용하여 iframe을 임베딩
    st.markdown("""
    <iframe src="https://www.chatbase.co/chatbot-iframe/6gHc7VLgwpf2oti8pG28X" width="100%" style="height: 700px; border-radius: 5px;" frameborder="0"></iframe>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style='background-color: #f2f2f2; padding: 10px; border-radius: 5px;'>
        <h2 style='font-size: 24px; color: #333;'>🔗 수정된 내용은 아래 링크로 확인하세요</h2>
        <a href='https://wiznetio-my.sharepoint.com/:x:/g/personal/simon_wiznet_io/EWucOi1dSLdMqQcGB5SmMlsBIkVjSz_PQJDUmob05SgVMA?e=tuygrg' style='font-size: 18px; color: #007bff;'>SharePoint 링크로 이동</a>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
