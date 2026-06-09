import streamlit as st

# 1. 페이지 기본 설정 🎒
st.set_page_config(
    page_title="하루 한 곡, Mood & Time Music 🎵",
    page_icon="🎧",
    layout="centered"
)

# 2. 러블리한 감성의 커스텀 CSS 🎀
st.markdown("""
    <style>
    .main-title {
        font-size: 2.8rem !important;
        color: #FF8E9E;
        text-align: center;
        font-weight: bold;
        margin-bottom: 5px;
    }
    .sub-title {
        font-size: 1.1rem !important;
        color: #6C5B7B;
        text-align: center;
        margin-bottom: 30px;
    }
    .music-card {
        background-color: #F3F0FF;
        padding: 18px;
        border-radius: 15px;
        border: 2px solid #E1D5FF;
        margin-bottom: 15px;
        text-align: center;
    }
    .music-title {
        color: #4A0E4E;
        font-weight: bold;
        font-size: 1.1rem;
    }
    </style>
""", unsafe_allow_html=True)

# 3. 음악 추천 데이터베이스 🎼 (기분 x 시간대별 K-POP 및 팝송)
# 시간대: 아침/낮 ☀️, 저녁/새벽 🌙
music_db = {
    "신나고 활기찬 기분 🥳🚀": {
        "☀️ 아침이나 낮 시간": [
            {"type": "🇰🇷 K-POP", "title": "NewJeans - OMG 🐰", "desc": "상큼한 리듬으로 오전 에너지 충전 완 가뿐하게 시작해요!"},
            {"type": "🇺🇸 POP", "title": "Dua Lipa - Levitating 🌌", "desc": "둥둥 뜨는 베이스 리듬이 몸을 들썩이게 만들어요!"}
        ],
        "🌙 저녁이나 새벽 시간": [
            {"type": "🇰🇷 K-POP", "title": "세븐틴 (SEVENTEEN) - 아주 NICE 💯", "desc": "밤새도록 식지 않는 에너지를 불태우고 싶을 때!"},
            {"type": "🇺🇸 POP", "title": "The Weeknd - Blinding Lights ⚡", "desc": "화려한 도시의 밤거리를 달리는 듯한 짜릿한 기분!"}
        ]
    },
    "말랑말랑 행복한 기분 🥰🌸": {
        "☀️ 아침이나 낮 시간": [
            {"type": "🇰🇷 K-POP", "title": "아이유 (IU) - 라일락 🔮", "desc": "화창한 햇살 아래 걸으며 들으면 행복이 두 배!"},
            {"type": "🇺🇸 POP", "title": "Taylor Swift - Lover 💗", "desc": "달콤한 꿀을 머금은 듯 온 세상이 핑크빛으로 물들어요."}
        ],
        "🌙 저녁이나 새벽 시간": [
            {"type": "🇰🇷 K-POP", "title": "백현 (BAEKHYUN) - UN Village 🏡", "desc": "은은한 달빛 아래 한가로이 힐링하고 싶을 때 강추!"},
            {"type": "🇺🇸 POP", "title": "Lauv - Paris in the Rain 🌧️", "desc": "포근하고 로맨틱한 밤의 감성에 촉촉하게 젖어보세요."}
        ]
    },
    "차분하고 집중하고 싶은 기분 📜☕": {
        "☀️ 아침이나 낮 시간": [
            {"type": "🇰🇷 K-POP", "title": "AKMU (악뮤) - 어떻게 이별까지 사랑하겠어... 💔", "desc": "잔잔한 멜로디와 가사가 생각에 잠기기 딱 좋아요."},
            {"type": "🇺🇸 POP", "title": "Bruno Major - Nothing ☕", "desc": "따뜻한 커피 한 잔과 함께 독서나 공부할 때 최고의 파트너!"}
        ],
        "🌙 저녁이나 새벽 시간": [
            {"type": "🇰🇷 K-POP", "title": "성시경 - 거리에서 🌧️", "desc": "새벽 감성을 자극하는 꿀성대 목소리에 귀를 맡겨봐요."},
            {"type": "🇺🇸 POP", "title": "Billie Eilish - ocean eyes 🌊", "desc": "몽환적이고 차분한 보이스가 하루를 평온하게 마무리해 줍니다."}
        ]
    },
    "토닥토닥 위로가 필요한 기분 🥺🩹": {
        "☀️ 아침이나 낮 시간": [
            {"type": "🇰🇷 K-POP", "title": "레드벨벳 (Red Velvet) - Daylight ☀️", "desc": "지친 마음에 따스한 햇살 같은 위로를 건네주는 노래예요."},
            {"type": "🇺🇸 POP", "title": "Coldplay - Fix You 🩹", "desc": "다 괜찮아질 거라고 등을 어루만져 주는 든든한 사운드!"}
        ],
        "🌙 저녁이나 새벽 시간": [
            {"type": "🇰🇷 K-POP", "title": "이하이 - 한숨 🌬️", "desc": "오늘 하루도 정말 수고 많았어요. 따스하게 감싸주는 노래."},
            {"type": "🇺🇸 POP", "title": "Lady Gaga - Always Remember Us This Way 🌹", "desc": "가슴 깊은 곳 울림을 주며 마음의 눈물을 닦아주는 명곡."}
        ]
    }
}

# 4. 헤더 영역 디자인 ✨
st.markdown('<div class="main-title">🎵 Mood & Time Music DJ 🎧</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">오늘 내 마음의 날씨는 어떨까? 시간과 기분에 맞는 음악 선물을 받아보세요! 🎁🎈</div>', unsafe_allow_html=True)

st.divider() # 핑키 가로선 🎀

# 5. 사용자 입력 (기분 및 시간 선택) 💭
st.subheader("💡 오늘의 감정 주파수를 맞춰주세요!")

# 귀여운 2열 레이아웃으로 옵션 배치
col1, col2 = st.columns(2)

with col1:
    mood = st.selectbox(
        "🔮 지금 내 기분 상태는?",
        list(music_db.keys())
    )

with col2:
    time_slot = st.selectbox(
        "⏰ 지금은 어떤 시간대인가요?",
        ["☀️ 아침이나 낮 시간", "🌙 저녁이나 새벽 시간"]
    )

st.write("") # 한 줄 띄우기

# 6. 결과 매칭 및 추천 카드 💌
if st.button("🎶 나만을 위한 추천 곡 보기 🎶", use_container_width=True):
    st.balloons() # 축하 풍선 팡팡! 🎈
    
    recommendations = music_db[mood][time_slot]
    
    st.success(f"완벽한 타이밍! 당신을 위한 오늘의 음악 처방전이에요! 💊✨")
    st.write("")
    
    # 추천 음악 2개 시각화 (K-POP / POP)
    card_cols = st.columns(2)
    
    for i, music in enumerate(recommendations):
        with card_cols[i]:
            st.markdown(f"""
                <div class="music-card">
                    <span style="background-color: #FFD2E5; padding: 3px 8px; border-radius: 10px; font-size: 0.8rem; font-weight: bold; color: #FF4B72;">
                        {music['type']}
                    </span>
                    <p class="music-title" style="margin-top: 10px; margin-bottom: 5px;">{music['title']}</p>
                    <p style="font-size: 0.85rem; color: #666; line-height: 1.4;">{music['desc']}</p>
                </div>
            """, unsafe_allow_html=True)

# 7. 귀여운 푸터 🧸
st.divider()
st.caption("💌 음악은 마음을 치료하는 마법이래요! 마음에 드는 곡을 스트리밍 앱에서 검색해 들어보세요. 귀여운 당신의 하루를 언제나 응원해요! 🦄💕")
