import streamlit as st

# 1. 페이지 기본 설정 🎒
st.set_page_config(
    page_title="나만의 감성 라디오 📻",
    page_icon="🌈",
    layout="centered"
)

# 2. 한층 더 업그레이드된 러블리 큐티 CSS 🎀
st.markdown("""
    <style>
    .main-title {
        font-size: 2.8rem !important;
        color: #FF758C;
        text-align: center;
        font-weight: bold;
        margin-bottom: 5px;
        text-shadow: 2px 2px 4px rgba(255,117,140,0.2);
    }
    .sub-title {
        font-size: 1.05rem !important;
        color: #8E7C93;
        text-align: center;
        margin-bottom: 30px;
    }
    .music-card-container {
        background: linear-gradient(135deg, #FFF5F5 0%, #F5F0FF 100%);
        padding: 25px;
        border-radius: 25px;
        border: 3px dotted #FFB7B2;
        box-shadow: 0px 8px 20px rgba(255, 183, 178, 0.2);
    }
    .song-title-text {
        font-size: 1.25rem;
        font-weight: bold;
        color: #4A4A4A;
        margin-top: 8px;
    }
    .badge-kpop {
        background-color: #FFD1DC;
        color: #FF477E;
        padding: 4px 12px;
        border-radius: 50px;
        font-size: 0.8rem;
        font-weight: bold;
    }
    .badge-pop {
        background-color: #D6EADF;
        color: #2D6A4F;
        padding: 4px 12px;
        border-radius: 50px;
        font-size: 0.8rem;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# 3. 8가지 기분 x 6가지 시간대 = 총 48개 조합의 촘촘한 데이터베이스! 🎼
# 구조: music_db[기분][시간] = {"kpop": "...", "pop": "...", "desc": "..."}
music_db = {
    "몽글몽글 연애 세포 살아나는 설렘 💕": {
        "💤 이른 새벽 (00:00~05:00)": {"kpop": "볼빨간사춘기 - 우주를 줄게 🌌", "pop": "Troye Sivan - Strawberries & Cigarettes 🍓", "desc": "밤하늘 아래 온 세상이 핑크빛으로 반짝이는 새벽 비행 감성."},
        "🌅 아침 창가 (05:00~09:00)": {"kpop": "NewJeans - Attention 🩵", "pop": "Taylor Swift - Cruel Summer ☀️", "desc": "아침 햇살을 받으며 등교/출근할 때 기분 좋은 발걸음!"},
        "☀️ 활기찬 오전 (09:00~12:00)": {"kpop": "아이유 - 내 손을 잡아 🤝", "pop": "Carly Rae Jepsen - Call Me Maybe 📞", "desc": "심장이 두근두근, 고백하기 직전의 짜릿한 활력 충전!"},
        "🍰 나른한 오후 (12:00~17:00)": {"kpop": "경서 - 나의 X에게 💌", "pop": "Bruno Mars - Just The Way You Are 🎸", "desc": "달콤한 디저트와 함께 즐기는 간지러운 오후의 로맨스."},
        "🌆 노을녘 퇴근길 (17:00~21:00)": {"kpop": "폴킴 - 너를 만나 ☕", "pop": "Lauv - I Like Me Better 🧡", "desc": "주황빛으로 물드는 가로등 밑, 손잡고 걷고 싶어지는 멜로디."},
        "🌃 깊어가는 밤 (21:00~24:00)": {"kpop": "백현 - UN Village 🏡", "pop": "Pink Sweat$ - At My Worst 🌸", "desc": "은은한 조명 아래서 오늘 하루 속삭였던 달콤한 대화들."}
    },
    "텐션 폭발! 온 세상이 다 내 거 같아 🥳": {
        "💤 이른 새벽 (00:00~05:00)": {"kpop": "빅뱅 - 뱅뱅뱅 🔫", "pop": "Pitbull - Timber 🌲", "desc": "잠들 수 없는 열정! 내 방을 클럽으로 만드는 미드나잇 파티."},
        "🌅 아침 창가 (05:00~09:00)": {"kpop": "부석순 - 파이팅 해야지 🔥", "pop": "Pharrell Williams - Happy 💛", "desc": "눈 뜨자마자 에너지 풀 충전! 오늘 하루 다 비켜라!"},
        "☀️ 활기찬 오전 (09:00~12:00)": {"kpop": "트와이스 - Cheer Up 📣", "pop": "One Direction - What Makes You Beautiful 🎸", "desc": "비타민 음료보다 더 상큼하게 오전의 능률을 올려봐요!"},
        "🍰 나른한 오후 (12:00~17:00)": {"kpop": "에스파 - Supernova 💥", "pop": "Sabrina Carpenter - Espresso ☕", "desc": "식곤증이 몰려올 때 머리를 쨍하게 울리는 하이텐션 팝과 케이팝!"},
        "🌆 노을녘 퇴근길 (17:00~21:00)": {"kpop": "싸이 - 연예인 🎤", "pop": "Dua Lipa - Dance The Night 🪩", "desc": "오늘 하루 수고한 나를 위해 퇴근길 비트를 신나게 up!"},
        "🌃 깊어가는 밤 (21:00~24:00)": {"kpop": "방탄소년단 - Dynamite 🧨", "pop": "The Weeknd - Blinding Lights ⚡", "desc": "화려한 도시 불빛 사이를 시원하게 질러가는 듯한 해방감."}
    },
    "영혼 가출... 좀비 모드, 피곤해 죽겠어 😴": {
        "💤 이른 새벽 (00:00~05:00)": {"kpop": "DEAN - instagram 📱", "pop": "Honne - Day 1 🧸", "desc": "피곤한데 잠은 안 오고... 멍하니 폰 보며 침대 뒹굴거릴 때."},
        "🌅 아침 창가 (05:00~09:00)": {"kpop": "NCT DREAM - Smoothie 🥤", "pop": "Justin Bieber - Beauty And A Beat 🥁", "desc": "안 떠지는 눈을 비틀어 번쩍 뜨게 해 줄 억지 텐션 끌어올리기!"},
        "☀️ 활기찬 오전 (09:00~12:00)": {"kpop": "청하 - 벌써 12시 ⏰", "pop": "The Kid LAROI, Justin Bieber - STAY 🏃", "desc": "시간아 달려라! 무거운 몸을 이끌고 버티는 오전 메이트."},
        "🍰 나른한 오후 (12:00~17:00)": {"kpop": "지코 - 아무노래 🎵", "pop": "Harry Styles - Watermelon Sugar 🍉", "desc": "뇌를 비우고 그냥 흘러가는 리듬에 몸을 맡기고 싶을 때."},
        "🌆 노을녘 퇴근길 (17:00~21:00)": {"kpop": "이영지 - Small Girl 🍯", "pop": "Post Malone - Sunflower 🌻", "desc": "지친 발걸음에 부드러운 쿠션을 깔아주는 포근한 리듬감."},
        "🌃 깊어가는 밤 (21:00~24:00)": {"kpop": "크러쉬 - 잊어버리지마 ❄️", "pop": "Lauv - Paris in the Rain 🌧️", "desc": "고생했어, 이제 따뜻한 물로 샤워하고 이불 속으로 쏙 들어갈 시간."}
    },
    "차분하고 고요해, 나만의 시간에 집중 ☕": {
        "💤 이른 새벽 (00:00~05:00)": {"kpop": "우원재 - 시차 ⏰", "pop": "Cigarettes After Sex - Apocalypse 🌌", "desc": "모두가 잠든 시간, 홀로 깨어 사색을 즐길 때 최고의 분위기."},
        "🌅 아침 창가 (05:00~09:00)": {"kpop": "악뮤 - 어떻게 이별까지 사랑하겠어 💔", "pop": "Billie Eilish - What Was I Made For? 🎀", "desc": "차분한 아침 안개처럼 차분하게 가라앉은 감성을 음미해요."},
        "☀️ 활기찬 오전 (09:00~12:00)": {"kpop": "선우정아 - 도망가자 🏃‍♀️", "pop": "Bruno Major - Nothing ☕", "desc": "할 일에 온전히 집중할 수 있도록 차분한 배경이 되어줍니다."},
        "🍰 나른한 오후 (12:00~17:00)": {"kpop": "방탄소년단 - 봄날 🌸", "pop": "Adele - Easy On Me 🌊", "desc": "커피 한 잔 홀짝이며 조용히 창밖을 바라보는 평온함."},
        "🌆 노을녘 퇴근길 (17:00~21:00)": {"kpop": "잔나비 - 주저하는 연인들을 위해 🎸", "pop": "Conan Gray - Heather 🍂", "desc": "빌딩 숲 사이로 사라지는 노을을 보며 센치해지는 타이밍."},
        "🌃 깊어가는 밤 (21:00~24:00)": {"kpop": "성시경 - 거리에서 🌧️", "pop": "Charlie Puth - Dangerously ⚡", "desc": "하루의 끝을 차분한 감성 음악으로 촉촉하게 마감해보세요."}
    },
    "눈물이 핑... 마음의 위로가 필요한 날 🥺": {
        "💤 이른 새벽 (00:00~05:00)": {"kpop": "이하이 - 한숨 🌬️", "pop": "Lady Gaga - Always Remember Us This Way 🌹", "desc": "베개를 적시는 눈물을 말없이 닦아주는 따스한 목소리."},
        "🌅 아침 창가 (05:00~09:00)": {"kpop": "아이유 - Love wins all 🤍", "pop": "Coldplay - Fix You 🩹", "desc": "상처받은 마음에 새 아침의 햇살 같은 온기를 주는 서사."},
        "☀️ 활기찬 오전 (09:00~12:00)": {"kpop": "레드벨벳 - Daylight ☀️", "pop": "Keane - Everybody's Changing 🍂", "desc": "세상이 낯설게 느껴질 때 고개를 끄덕여주는 다정한 멜로디."},
        "🍰 나른한 오후 (12:00~17:00)": {"kpop": "태연 - Stay 🌟", "pop": "Olivia Rodrigo - making the bed 🛏️", "desc": "서럽고 외로운 마음을 둥둥 떠다니는 리듬이 가만히 안아줄게요."},
        "🌆 노을녘 퇴근길 (17:00~21:00)": {"kpop": "종현 - 하루의 끝 🌅", "pop": "Lewis Capaldi - Someone You Loved 💔", "desc": "오늘 참 서러웠지? 수고했어라는 말을 대신 전하는 음악."},
        "🌃 깊어가는 밤 (21:00~24:00)": {"kpop": "박효신 - 야생화 🌼", "pop": "Sam Smith - Stay With Me 🕯️", "desc": "깊은 어둠 속에서 가만히 위로의 촛불을 켜주는 명곡."}
    },
    "심술 퉁퉁! 짜증나고 화가 잔뜩 나 😡": {
        "💤 이른 새벽 (00:00~05:00)": {"kpop": "레드벨벳 - Psycho 🖤", "pop": "Billie Eilish - bad guy 😎", "desc": "잠 안 오는 밤, 빌런처럼 힙하고 시크하게 분노 표출하기!"},
        "🌅 아침 창가 (05:00~09:00)": {"kpop": "블랙핑크 - Kill This Love 💔", "pop": "Olivia Rodrigo - bad idea right? 🤔", "desc": "아침부터 꼬인 기분을 센 비트로 한 방에 부숴버려요."},
        "☀️ 활기찬 오전 (09:00~12:00)": {"kpop": "있지 (ITZY) - WANNABE 👑", "pop": "Taylor Swift - Shake It Off 💃", "desc": "누가 뭐래도 난 내 길 가련다! 짜증을 자신감으로 승화!"},
        "🍰 나른한 오후 (12:00~17:00)": {"kpop": "지코 - Freak 🤪", "pop": "Avril Lavigne - Sk8er Boi 🎸", "desc": "답답한 가슴을 뻥 뚫어주는 일렉기타 사운드 락앤롤!"},
        "🌆 노을녘 퇴근길 (17:00~21:00)": {"kpop": "스트레이 키즈 - 락 (樂) ⚡", "pop": "Eminem - Lose Yourself 🎤", "desc": "퇴근길 빌런들을 생각하며 속사포 랩과 비트로 스트레스 파괴!"},
        "🌃 깊어가는 밤 (21:00~24:00)": {"kpop": "f(x) - 4 Walls 🪩", "pop": "Doja Cat - Paint The Town Red 🩸", "desc": "도도하고 시크하게, 묵직한 베이스로 낮의 분노를 날려버려요."}
    },
    "아무 생각 없음... 완전 멍 때리는 중 😶": {
        "💤 이른 새벽 (00:00~05:00)": {"kpop": "죠지 - Boat 🚣", "pop": "Mac DeMarco - Chamber Of Reflection 🌀", "desc": "우주 속을 둥둥 표류하는 듯 아득하고 편안한 미니멀 사운드."},
        "🌅 아침 창가 (05:00~09:00)": {"kpop": "릴러말즈 - 비와서 그래 🌧️", "pop": "Jeremy Zucker - comethru 🏡", "desc": "머릿속 환기용! 잔잔하게 스며드는 아침 무드."},
        "☀️ 활기찬 오전 (09:00~12:00)": {"kpop": "10cm - 봄이 좋냐?? 🌸", "pop": "Jason Mraz - I'm Yours 🎸", "desc": "어쿠스틱 기타 소리에 정신줄을 놓고 가벼운 스텝을 밟아요."},
        "🍰 나른한 오후 (12:00~17:00)": {"kpop": "볼빨간사춘기 - 여행 ✈️", "pop": "Surfaces - Sunday Best ☀️", "desc": "구름 위를 걷는 듯 몽롱하고 평화로운 오후의 정취."},
        "🌆 노을녘 퇴근길 (17:00~21:00)": {"kpop": "카더가든 - 나무 🌱", "pop": "Men I Trust - Show Me How ☁️", "desc": "흐르는 강물이나 가로등을 보며 멍 때리기 최적화된 드림팝."},
        "🌃 깊어가는 밤 (21:00~24:00)": {"kpop": "잔나비 - 뜨거운 여름밤은 가고 🌌", "pop": "Cigarettes After Sex - Sweet 🍬", "desc": "귓가에 나직하게 울리는 악기 소리에 뇌를 완전히 맡기는 시간."}
    },
    "과거 여행 중... 왠지 아련하고 그리워 🍂": {
        "💤 이른 새벽 (00:00~05:00)": {"kpop": "아이유 - 이름에게 ✉️", "pop": "brent faiyaz - trust 🖤", "desc": "새벽에 꺼내보는 낡은 일기장 같은 먹먹한 울림."},
        "🌅 아침 창가 (05:00~09:00)": {"kpop": "토이 - 좋은 사람 ☕", "pop": "The Beatles - Yesterday 🎸", "desc": "기억 저편 옛 추억들이 아침 햇살과 함께 부드럽게 깨어나요."},
        "☀️ 활기찬 오전 (09:00~12:00)": {"kpop": "이문세 - 옛사랑 🍂", "pop": "Oasis - Don't Look Back In Anger 🇬🇧", "desc": "웅장한 밴드 사운드로 추억을 그리워하는 화창한 오전."},
        "🍰 나른한 오후 (12:00~17:00)": {"kpop": "폴킴 - 비 🌧️", "pop": "Christopher - Bad 🕶️", "desc": "문득 옛 친구나 지나간 사랑이 흐릿하게 생각나는 시간."},
        "🌆 노을녘 퇴근길 (17:00~21:00)": {"kpop": "태연 - 사계 (Four Seasons) 🍁", "pop": "Troye Sivan - Youth 🦋", "desc": "빛바랜 사진첩을 넘기는 듯 노을빛이 추억을 소환해요."},
        "🌃 깊어가는 밤 (21:00~24:00)": {"kpop": "하이키 - 건물 사이에 피어난 장미 🌹", "pop": "Lany - malibu nights 🌊", "desc": "그때의 나, 그때의 우리가 그리워 가슴 한구석이 아릿해지는 밤."}
    }
}

# 4. 헤더 타이틀 🎈
st.markdown('<div class="main-title">🔮 요정의 감성 주파수 라디오 📻</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">당신의 소중한 감정의 결표와 정확한 시간의 조각을 맞춰 최고의 하모니를 선물할게요! ✨🍭</div>', unsafe_allow_html=True)

st.divider()

# 5. 한층 세분화된 사용자 입력창 💭
st.subheader("🎪 감정 & 시간 팩토리 코디하기")

col1, col2 = st.columns(2)

with col1:
    selected_mood = st.selectbox(
        "🔮 지금 내 마음의 구름 모양은?",
        list(music_db.keys())
    )

with col2:
    selected_time = st.selectbox(
        "⏰ 지금 창밖의 정밀 타임라인!",
        ["💤 이른 새벽 (00:00~05:00)", "🌅 아침 창가 (05:00~09:00)", "☀️ 활기찬 오전 (09:00~12:00)", "🍰 나른한 오후 (12:00~17:00)", "🌆 노을녘 퇴근길 (17:00~21:00)", "🌃 깊어가는 밤 (21:00~24:00)"]
    )

st.write("")

# 6. 정밀 매칭 결과 출력 🎁
if st.button("🎵 우주에서 가장 어울리는 노래 소환하기 🎵", use_container_width=True):
    st.balloons()
    st.snow()
    
    song_info = music_db[selected_mood][selected_time]
    
    st.success("🎯 소환 성공! 오늘의 기분 맞춤형 비타민 처방전 도착 💌")
    st.write("")
    
    # 럭셔리 큐티 감성 박스로 결과 렌더링
    st.markdown(f"""
        <div class="music-card-container">
            <h3 style="color: #6C5B7B; text-align: center; margin-bottom: 25px; font-weight: bold;">🎒 [ {selected_time.split(' ')[1]} ] 의 음악 처방</h3>
            
            <div style="margin-bottom: 20px;">
                <span class="badge-kpop">🇰🇷 K-POP RECOMMEND</span>
                <p class="song-title-text">{song_info['kpop']}</p>
            </div>
            
            <div style="border-top: 2px dashed #E1D5FF; margin: 20px 0;"></div>
            
            <div style="margin-bottom: 20px;">
                <span class="badge-pop">🇺🇸 POP RECOMMEND</span>
                <p class="song-title-text">{song_info['pop']}</p>
            </div>
            
            <div style="background-color: #FFFFFF; padding: 12px 15px; border-radius: 12px; margin-top: 20px; border-left: 5px solid #FFB7B2;">
                <p style="font-size: 0.9rem; color: #777; line-height: 1.5; margin: 0; font-style: italic;">
                    💬 요정의 한마디: "{song_info['desc']}"
                </p>
            </div>
        </div>
    """, unsafe_allow_html=True)

# 7. 귀여운 푸터 🧸
st.divider()
st.caption("🌈 당신의 매 순간순간, 미세한 감정의 떨림까지 음악이 되어 빛날 거예요. 오늘도 특별한 하루 보내세요! 💖🐰")
requirements.txt
