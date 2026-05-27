import streamlit as st

# ==========================================
# 1. 페이지 기본 설정 및 디자인 (Cute 테마)
# ==========================================
st.set_page_config(
    page_title="나의 MBTI 뮤지컬 메이트 🎭",
    page_icon="🎵",
    layout="centered"
)

# 귀여운 커스텀 스타일 적용 (CSS)
st.markdown("""
    <style>
    .main {
        background-color: #FFF9F2;
    }
    h1 {
        color: #FF6B6B;
        text-align: center;
        font-family: 'GmarketSansMedium', sans-serif;
    }
    .subtitle {
        text-align: center;
        color: #4A4A4A;
        font-size: 1.2rem;
        margin-bottom: 2rem;
    }
    .result-card {
        background-color: #FFFFFF;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.05);
        border-left: 5px solid #FF6B6B;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 2. MBTI별 뮤지컬 추천 데이터베이스 (DB)
# ==========================================
# 각 MBTI에 어울리는 대표 이미지(Unsplash 무료 고화질)와 설명 설정
musical_data = {
    "ISTJ": {
        "title": "레미제라블 (Les Misérables) 👮‍♂️📖",
        "desc": "원칙과 책임감을 중요시하는 ISTJ! 법과 신념을 지키려는 자베르 경감과 정의를 위해 묵묵히 헌신하는 장발장의 묵직한 서사시가 당신의 마음을 울릴 거예요.",
        "image": "https://www.google.com/imgres?q=%EB%A0%88%EB%AF%B8%EC%A0%9C%EB%9D%BC%EB%B8%94&imgurl=https%3A%2F%2Fticketimage.interpark.com%2FPlay%2Fimage%2Flarge%2F23%2F23012526_p.gif&imgrefurl=https%3A%2F%2Ftickets.interpark.com%2Fgoods%2F23012526&docid=P6wwd5Mj0utPEM&tbnid=QoiVvulOj1awLM&vet=12ahUKEwjl99eb1NiUAxUfVusIHboYFjgQnPAOegQIFhAB..i&w=300&h=400&hcb=2&ved=2ahUKEwjl99eb1NiUAxUfVusIHboYFjgQnPAOegQIFhAB", # 혁명/깃발 느낌
        "song": "🎶 추천 넘버: <One Day More>, <Who Am I?>"
    },
    "ISFJ": {
        "title": "레베카 (Rebecca) 🏰💙",
        "desc": "차분하고 헌신적인 ISFJ! 진심 어린 사랑으로 어두운 저택의 비밀을 극복해 나가는 '나(I)'의 따뜻하고도 강인한 모습에 깊이 공감하게 될 것입니다.",
        "image": "https://www.google.com/imgres?q=%EB%A0%88%EB%B2%A0%EC%B9%B4&imgurl=https%3A%2F%2Fticketimage.interpark.com%2FPlay%2Fimage%2Flarge%2F23%2F23008837_p.gif&imgrefurl=https%3A%2F%2Ftickets.interpark.com%2Fgoods%2F23008837&docid=6wcwW3yIlCwy-M&tbnid=H68zAU6AhCnnBM&vet=12ahUKEwip382_1NiUAxU7YOsIHXVQFzQQnPAOegQIExAB..i&w=300&h=400&hcb=2&ved=2ahUKEwip382_1NiUAxU7YOsIHXVQFzQQnPAOegQIExAB", # 고풍스러운 저택/성 느낌
        "song": "🎶 추천 넘버: <Rebecca>, <신이여>"
    },
    "INFJ": {
        "title": "하데스타운 (Hadestown) 🌿🎻",
        "desc": "깊은 통찰력과 이상향을 꿈꾸는 INFJ! 신화적 세계관 속에서 사랑과 희망을 끝까지 노래하는 오르페우스의 순수한 영혼이 큰 감동을 선사할 거예요.",
        "image": "https://namu.wiki/w/%ED%95%98%EB%8D%B0%EC%8A%A4%ED%83%80%EC%9A%B4", # 재즈/오르페우스의 하프 느낌
        "song": "🎶 추천 넘버: <Wait for Me>, <Epic III>"
    },
    "INTJ": {
        "title": "데스노트 (Death Note) 📓🍎",
        "desc": "치밀한 전략과 지적 대결을 즐기는 INTJ! 세상을 바꾸려는 천재 야가미 라이토와 베일에 싸인 탐정 엘(L)의 불꽃 튀는 두뇌 게임에 온전히 빠져들게 될 것입니다.",
        "image": "https://tickets.interpark.com/goods/26002593", # 미스터리한 사과/어두운 톤
        "song": "🎶 추천 넘버: <죽음의 게임>, <놈의 마음 속으로>"
    },
    "ISTP": {
        "title": "지킬 앤 하이드 (Jekyll & Hyde) 🧪⚡",
        "desc": "냉철한 이성과 강한 호기심을 지닌 ISTP! 인간의 선과 악을 분리하려는 대담한 실험과, 통제할 수 없는 하이드와의 위험한 줄타기가 당신의 심장을 뛰게 만듭니다.",
        "image": "https://www.google.com/imgres?q=%EC%A7%80%ED%82%AC%EC%95%A4%ED%95%98%EC%9D%B4%EB%93%9C%20%ED%8F%AC%EC%8A%A4%ED%84%B0&imgurl=http%3A%2F%2Fimage.yes24.com%2Fimages%2Fchyes24%2Ffroala%2F0%2F46156%2F44120.jpg&imgrefurl=https%3A%2F%2Fch.yes24.com%2Farticle%2Fdetails%2F46156&docid=qt3XURSx4GKIXM&tbnid=s2THsLqa3fMSvM&vet=12ahUKEwjsp_v-1NiUAxXbYOsIHeppBjMQnPAOegQIGBAB..i&w=1000&h=1000&hcb=2&ved=2ahUKEwjsp_v-1NiUAxXbYOsIHeppBjMQnPAOegQIGBAB", # 과학 실험실 느낌
        "song": "🎶 추천 넘버: <지금 이 순간 (This is the Moment)>, <얼라이브 (Alive)>"
    },
    "ISFP": {
        "title": "캣츠 (Cats) 🐾🌙",
        "desc": "예술적 감수성이 풍부하고 자유를 사랑하는 ISFP! 개성 넘치는 고양이들의 아름다운 몸짓과 밤하늘에 울려 퍼지는 감성적인 음악에 마음이 스르륵 녹아내릴 거예요.",
        "image": "https://economist.co.kr/article/view/ecn202211150128", # 밤하늘과 고양이
        "song": "🎶 추천 넘버: <Memory>"
    },
    "INFP": {
        "title": "오페라의 유령 (The Phantom of the Opera) 🌹🎭",
        "desc": "몽환적인 로맨스와 마음속 깊은 감정을 간직한 INFP! 지하 미궁에 사는 유령의 슬픈 사랑 이야기와 웅장한 가면무도회의 세계관이 당신의 상상력을 마구 자극합니다.",
        "image": "https://hafsres.wordpress.com/2014/02/18/%EC%9C%A0%EB%A0%B9%EC%97%90%EA%B2%8C-%ED%99%80%EB%A6%AC%EB%8B%A4-%EB%AE%A4%EC%A7%80%EC%BB%AC/", # 붉은 장미와 오페라 가면 느낌
        "song": "🎶 추천 넘버: <The Phantom of the Opera>, <Think of Me>"
    },
    "INTP": {
        "title": "프랑켄슈타인 (Frankenstein) 🧠🔬",
        "desc": "끝없는 지적 호기심과 본질을 탐구하는 INTP! 신의 영역에 도전하는 과학자 빅터와 생명의 창조, 그리고 그 속의 철학적 질문들이 당신에게 깊은 생각의 거리를 던져줄 거예요.",
        "image": "https://mobileticket.interpark.com/goods/21008252", # 어둡고 지적인 아카데미 서재
        "song": "🎶 추천 넘버: <단 하나의 미래>, <너의 꿈 속에서>"
    },
    "ESTP": {
        "title": "시카고 (Chicago) 🎷👠",
        "desc": "매 순간 자극과 즐거움을 쫓는 트렌디한 ESTP! 화려한 재즈 선율, 유쾌하고도 풍자적인 무대, 그리고 당당한 주인공들의 씬스틸러 매력에 200% 매료될 거예요!",
        "image": "https://www.daeguoperahouse.org/eng/contents/01_performance/page.html?mid=177182295&mode=view&no=2011", # 재즈와 트럼펫/무대 느낌
        "song": "🎶 추천 넘버: <All That Jazz>, <Cell Block Tango>"
    },
    "ESFP": {
        "title": "맘마미아! (Mamma Mia!) 💃☀️",
        "desc": "인생 자체가 축제이자 즐거움인 분위기 메이커 ESFP! 그리스의 푸른 바다를 배경으로 펼쳐지는 신나는 아바(ABBA)의 명곡들과 흥겨운 댄스 타임에 몸이 저절로 들썩일걸요?",
        "image": "https://www.themusical.co.kr/Musical/Detail?num=3115", # 밝은 햇살과 그리스 바다 해변
        "song": "🎶 추천 넘버: <Dancing Queen>, <Mamma Mia>"
    },
    "ENFP": {
        "title": "위키드 (Wicked) 🧹💚",
        "desc": "언제나 독창적인 아이디어와 모험심이 넘치는 ENFP! 세상의 편견에 맞서 초록색 피부의 마녀 엘파바가 빗자루를 타고 하늘로 날아오르는 순간, 온몸에 소름이 돋을 거예요!",
        "image": "https://m.blog.naver.com/safari17/60214339191", # 신비로운 초록빛 마법 느낌
        "song": "🎶 추천 넘버: <Defying Gravity>, <Popular>"
    },
    "ENTP": {
        "title": "모차르트! (Mozart!) 🎹👑",
        "desc": "기존의 틀을 깨는 천재이자 자유로운 영혼 ENTP! 클래식의 상식을 뒤흔들며 자신만의 음악 세계를 펼쳤던 록스타 같은 모차르트의 뜨거운 삶에 완전히 동화될 것입니다.",
        "image": "https://www.themusical.co.kr/Musical/Detail?num=3164", # 피아노 건반과 열정
        "song": "🎶 추천 넘버: <내 운명 피하고 싶어>, <황금별>"
    },
    "ESTJ": {
        "title": "영웅 (Hero) 🇰🇷🚂",
        "desc": "목표를 향해 단호하게 나아가는 리더 ESTJ! 조국의 독립이라는 대의를 위해 결연하게 한걸음씩 걸어 나갔던 안중근 의사의 곧고 강인한 기백이 당신의 심장을 울립니다.",
        "image": "https://m.lgart.com/product/performance/252732", # 철도와 묵직한 시대적 배경
        "song": "🎶 추천 넘버: <누가 죄인인가>, <장부가>"
    },
    "ESFJ": {
        "title": "헤어스프레이 (Hairspray) 💇‍♀️🌈",
        "desc": "주변 사람들을 챙기고 화합을 사랑하는 다정한 ESFJ! 편견을 깨부수고 모두가 하나 되어 춤추고 노래하는 유쾌하고 사랑스러운 에너지가 당신에게 완벽한 행복을 줄 거예요.",
        "image": "https://namu.wiki/w/%ED%97%A4%EC%96%B4%EC%8A%A4%ED%94%84%EB%A0%88%EC%9D%B4%28%EB%AE%A4%EC%A7%80%EC%BB%AC%29", # 신나는 파티와 화합의 에너지
        "song": "🎶 추천 넘버: <You Can't Stop the Beat>"
    },
    "ENFJ": {
        "title": "렌트 (Rent) 🎸❤️",
        "desc": "세상을 더 따뜻하게 만들고 싶은 로맨티시스트 ENFJ! 가난하지만 예술과 사랑으로 서로의 상처를 보듬으며 살아가는 청춘들의 외침이 당신의 마음에 큰 감동을 줄 거예요.",
        "image": "https://tickets.interpark.com/play/performance/%EB%AE%A4%EC%A7%80%EC%BB%AC-%EB%A0%8C%ED%8A%B8-gA7gaFCmiIHseRsg", # 록 콘서트의 열기 가득한 조명
        "song": "🎶 추천 넘버: <Seasons of Love>"
    },
    "ENTJ": {
        "title": "몬테크리스토 (Monte Cristo) ⚔️🏰",
        "desc": "철저한 계획과 강력한 카리스마를 가진 ENTJ! 배신으로 무너진 삶을 극복하고 치밀한 전략으로 정의를 되찾는 몬테크리스토 백작의 통쾌한 복수극이 최고의 카타르시스를 줍니다.",
        "image": "https://namu.wiki/w/%EB%AA%AC%ED%85%8C%ED%81%AC%EB%A6%AC%EC%8A%A4%ED%86%A0%28%EB%AE%A4%EC%A7%80%EC%BB%AC%29", # 거친 파도와 복수의 여정
        "song": "🎶 추천 넘버: <너희에게 선사하는 지옥>, <언제나 그대 곁에>"
    }
}

# ==========================================
# 3. UI 구성 요소 (헤더 및 선택 영역)
# ==========================================
st.title("🎵 나의 MBTI 뮤지컬 메이트 ✨")
st.markdown("<p class='subtitle'>MBTI를 선택하면 딱! 어울리는 명작 뮤지컬을 추천해드려요 🧸</p>", unsafe_allow_html=True)

st.write("---")

# 4개 성향 그룹별로 귀여운 라디오 버튼 배치
st.subheader("💡 나의 MBTI 성향 조합하기")

col1, col2, col3, col4 = st.columns(4)

with col1:
    energy = st.radio("에너지 방향", ["E (외향형)", "I (내향형)"])
with col2:
    info = st.radio("정보 인식", ["S (감각형)", "N (직관형)"])
with col3:
    decision = st.radio("의사 결정", ["T (사고형)", "F (감정형)"])
with col4:
    life = st.radio("생활 양식", ["J (판단형)", "P (인식형)"])

# 선택된 성향 문자열 합치기 (예: "E" + "N" + "F" + "P" = "ENFP")
user_mbti = energy[0] + info[0] + decision[0] + life[0]

st.write("---")

# ==========================================
# 4. 결과 출력 및 효과 발생
# ==========================================
if st.button("🎭 나만의 뮤지컬 추천받기!", use_container_width=True):
    # 신나는 파티풍 풍선 날리기 효과 🎈
    st.balloons()
    
    # 추천 데이터 가져오기
    recommended = musical_data[user_mbti]
    
    # 결과 보여주기
    st.markdown(f"### 🎉 당신의 MBTI [**{user_mbti}**]에 꼭 맞는 뮤지컬은?")
    
    # 카드 레이아웃 안에 결과 예쁘게 배치
    with st.container():
        st.markdown(f"""
        <div class="result-card">
            <h2 style="color: #FF6B6B; margin-top: 0;">{recommended['title']}</h2>
            <p style="font-size: 1.1rem; line-height: 1.6; color: #333333;">{recommended['desc']}</p>
            <strong style="color: #FF6B6B; font-size: 1.05rem;">{recommended['song']}</strong>
        </div>
        """, unsafe_allow_html=True)
        
        st.write("") # 간격 띄우기
        
        # 뮤지컬 컨셉 이미지 출력
        st.image(recommended['image'], caption=f"뮤지컬 {recommended['title']} 테마 이미지", use_container_width=True)

st.write("")
st.write("---")
st.caption("당곡고등학교 학생들의 즐거운 파이썬 학습을 응원합니다! 🏫💫")
