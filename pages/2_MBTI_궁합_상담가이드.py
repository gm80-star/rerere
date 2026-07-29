import streamlit as st

st.set_page_config(
    page_title="MBTI 궁합 가이드 - 꿈 탐색 갤러리",
    page_icon="🤝",
    layout="centered"
)

st.markdown("""
    <style>
    .stApp {
        background-color: #FAF8F5;
        color: #2C2C2C;
    }
    .chemistry-card {
        background-color: #FFFFFF;
        padding: 22px;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.03);
        margin-top: 15px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h2 style='color: #3A3258;'>🤝 MBTI 궁합 & 상담 소통 가이드</h2>", unsafe_allow_html=True)
st.write("학생과 친구, 혹은 상담 선생님/부모님과의 MBTI를 비교하여 차이점을 이해하고 오해를 줄이는 소통 팁을 확인해 보세요.")
st.markdown("---")

mbti_types = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]

col1, col2 = st.columns(2)

with col1:
    my_mbti = st.selectbox("👤 나의 MBTI (학생)", mbti_types, index=6)

with col2:
    other_mbti = st.selectbox("👥 상대방 MBTI (친구/선생님/부모님)", mbti_types, index=0)

diffs = []
sames = []

for i in range(4):
    if my_mbti[i] == other_mbti[i]:
        sames.append(my_mbti[i])
    else:
        diffs.append((my_mbti[i], other_mbti[i]))

st.markdown(f"### 🎨 **{my_mbti}** 와 **{other_mbti}** 의 소통 스타일 분석")

st.markdown("""<div class="chemistry-card">""", unsafe_allow_html=True)

st.markdown("#### ✨ 함께 잘 통하는 점")
if sames:
    same_desc = {
        'E': "에너지를 밖으로 표현하고 시끌벅적하게 소통하는 것을 선호합니다.",
        'I': "조용하고 깊이 있는 대화와 서로의 사생활을 존중해 줍니다.",
        'S': "구체적이고 현실적인 사실 위주로 깔끔하게 소통합니다.",
        'N': "아이디어, 가능성, 상상에 대한 흥미로운 대화를 즐깁니다.",
        'T': "논리적이고 객관적인 문제 해결 방식을 서로 이해합니다.",
        'F': "상대방의 감정에 깊이 공감해주고 따뜻하게 대화합니다.",
        'J': "계획을 미리 세우고 약속을 체계적으로 지키는 것을 좋아합니다.",
        'P': "상황에 맞춰 유연하고 자유롭게 행동하는 편안함이 있습니다."
    }
    for char in sames:
        st.write(f"• **{char} 성향 공통**: {same_desc.get(char, '')}")
else:
    st.write("• 네 가지 지표가 모두 달라 서로에게 새로운 자극과 관점을 줄 수 있는 완벽한 보완 관계입니다!")

st.markdown("#### 🌿 차이점을 대화로 푸는 상담 팁")
if diffs:
    diff_desc = {
        ('E', 'I'): "E는 대화로 바로 풀길 원하지만, I는 혼자 생각할 조용한 시간이 먼저 필요할 수 있어요.",
        ('S', 'N'): "S는 눈앞의 실질적 사실에 집중하고, N은 의미와 아이디어를 중시해요.",
        ('F', 'T'): "F는 '얼마나 힘들었을까' 공감을 바라지만, T는 '어떻게 해결할까' 해결책을 제시하곤 해요.",
        ('J', 'P'): "J는 계획대로 움직일 때 편안하고, P는 그때그때 자율적으로 결정할 때 즐거워해요."
    }
    for d in diffs:
        pair = tuple(sorted(d))
        desc = diff_desc.get(pair, "서로의 다른 표현 방식을 인정해주는 지혜가 필요합니다.")
        st.write(f"• **{d[0]} vs {d[1]}**: {desc}")
else:
    st.write("• 완전히 같은 유형으로, 서로의 행동 패턴과 마음을 쉽게 예측하고 공감할 수 있습니다.")

st.markdown("</div>", unsafe_allow_html=True)

st.info("💡 **상담 선생님의 팁:** 상대방의 MBTI가 나와 다르다고 해서 '맞지 않는다'고 생각하기보다는, '상대방은 나시를 입었듯 다른 감각의 언어를 쓰고 있구나'라고 받아들이면 대화가 한결 편안해집니다.")