import streamlit as st

# 1. 페이지 기본 설정 (가장 상단에 위치해야 합니다!)
st.set_page_config(
    page_title="나의 MBTI 커리어 매칭! 🧭",
    page_icon="🎒",
    layout="centered"
)

# 2. 귀여운 스타일링을 위한 커스텀 CSS (폰트 및 부드러운 느낌)
st.markdown("""
    <style>
    .main-title {
        font-size: 3rem !important;
        color: #FF6B6B;
        text-align: center;
        font-weight: bold;
        margin-bottom: 5px;
    }
    .sub-title {
        font-size: 1.2rem !important;
        color: #4A4A4A;
        text-align: center;
        margin-bottom: 30px;
    }
    .result-box {
        background-color: #FFF0F5;
        padding: 20px;
        border-radius: 15px;
        border: 2px dashed #FFB6C1;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. 데이터베이스 (MBTI별 특징 및 추천 직업)
mbti_jobs = {
    "ISTJ": {"emoji": "📐", "title": "청렴결백한 논리주의자", "jobs": ["회계사 📊", "데이터 분석가 💻", "사서 📚", "경찰관 👮"]},
    "ISFJ": {"emoji": "🛡️", "title": "용감한 수호자", "jobs": ["간호사 🩺", "초등교사 🎒", "사회복지사 🤝", "인사담당자 👥"]},
    "INFJ": {"emoji": "🔮", "title": "선의의 옹호자", "jobs": ["상담심리사 🗣️", "작가 ✍️", "환경운동가 🌱", "인권 변호사 ⚖️"]},
    "INTJ": {"emoji": "🧠", "title": "용의주도한 전략가", "jobs": ["소프트웨어 개발자 👩‍💻", "투자분석가 📈", "교수 🎓", "전략 기획자 🎯"]},
    "ISTP": {"emoji": "🛠️", "title": "만능 재주꾼", "jobs": ["엔지니어 ⚙️", "파일럿 ✈️", "소방관 🚒", "영상 편집자 🎬"]},
    "ISFP": {"emoji": "🎨", "title": "호기심 많은 예술가", "jobs": ["디자이너 🖌️", "파티시에 🍰", "작곡가 🎵", "수의테크니션 🐾"]},
    "INFP": {"emoji": "🧸", "title": "열정적인 중재자", "jobs": ["소설가 📖", "심리치료사 🧠", "일러스트레이터 🎨", "사유지 관리인 🏡"]},
    "INTP": {"emoji": "🧪", "title": "논리적인 사색가", "jobs": ["연구원 🔬", "프로그래머 💻", "경제학자 📉", "철학자 📜"]},
    "ESTP": {"emoji": "⚡", "title": "수완 좋은 활동가", "jobs": ["마케터 📣", "스포츠 에이전트 ⚽", "소방관 🚒", "기업가 🚀"]},
    "ESFP": {"emoji": "🎉", "title": "자유로운 영혼의 연예인", "jobs": ["연예인 🎤", "이벤트 플래너 🎈", "항공 승무원 ✈️", "뮤지컬 배우 🎭"]},
    "ENFP": {"emoji": "🌈", "title": "재기발랄한 활동가", "jobs": ["홍보 전문가 📢", "크리에이터 📹", "카운셀러 💬", "여행 가이드 🗺️"]},
    "ENTP": {"emoji": "💡", "title": "뜨거운 논쟁을 즐기는 변론가", "jobs": ["벤처 캐피탈리스트 💰", "정치인 🏛️", "광고 기획자 📋", "스타트업 창업가 🌟"]},
    "ESTJ": {"emoji": "👔", "title": "엄격한 관리자", "jobs": ["프로젝트 매니저 📅", "은행원 🏦", "법조인 ⚖️", "군 장교 🎖️"]},
    "ESFJ": {"emoji": "🤝", "title": "사교적인 외교관", "jobs": ["호텔리어 🏨", "승무원 🛫", "초등교사 🏫", "고customer 서비스 매니저 ☎️"]},
    "ENFJ": {"emoji": "☀️", "title": "정의로운 사회운동가", "jobs": ["비영리단체 리더 🌍", "교사 👩‍🏫", "정치인 🗣️", "HR 컨설턴트 👔"]},
    "ENTJ": {"emoji": "👑", "title": "대담한 통솔자", "jobs": ["경영 최고책임자(CEO) 💼", "경영 컨설턴트 📊", "변호사 ⚖️", "벤처 투자자 💵"]}
}

# 4. 메인 화면 구성
st.markdown('<div class="main-title">✨ 나의 MBTI 커리어 매칭 ✨</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">내 MBTI에 꼭 맞는 즐겁고 행복한 직업 세계로 떠나볼까요? 🚀🌈</div>', unsafe_allow_html=True)

st.divider() # 귀여운 구분선 🎀

# 5. 사용자 입력 받기
st.subheader("🔮 나의 MBTI를 선택해 주세요!")
selected_mbti = st.selectbox(
    "아래 목록에서 골라보세요 👇",
    list(mbti_jobs.keys()),
    index=0
)

# 6. 결과 출력하기
if selected_mbti:
    info = mbti_jobs[selected_mbti]
    
    st.success(f"짜잔! 여러분을 위한 결과가 준비되었어요! 🎈")
    
    # 귀여운 박스 형태로 결과 출력
    st.markdown(f"""
        <div class="result-box">
            <h3>{info['emoji']} {selected_mbti} : {info['title']}</h3>
            <p style="font-size: 1.1rem; color: #555;">이 성향의 친구들에게는 아래와 같은 멋진 직업들이 잘 어울려요! ⭐</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.write("") # 간격 띄우기
    
    # 추천 직업을 이쁜 카드(Columns) 형태로 배치
    st.subheader("💼 추천하는 꿈의 직업들")
    cols = st.columns(2) # 2열로 배치
    
    for idx, job in enumerate(info['jobs']):
        with cols[idx % 2]:
            st.info(f"✨ **{job}**")

# 7. 푸터 (Footer)로 마무리
st.divider()
st.caption("🎈 본 프로그램은 청소년 및 학생들의 진로 교육을 돕기 위해 재미로 보는 MBTI 기반 직업 추천 서비스입니다. 둥글둥글 예쁜 꿈을 응원해요! 🧸🎈")
