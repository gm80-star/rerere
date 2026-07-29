import streamlit as st

st.set_page_config(
    page_title="우리나라 MBTI 비율 - 꿈 탐색 갤러리",
    page_icon="📊",
    layout="centered"
)

st.markdown("""
    <style>
    .stApp {
        background-color: #FAF8F5;
        color: #2C2C2C;
    }
    .info-card {
        background-color: #FFFFFF;
        padding: 20px;
        border-radius: 12px;
        border-left: 5px solid #9C88FF;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.03);
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h2 style='color: #3A3258;'>📊 대한민국 MBTI 유형별 분포 비율</h2>", unsafe_allow_html=True)
st.write("우리나라 사람들은 어떤 MBTI 유형이 가장 많을까요? 통계 자료를 바탕으로 한 데이터입니다.")
st.markdown("---")

korea_mbti_data = {
    'ISTJ': 12.8, 'ESTJ': 12.4, 'ENFP': 9.7, 'ISFJ': 8.3,
    'ESFJ': 8.2, 'ESFP': 7.2, 'INFP': 6.7, 'ISFP': 6.5,
    'ESTP': 4.2, 'ISTP': 4.1, 'ENTP': 3.6, 'ENTJ': 3.5,
    'ENFJ': 3.3, 'INTJ': 3.3, 'INTP': 3.2, 'INFJ': 2.9
}

sorted_mbti = sorted(korea_mbti_data.items(), key=lambda x: x[1], reverse=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🔝 가장 높은 비율 TOP 3")
    for rank, (mbti, ratio) in enumerate(sorted_mbti[:3], 1):
        st.markdown(f"**{rank}위: {mbti}** — `{ratio}%`")

with col2:
    st.markdown("### 🎈 가장 희귀한 비율 TOP 3")
    for rank, (mbti, ratio) in enumerate(sorted_mbti[-3:], 1):
        st.markdown(f"**{rank}위: {mbti}** — `{ratio}%`")

st.write("")
st.markdown("### 📈 전체 비율 그래프")
st.bar_chart(korea_mbti_data)

st.markdown("""
<div class="info-card">
    <h4 style="color: #4A3E6D; margin-top:0;">💡 상담 선생님과 나누는 이야기</h4>
    한국 사회에서는 전통적으로 질서와 규칙을 존중하는 <b>ISTJ, ESTJ, ISFJ</b> 비율이 높게 나타납니다.<br>
    만약 내 성향이 비율이 적은 유형(INFJ, INTP 등)에 해당하더라도 걱정하지 마세요! 
    그만큼 남들과 다른 <b>독창적이고 특별한 관점</b>을 가지고 있다는 뜻이랍니다.
</div>
""", unsafe_allow_html=True)