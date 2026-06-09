import streamlit as st

# 1. 페이지 기본 설정 🎒
st.set_page_config(
    page_title="내 마음의 주크박스 🎶",
    page_icon="🦄",
    layout="centered"
)

# 2. 러블리 파스텔톤 커스텀 CSS ✨
st.markdown("""
    <style>
    .main-title {
        font-size: 2.8rem !important;
        color: #FF7B94;
        text-align: center;
        font-weight: bold;
        margin-bottom: 5px;
    }
    .sub-title {
        font-size: 1.1rem !important;
        color: #7A6F8F;
        text-align: center;
        margin-bottom: 30px;
    }
    .music-box {
        background-color: #FFF9E6;
        padding: 20px;
        border-radius: 20px;
        border: 2px dashed #FFD166;
        text-align: center;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.05);
    }
    .song-tag {
        background-color: #FFCCD5;
        color: #FF477E;
        padding: 4px 10px;
        border-radius: 50px;
        font-size: 0.8rem;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# 3. 세분화된 음악 데이터베이스 🎼
# 기분(6가지) x 시간대(4가지)
music_db = {
    "눈떠보니 피곤해... 충전이 필요해 😴⚡": {
        "🌅 상쾌한 아침 (06시~11시)": {"kpop": "부석순 - 파이팅 해야지 🔥", "pop": "Justin Bieber - Beauty And A Beat 🥁", "desc": "무거운 눈을 번쩍 뜨게 만들어 줄 인간 비타민 같은 조합!"},
        "☀️ 나른한 한낮 (11시~17시)": {"kpop": "NCT DREAM - Smoothie 🥤", "pop": "Sabrina Carpenter - Espresso ☕", "desc": "오후의 잠기를 확 쫓아내 줄 톡 쏘는 탄산음료 같은 노래들이에요!"},
        "🌆 노을 지는 저녁 (17시~22시)": {"kpop": "이영지 - Small Girl 꿀조합 🍯", "pop": "Post Malone - Sunflower 🌻", "desc": "퇴근길/하교길 지친 어깨를 들썩이게 만드는 기분 좋은 리듬!"},
        "🌙 조용한 심야 (22시~06시)": {"kpop": "DEAN - instagram 📱", "pop": "Honne - Day 1 🧸", "desc": "피곤한 하루 끝, 침대 속에서 뒹굴거리며 밤을 위로받기 딱 좋은 선곡."}
    },
    "심장이 몽글몽글, 설레고 행복해 🥰🌸": {
        "🌅 상쾌한 아침 (06시~11시)": {"kpop": "NewJeans - Attention 🩵", "pop": "Taylor Swift - Cruel Summer ☀️", "desc": "아침 햇살마저 나를 축하해 주는 것 같은 싱그러운 설렘!"},
        "☀️ 나른한 한낮 (11시~17시)": {"kpop": "경서 - 나의 X에게 💌", "pop": "Bruno Mars - Just The Way You Are 🎸", "desc": "달콤한 에이드 한 잔 마시면서 들으면 콧노래가 절로 나와요."},
        "🌆 노을 지는 저녁 (17시~22시)": {"kpop": "폴킴 - 모든 날, 모든 순간 ✨", "pop": "Lauv - I Like Me Better 🧡", "desc": "주황빛 노을을 바라보며 로맨틱한 감성에 푹 빠져볼 시간!"},
        "🌙 조용한 심야 (22시~06시)": {"kpop": "볼빨간사춘기 - 우주를 줄게 🌌", "pop": "Troye Sivan - Strawberries & Cigarettes 🍓", "desc": "이불 속에서 들으면 밤하늘에 별이 쏟아지는 듯한 기분이에요."}
    },
    "텐션 업! 에너지가 넘쳐흘러 🥳🚀": {
        "🌅 상쾌한 아침 (06시~11시)": {"kpop": "트와이스 - Cheer Up 📣", "pop": "Pharrell Williams - Happy 💛", "desc": "오늘 하루를 완전히 내 것으로 만들 수 있을 것 같은 자신감 뿜뿜!"},
        "☀️ 나른한 한낮 (11시~17시)": {"kpop": "에스파 (aespa) - Supernova 💥", "pop": "Dua Lipa - Dance The Night 🪩", "desc": "우주 끝까지 날아갈 것 같은 강력한 비트로 지구 정복 완료!"},
        "🌆 노을 지는 저녁 (17시~22시)": {"kpop": "싸이 - 연예인 🎤", "pop": "The Weeknd - Can't Feel My Face ⚡", "desc": "지치지 않는 열정! 파티는 이제부터 시작이라구욧!"},
        "🌙 조용한 심야 (22시~06시)": {"kpop": "빅뱅 - 뱅뱅뱅 🔫", "pop": "Pitbull - Timber 🌲", "desc": "잠들기 아쉬운 이 밤, 내 방을 클럽으로 만들어 줄 하이텐션 음악!"}
    },
    "혼자 있고 싶어... 센치하고 차분해 ☕📜": {
        "🌅 상쾌한 아침 (06시~11시)": {"kpop": "AKMU - 어떻게 이별까지 사랑하겠어 💔", "pop": "Billie Eilish - What Was I Made For? 🎀", "desc": "차분한 아침 안개 속에서 내 마음을 고요하게 들여다봐요."},
        "☀️ 나른한 한낮 (11시~17시)": {"kpop": "방탄소년단 (BTS) - 봄날 🌸", "pop": "Adele - Easy On Me 🌊", "desc": "따뜻한 차 한 잔과 함께 가사 하나하나를 음미하기 좋아요."},
        "🌆 노을 지는 저녁 (17시~22시)": {"kpop": "잔나비 - 주저하는 연인들을 위해 🎸", "pop": "Conan Gray - Heather 🍂", "desc": "스쳐 지나가는 바람마저 영화 속 한 장면처럼 만들어 주는 감성."},
        "🌙 조용한 심야 (22시~06시)": {"kpop": "우원재 - 시차 ⏰", "pop": "Cigarettes After Sex - Apocalypse 🌌", "desc": "어두운 방 안, 스탠드 불빛 하나 켜두고 깊은 생각에 잠길 때."}
    },
    "우울하고 속상해, 토닥토닥이 필요해 🥺🩹": {
        "🌅 상쾌한 아침 (06시~11시)": {"kpop": "아이유 - Love wins all 🤍", "pop": "Coldplay - Fix You 🩹", "desc": "상처받은 아침, 당신을 따뜻하게 안아줄 첫 번째 위로."},
        "☀️ 나른한 한낮 (11시~17시)": {"kpop": "태연 - Stay 🌟", "pop": "Olivia Rodrigo - making the bed 🛏️", "desc": "울어도 괜찮아요. 음악이 조용히 곁을 지켜줄게요."},
        "🌆 노을 지는 저녁 (17시~22시)": {"kpop": "이하이 - 한숨 🌬️", "desc": "숨이 턱 끝까지 차오를 때, 당신의 한숨을 대신 쉬어줄게요."}, "pop": "Lewis Capaldi - Someone You Loved 💔", "desc": "마음껏 감정을 쏟아내고 나면 한결 편안해질 거예요."
    },
    "화가 난다 화가 나! 심술이 퉁퉁 😡🔥": {
        "🌅 상쾌한 아침 (06시~11시)": {"kpop": "블랙핑크 - Kill This Love 💔", "pop": "Olivia Rodrigo - bad idea right? 🤔", "desc": "아침부터 꼬인 기분을 강렬한 비트로 다 부숴버려요!"},
        "☀️ 나른한 한낮 (11시~17시)": {"kpop": "지코 (ZICO) - Any Song 🎵", "pop": "Taylor Swift - Shake It Off 💃", "desc": "짜증 나는 일들은 그냥 훌훌 털어버리고 리듬을 타봐요!"},
        "🌆 노을 지는 저녁 (17시~22시)": {"kpop": "스트레이 키즈 - 락 (樂) ⚡", "pop": "Eminem - Lose Yourself 🎤", "desc": "분노를 랩과 강렬한 락 사운드로 승화시켜 스트레스 타파!"},
        "🌙 조용한 심야 (22시~06시)": {"kpop": "레드벨벳 - Psycho 🖤", "pop": "Billie Eilish - bad guy 😎", "desc": "조금은 도도하고 삐딱하게, 밤의 다크한 매력으로 기분 전환!"}
    }
}

# 4. 헤더 타이틀 영역 🎀
st.markdown('<div class="main-title">🦄 요정의 커스텀 주크박스 🦄</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">지금 내 맘에 쏙 드는 감정과 완벽한 시간대를 골라봐요! 🔮✨</div>', unsafe_allow_html=True)

st.divider()

# 5. 사용자 입력 (세분화 버전) 💭
st.subheader("🎪 오늘의 조각 맞추기")

col1, col2 = st.columns(2)

with col1:
    selected_mood = st.selectbox(
        "🔮 지금 내 마음 속 기분은?",
        list(music_db.keys())
    )

with col2:
    selected_time = st.selectbox(
        "⏰ 지금 창밖의 시간대는?",
        ["🌅 상쾌한 아침 (06시~11시)", "☀️ 나른한 한낮 (11시~17시)", "🌆 노을 지는 저녁 (17시~22시)", "🌙 조용한 심야 (22시~06시)"]
    )

st.write("")

# 6. 매칭 결과 출력 🎁
if st.button("💝 요정아, 내 분위기에 맞는 노래를 줘! 💝", use_container_width=True):
    st.balloons() # 상큼한 풍선 날리기 🎈
    st.snow()     # 반짝이는 눈꽃 효과까지 추가! ❄️
    
    song_info = music_db[selected_mood][selected_time]
    
    st.success("✨ 뾰로롱! 오늘 이 시간에 딱 어울리는 마법 소환 완료!")
    st.write("")
    
    # 예쁜 커스텀 박스로 추천 카드 만들기
    st.markdown(f"""
        <div class="music-box">
            <h3 style="color: #4A4A4A; margin-bottom: 20px;">🎒 당신을 위한 맞춤 처방전</h3>
            <div style="margin-bottom: 20px;">
                <span class="song-tag">🇰🇷 K-POP</span> 
                <p style="font-size: 1.3rem; font-weight: bold; margin-top: 5px; color: #333;">{song_info['kpop']}</p>
            </div>
            <hr style="border: 0; border-top: 1px dashed #FFD166; margin: 15px 0;">
            <div style="margin-bottom: 20px;">
                <span class="song-tag" style="background-color: #C1E1C1; color: #3F704D;">🇺🇸 POP</span> 
                <p style="font-size: 1.3rem; font-weight: bold; margin-top: 5px; color: #333;">{song_info['pop']}</p>
            </div>
            <p style="font-size: 0.95rem; color: #666; font-style: italic; background-color: #FFF; padding: 10px; border-radius: 10px; margin-top: 15px;">
                💬 "{song_info['desc']}"
            </p>
        </div>
    """, unsafe_allow_html=True)

# 7. 귀여운 푸터 🧸
st.divider()
st.caption("🦄 매일 달라지는 기분도 모두 소중한 당신의 조각이에요. 노래와 함께 오늘도 예쁜 시간 보내기 약속! 🤙💕")
