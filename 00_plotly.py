import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime, timedelta

# 1. 페이지 설정 및 아기자기한 기본 디자인 🎒
st.set_page_config(
    page_title="글로벌 Top 10 주식 대시보드 📊",
    page_icon="🦄",
    layout="wide"
)

# 귀여운 감성 타이틀 스타일링 ✨
st.markdown("""
    <style>
    .main-title {
        font-size: 2.5rem !important;
        color: #FF6B81;
        text-align: center;
        font-weight: bold;
        margin-bottom: 5px;
    }
    .sub-title {
        font-size: 1.1rem !important;
        color: #747D8C;
        text-align: center;
        margin-bottom: 25px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🦄 요정의 글로벌 Top 10 주식 주크박스 📻</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">현재 기준 세계를 뒤흔드는 가장 가치 있는 기업 10곳의 1년간의 발자취를 추적해요! 🚀📈</div>', unsafe_allow_html=True)
st.divider()

# 2. 글로벌 시가총액 Top 10 기업 정보 (2026년 기준 딕셔너리 매핑) 🌍
top10_companies = {
    "NVIDIA (NVDA) 🟢": "NVDA",
    "Apple (AAPL) 🍎": "AAPL",
    "Alphabet / Google (GOOGL) 🔍": "GOOGL",
    "Microsoft (MSFT) 💻": "MSFT",
    "Amazon (AMZN) 📦": "AMZN",
    "TSMC (TSM) 💾": "TSM",
    "Broadcom (AVGO) 📡": "AVGO",
    "Saudi Aramco (2222.SR) 🛢️": "2222.SR",
    "Tesla (TSLA) ⚡": "TSLA",
    "Meta Platforms (META) 📸": "META"
}

# 3. 사이드바 구성 (기업 선택 & 옵션) 🛠️
st.sidebar.header("🎨 옵션을 골라주세요!")
selected_names = st.sidebar.multiselect(
    "📊 비교할 기업을 선택하세요 (여러 개 선택 가능):",
    list(top10_companies.keys()),
    default=list(top10_companies.keys())[:3] # 기본값으로 상위 3개 선택
)

plot_type = st.sidebar.radio(
    "📈 차트 보기 방식 종류:",
    ["실제 주가 (USD/개별통화) 💵", "1년 전 대비 수익률 (%) 📈"]
)

# 날짜 계산 (최근 1년)
end_date = datetime.today()
start_date = end_date - timedelta(days=365)

# 4. 데이터 로드 및 차트 시각화 부분 🔍
if not selected_names:
    st.warning("⚠️ 차트를 그리려면 기업을 최소 1개 이상 선택해 주세요! 🥺")
else:
    # 딕셔너리에서 티커 기호만 추출
    selected_tickers = [top10_companies[name] for name in selected_names]
    
    with st.spinner("🧙‍♂️ 요정이 야후 파이낸스에서 데이터를 열심히 져오고 있어요... 잠시만 기다려주세요! ✨"):
        try:
            # yfinance로 주가 데이터 한 번에 다운로드
            raw_data = yf.download(selected_tickers, start=start_date, end=end_date)['Close']
            
            # 단일 종목 선택 시 Series를 DataFrame 구조로 맞춰주기
            if len(selected_tickers) == 1:
                raw_data = pd.DataFrame(raw_data, columns=[selected_tickers[0]])
                
            # 결측치 보정 (주말/휴일 제외 처리)
            raw_data = raw_data.ffill()
            
            # Plotly 객체 생성 📊
            fig = go.Figure()
            
            for name in selected_names:
                ticker = top10_companies[name]
                if ticker in raw_data.columns:
                    y_values = raw_data[ticker]
                    
                    # '수익률 (%)' 방식일 경우 첫 번째 유효 주가 기준으로 변환
                    if "수익률" in plot_type:
                        first_valid_val = y_values.dropna().iloc[0]
                        y_values = ((y_values - first_valid_val) / first_valid_val) * 100
                    
                    fig.add_trace(go.Scatter(
                        x=raw_data.index,
                        y=y_values,
                        mode='lines',
                        name=name,
                        line=dict(width=2.5)
                    ))
            
            # 레이아웃 예쁘게 꾸미기
            y_axis_title = "주가 (Currency)" if "실제 주가" in plot_type else "수익률 (%)"
            fig.update_layout(
                title=f"📅 최근 1년간의 {plot_type} 추이",
                title_font=dict(size=18, color="#2F3542"),
                xaxis_title="날짜 (Date)",
                yaxis_title=y_axis_title,
                hovermode="x unified",
                template="plotly_white", # 깨끗하고 화사한 하얀색 테마
                legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
                margin=dict(l=40, r=40, t=80, b=40),
                height=550
            )
            
            # 스트림릿 화면에 Plotly 차트 출력 🎉
            st.plotly_chart(fig, use_container_width=True)
            
            # 5. 간단한 데이터 요약 정보 카드 배치 🧩
            st.subheader("🎒 요약 처방전 & 현재 주가 상태")
            cols = st.columns(len(selected_names))
            
            for idx, name in enumerate(selected_names):
                ticker = top10_companies[name]
                if ticker in raw_data.columns:
                    series = raw_data[ticker].dropna()
                    if not series.empty:
                        current_price = series.iloc[-1]
                        initial_price = series.iloc[0]
                        total_return = ((current_price - initial_price) / initial_price) * 100
                        
                        # 각 칸마다 귀여운 메트릭 위젯으로 성과 표시 🧸
                        with cols[idx]:
                            st.metric(
                                label=name,
                                value=f"{current_price:,.2f}",
                                delta=f"{total_return:+.2f}% (1년)"
                            )
                            
        except Exception as e:
            st.error(f"❌ 데이터를 가져오는 도중 오류가 발생했어요: {e}")

# 6. 푸터 🎀
st.divider()
st.caption("🌈 본 정보는 yfinance 공공 API를 기반으로 실시간 제공됩니다. 주식 요정과 함께하는 달콤한 투자 공부 시간 완료! 🤙💕")
