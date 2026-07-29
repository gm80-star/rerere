import streamlit as st

st.set_page_config(
    page_title="공부법 & 상관관계 - 꿈 탐색 갤러리",
    page_icon="📚",
    layout="centered"
)

st.markdown("""
    <style>
    .stApp {
        background-color: #FAF8F5;
        color: #2C2C2C;
    }
    .study-card {
        background-color: #FFFFFF;
        padding: 22px;
        border-radius: 12px;
        border-left: 5px solid #E08D79;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.03);
        margin-bottom: 20px;
    }
    .study-title {
        font-size: 1.1rem;
        font-weight: bold;
        color: #4A3E6D;
        margin-bottom: 6px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h2 style='color: #3A3258;'>📚 MBTI별 맞춤 공부법 & 성적 상관관계</h2>", unsafe_allow_html=True)
st.write("MBTI 유형에 따라 가장 효율적인 학습 스타일과 스트레스 해소법이 다릅니다.")
st.markdown("---")

study_info = {
    'ISTJ': {'style': '체계적이고 정돈된 정석파 학습자', 'strength': '높은 집중력, 꾸준함, 계획 이행력', 'method': '일일 공부 플래너 작성, 오답 노트 구조화', 'stress': '계획대로 마무리했을 때 오는 보상과 수면'},
    'ISFJ': {'style': '성실하고 성심성의껏 공부하는 노력파', 'strength': '세심한 노트 필기, 암기 과목 우수', 'method': '핵심 요약집 만들기, 따뜻하고 정돈된 책상', 'stress': '차 한 잔과 함께하는 조용한 음악, 격려'},
    'INFJ': {'style': '원리와 의미를 파악하는 탐구파', 'strength': '개념의 본질 이해, 통찰력', 'method': '마인드맵 활용, 스토리텔링식 암기', 'stress': '일기 쓰기, 산책하며 생각 정리'},
    'INTJ': {'style': '전략적이고 독자적인 마이웨이 학습자', 'strength': '논리적 분석력, 목표 지향성', 'method': '단권화 교재 작성, 기출 분석', 'stress': '관심 분야 독서 및 혼자만의 시간'},
    'ISTP': {'style': '핵심만 효율적으로 공략하는 실속파', 'strength': '벼락치기 몰입력, 순발력', 'method': '타이머 기법(25분 집중 후 휴식), 실전 모의고사', 'stress': '가벼운 운동, 손으로 할 수 있는 액티비티'},
    'ISFP': {'style': '편안한 환경에서 공부하는 감성파', 'strength': '자율적 환경에서의 몰입', 'method': '예쁜 필기구 활용, 소규모 목표 설정', 'stress': '그림 그리기, 휴식'},
    'INFP': {'style': '상상력과 의미 부여를 통해 공부하는 영감파', 'strength': '문학/언어/사회 과목의 높은 이해도', 'method': '내적 동기 부여, 연관 개념을 이야기처럼 연결', 'stress': '감성적인 음악 감상'},
    'INTP': {'style': '호기심과 논리로 파헤치는 학구파', 'strength': '원리 이해, 창의적 문제 해결', 'method': '"왜?"에 답하는 탐구식 공부', 'stress': '새로운 정보 검색'},
    'ESTP': {'style': '몸으로 느끼고 적용하는 행동파', 'strength': '위기 관리 능력, 대담함', 'method': '친구와 서로 설명해주기, 스터디 그룹', 'stress': '스포츠, 야외 활동'},
    'ESFP': {'style': '즐거운 분위기에서 함께 공부하는 유형', 'strength': '긍정적 에너지, 협동 학습', 'method': '말하면서 외우는 스피킹 학습', 'stress': '친구들과 대화하기'},
    'ENFP': {'style': '열정이 넘치는 융합형 학습자', 'strength': '창의성, 과목 간 연결', 'method': '공부 장소 자주 바꾸기, 뽀모도로 기법', 'stress': '새로운 장소 방문, 수다'},
    'ENTP': {'style': '토론하고 질문하며 진가를 발휘하는 모험가', 'strength': '고난도 응용 문제 해결', 'method': '타인과 토론하며 개념 확립', 'stress': '아이디어 구상'},
    'ESTJ': {'style': '목표를 향해 달려가는 리더형', 'strength': '철저한 시간 관리, 높은 성취욕', 'method': 'D-day 체크리스트, 주간 목표 세분화', 'stress': '방 정리정돈'},
    'ESFJ': {'style': '체계적으로 노력하는 협력가', 'strength': '성실성, 긍정적 관계', 'method': '칭찬과 격려가 있는 멘토링', 'stress': '맛있는 음식 먹기, 감사 일기'},
    'ENFJ': {'style': '비전을 바탕으로 몰입하는 유형', 'strength': '언어/인문 분야 뛰어남', 'method': '남을 가르치듯 공부하기', 'stress': '마음 맞는 사람과의 대화'},
    'ENTJ': {'style': '전략적 기획으로 목표 성적을 달성하는 경영자형', 'strength': '장기적 로드맵 설계, 추진력', 'method': '취약 과목 우선 공략, 성적 추이 분석', 'stress': '자기개발 서적 읽기'}
}

mbti_sel = st.selectbox("🎯 학습 스타일을 볼 MBTI를 선택하세요:", list(study_info.keys()), index=6)
data = study_info[mbti_sel]

st.markdown(f"""
<div class="study-card">
    <div class="study-title">✨ {mbti_sel}: {data['style']}</div>
    <p><b>💪 학습 강점:</b> {data['strength']}</p>
    <p><b>📖 추천 공부 전략:</b> {data['method']}</p>
    <p><b>🧘 스트레스 해소법:</b> {data['stress']}</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")
st.markdown("### 📊 MBTI와 학업 성적의 상관관계 요약")
st.markdown("""
* **J(판단) vs P(인식)**: 꾸준한 내신 성적 관리에서는 **J 성향**의 계획성이 유리한 편이지만, 창의적 수능 응용 문제나 단기 집중력에서는 **P 성향**의 몰입도가 높습니다.
* **N(직관) vs S(감각)**: **N 성향**은 전체 맥락과 비문학/국어/사회 탐구에 강점을 보이고, **S 성향**은 세부 공식과 암기가 중요한 수학/과학/외국어 과목에서 안정적입니다.
* **결론**: 특정 MBTI가 무조건 성적이 높은 것이 아니라, **나의 MBTI에 딱 맞는 공부 전략**을 찾았을 때 가장 큰 성과가 나타납니다!
""")