import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import warnings
warnings.filterwarnings('ignore')

from events_db import EVENTS, CATEGORY_LABELS, CATEGORY_COLORS, get_events_by_category, get_event_by_id, get_intensity_rank
from charts import fetch_sector_data, plot_time_series, plot_radar, plot_causality, SECTOR_COLORS

# ============================================================
# PAGE CONFIG
# ============================================================
st.set_page_config(
    page_title="AlpineShock",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# DESIGN
# ============================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@300;400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap');

* { font-family: 'IBM Plex Sans', sans-serif; }

.stApp { background-color: #08090e; color: #e8eaf0; }

section[data-testid="stSidebar"] {
    background-color: #0d0f17;
    border-right: 1px solid #1a1d2e;
}
section[data-testid="stSidebar"] * { color: #e8eaf0; }

.stSelectbox > div > div {
    background-color: #12141f !important;
    border: 1px solid #1e2130 !important;
    border-radius: 8px !important;
    color: #e8eaf0 !important;
}
.stSelectbox [data-baseweb="select"] > div {
    background-color: #12141f !important;
    border-color: #1e2130 !important;
}

.stTabs [data-baseweb="tab-list"] {
    background-color: #08090e;
    border-bottom: 1px solid #1a1d2e;
    gap: 0;
}
.stTabs [data-baseweb="tab"] {
    color: #3a4050;
    font-size: 0.78rem;
    font-weight: 500;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    padding: 0.7rem 1.4rem;
    border-bottom: 2px solid transparent;
    background: transparent !important;
}
.stTabs [aria-selected="true"] {
    color: #e8eaf0 !important;
    border-bottom: 2px solid #4a9eff !important;
    background: transparent !important;
}
.stTabs [data-baseweb="tab"]:hover { color: #8892b0 !important; }

.as-card {
    background-color: #10121c;
    border: 1px solid #1e2130;
    border-radius: 10px;
    padding: 1.1rem 1.3rem;
    margin-bottom: 0.6rem;
}
.as-kpi {
    background-color: #0d0f17;
    border: 1px solid #252840;
    border-radius: 10px;
    padding: 1rem 1.2rem;
    margin-bottom: 0.6rem;
}
.as-label {
    font-size: 0.62rem;
    font-weight: 500;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #3a4050;
    margin-bottom: 0.3rem;
}
.as-value {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 1.4rem;
    font-weight: 500;
    color: #e8eaf0;
}
.as-section-title {
    font-size: 0.62rem;
    font-weight: 500;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #3a4050;
    margin-bottom: 0.8rem;
    padding-bottom: 0.45rem;
    border-bottom: 1px solid #1a1d2e;
}
.as-tag {
    display: inline-block;
    padding: 0.12rem 0.55rem;
    border-radius: 4px;
    font-size: 0.62rem;
    font-weight: 600;
    letter-spacing: 0.07em;
    text-transform: uppercase;
}
.as-event-header {
    padding: 1rem 0 0.9rem 0;
    border-bottom: 1px solid #1a1d2e;
    margin-bottom: 1.2rem;
}

hr { border-color: #1a1d2e; }
#MainMenu, footer, header { visibility: hidden; }
.stSpinner > div { border-color: #4a9eff transparent transparent transparent !important; }

/* Hide sidebar collapse button completely */
button[data-testid="baseButton-headerNoPadding"],
button[data-testid="collapsedControl"],
[data-testid="collapsedControl"] {
    display: none !important;
}
</style>
""", unsafe_allow_html=True)

# Fixed top header bar
st.markdown("""
<style>
body::before {
    content: '';
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    height: 2px;
    background: linear-gradient(90deg, #4a9eff, #7c5cbf, #4a9eff);
    z-index: 99999;
    pointer-events: none;
}

.as-topbar {
    position: fixed;
    top: 2px;
    left: 0;
    right: 0;
    height: 42px;
    background: #08090e;
    border-bottom: 1px solid #1a1d2e;
    display: flex;
    align-items: center;
    padding: 0 1.5rem;
    z-index: 9998;
    gap: 0.6rem;
}
.as-topbar-name {
    font-size: 0.88rem;
    font-weight: 600;
    letter-spacing: -0.01em;
    color: #e8eaf0;
}
.as-topbar-sub {
    font-size: 0.6rem;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: #2a3040;
    margin-top: 1px;
}
/* Push content down to account for topbar */
.main .block-container {
    padding-top: 4rem !important;
}
section[data-testid="stSidebar"] {
    padding-top: 44px !important;
}
</style>
<div class="as-topbar"></div>
""", unsafe_allow_html=True)

# ============================================================
# SIDEBAR
# ============================================================
with st.sidebar:
    st.markdown("""
    <div style="padding:0.8rem 0 0.8rem 0;">
        <div style="font-size:0.6rem;color:#2a3040;letter-spacing:0.1em;text-transform:uppercase;">Market Impact Analyzer</div>
    </div>
    <div style="border-top:1px solid #1a1d2e;margin-bottom:1rem;"></div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="as-label" style="margin-bottom:0.4rem;">Market</div>', unsafe_allow_html=True)
    market_options = {"SMI — Swiss Market Index": "smi", "S&P 500": "sp500", "NASDAQ": "nasdaq"}
    market_label = st.selectbox("", list(market_options.keys()), label_visibility="collapsed", key="market_sel")
    market_key = market_options[market_label]

    st.markdown('<div class="as-label" style="margin-top:1rem;margin-bottom:0.4rem;">Event Category</div>', unsafe_allow_html=True)
    category_options = {v: k for k, v in CATEGORY_LABELS.items()}
    selected_cat_label = st.selectbox("", list(CATEGORY_LABELS.values()), label_visibility="collapsed", key="cat_sel")
    selected_cat = category_options[selected_cat_label]

    st.markdown('<div class="as-label" style="margin-top:1rem;margin-bottom:0.4rem;">Event</div>', unsafe_allow_html=True)
    events_in_cat = get_events_by_category(selected_cat)
    event_names = {e["name"]: e["id"] for e in events_in_cat}
    selected_event_name = st.selectbox("", list(event_names.keys()), label_visibility="collapsed", key="event_sel")
    selected_event_id = event_names[selected_event_name]
    event = get_event_by_id(selected_event_id)

    st.markdown('<div style="border-top:1px solid #1a1d2e;margin-top:1.5rem;margin-bottom:0.8rem;"></div>', unsafe_allow_html=True)
    st.markdown('<div style="font-size:0.58rem;color:#2a3040;letter-spacing:0.06em;">ALPINESHOCK v1.1</div>', unsafe_allow_html=True)

# ============================================================
# TITLE + TABS
# ============================================================
st.markdown("""
<div style="padding:1.5rem 0 0.5rem 0;display:flex;align-items:baseline;gap:0.8rem;">
    <div style="font-size:1.4rem;font-weight:600;letter-spacing:-0.03em;color:#e8eaf0;">AlpineShock</div>
    <div style="font-size:0.6rem;font-weight:500;letter-spacing:0.12em;text-transform:uppercase;color:#2a3040;padding-bottom:2px;">Market Impact Analyzer</div>
</div>
""", unsafe_allow_html=True)

tab_impact, tab_method = st.tabs(["Impact Analysis", "Methodology"])

# ============================================================
# TAB 1 — IMPACT ANALYSIS
# ============================================================
with tab_impact:

    # ── Hero ─────────────────────────────────────────────────
    total_events = sum(len(v) for v in EVENTS.values())
    st.markdown(f"""
    <div style="padding:2.5rem 0 2rem 0;border-bottom:1px solid #1a1d2e;margin-bottom:2rem;">
        <div style="font-size:0.62rem;font-weight:500;letter-spacing:0.15em;text-transform:uppercase;color:#4a9eff;margin-bottom:0.8rem;">
            Global Market Impact Analyzer
        </div>
        <div style="font-size:2.4rem;font-weight:600;letter-spacing:-0.04em;color:#e8eaf0;line-height:1.15;margin-bottom:0.6rem;">
            How do geopolitical shocks<br>move financial markets?
        </div>
        <div style="font-size:0.88rem;color:#3a4050;max-width:560px;line-height:1.7;margin-bottom:2rem;">
            Select an event in the sidebar to analyze its real market impact across sectors,
            with live price data sourced from Yahoo Finance.
        </div>
        <div style="display:flex;gap:2.5rem;">
            <div>
                <div style="font-family:'IBM Plex Mono',monospace;font-size:1.6rem;font-weight:500;color:#e8eaf0;">{total_events}</div>
                <div style="font-size:0.6rem;letter-spacing:0.1em;text-transform:uppercase;color:#4a5060;margin-top:0.1rem;">Historical Events</div>
            </div>
            <div style="width:1px;background:#1a1d2e;"></div>
            <div>
                <div style="font-family:'IBM Plex Mono',monospace;font-size:1.6rem;font-weight:500;color:#e8eaf0;">3</div>
                <div style="font-size:0.6rem;letter-spacing:0.1em;text-transform:uppercase;color:#4a5060;margin-top:0.1rem;">Markets</div>
            </div>
            <div style="width:1px;background:#1a1d2e;"></div>
            <div>
                <div style="font-family:'IBM Plex Mono',monospace;font-size:1.6rem;font-weight:500;color:#e8eaf0;">9</div>
                <div style="font-size:0.6rem;letter-spacing:0.1em;text-transform:uppercase;color:#4a5060;margin-top:0.1rem;">Event Categories</div>
            </div>
            <div style="width:1px;background:#1a1d2e;"></div>
            <div>
                <div style="font-family:'IBM Plex Mono',monospace;font-size:1.6rem;font-weight:500;color:#e8eaf0;">1990</div>
                <div style="font-size:0.6rem;letter-spacing:0.1em;text-transform:uppercase;color:#4a5060;margin-top:0.1rem;">Data Since</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    if not event:
        st.markdown('<div class="as-card" style="color:#5a6070;font-size:0.88rem;">Select an event in the sidebar to begin.</div>', unsafe_allow_html=True)
    else:
        impact_key = f"{market_key}_impact"
        impacts = event.get(impact_key, {})
        cat_color = CATEGORY_COLORS.get(event["category"], "#5a6070")
        rank, total_in_cat = get_intensity_rank(event["id"], event["category"])

        st.markdown(f"""
        <div class="as-event-header">
            <span class="as-tag" style="background:{cat_color}18;color:{cat_color};border:1px solid {cat_color}28;">
                {CATEGORY_LABELS.get(event['category'], '').upper()}
            </span>
            <div style="font-size:1.5rem;font-weight:600;color:#e8eaf0;margin:0.5rem 0 0.2rem 0;letter-spacing:-0.02em;">
                {event['name']}
            </div>
            <div style="font-size:0.78rem;color:#3a4050;line-height:1.6;">
                {event['date']} &nbsp;&middot;&nbsp; {event['description']}
            </div>
        </div>
        """, unsafe_allow_html=True)

        # KPI row
        c1, c2, c3, c4 = st.columns(4)
        rank_str = f"#{rank} / {total_in_cat}" if rank else "—"
        for col, lbl, val in zip(
            [c1, c2, c3, c4],
            ["Intensity", "Amplitude", "Contagion", "Rank in Category"],
            [f'{event["intensity_score"]}<span style="font-size:0.8rem;color:#3a4050;">/100</span>',
             f'{event["amplitude"]}<span style="font-size:0.8rem;color:#3a4050;">/100</span>',
             f'{event["contagion"]}<span style="font-size:0.8rem;color:#3a4050;">/100</span>',
             rank_str]
        ):
            with col:
                st.markdown(f'<div class="as-kpi"><div class="as-label">{lbl}</div><div class="as-value">{val}</div></div>', unsafe_allow_html=True)

        # Time Series
        st.markdown('<div style="margin-top:1.4rem;" class="as-section-title">Price Action — Indexed to Event Date</div>', unsafe_allow_html=True)
        st.markdown("""
        <div style="display:flex;gap:1.5rem;margin-bottom:0.6rem;align-items:center;">
            <div style="display:flex;align-items:center;gap:0.5rem;">
                <svg width="28" height="10"><line x1="0" y1="5" x2="28" y2="5" stroke="#8892b0" stroke-width="2"/></svg>
                <span style="font-size:0.65rem;color:#3a4050;letter-spacing:0.06em;text-transform:uppercase;">Pre-event</span>
            </div>
            <div style="display:flex;align-items:center;gap:0.5rem;">
                <svg width="28" height="10"><line x1="0" y1="5" x2="28" y2="5" stroke="#8892b0" stroke-width="2" stroke-dasharray="3,4"/></svg>
                <span style="font-size:0.65rem;color:#3a4050;letter-spacing:0.06em;text-transform:uppercase;">Post-event</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

        with st.spinner("Fetching market data..."):
            sector_data, event_date = fetch_sector_data(market_key, event["date"])

        if sector_data:
            fig_ts = plot_time_series(event, market_key, sector_data, event_date)
            if fig_ts:
                st.plotly_chart(fig_ts, use_container_width=True, config={"displayModeBar": False})
        else:
            st.markdown('<div class="as-card" style="color:#3a4050;font-size:0.82rem;">No market data available for this date range.</div>', unsafe_allow_html=True)

        # Radar + Causality
        col_left, col_right = st.columns(2, gap="medium")

        with col_left:
            st.markdown('<div class="as-section-title">Shock Profile</div>', unsafe_allow_html=True)
            fig_radar = plot_radar(event)
            st.plotly_chart(fig_radar, use_container_width=True, config={"displayModeBar": False})

        with col_right:
            st.markdown('<div class="as-section-title">Causal Confidence by Sector</div>', unsafe_allow_html=True)
            st.markdown('<div style="font-size:0.68rem;color:#2a3040;margin-bottom:0.5rem;">Likelihood that this event directly caused the observed market movement.</div>', unsafe_allow_html=True)
            fig_caus = plot_causality(event, market_key)
            if fig_caus:
                fig_caus.update_layout(title="")
                st.plotly_chart(fig_caus, use_container_width=True, config={"displayModeBar": False})

        # Sector Impact
        if impacts:
            st.markdown('<div style="margin-top:0.8rem;" class="as-section-title">Sector Impact</div>', unsafe_allow_html=True)
            c1, c2, c3 = st.columns(3)
            best_s  = max(impacts, key=impacts.get)
            worst_s = min(impacts, key=impacts.get)
            avg_v   = np.mean(list(impacts.values()))

            def signed(v):
                return ("+" if v >= 0 else "") + f"{v:.1f}%"

            with c1:
                st.markdown(f"""
                <div class="as-kpi">
                    <div class="as-label">Best Sector</div>
                    <div style="font-size:0.92rem;font-weight:500;color:#e8eaf0;margin:0.25rem 0 0.15rem;">{best_s}</div>
                    <div style="font-family:'IBM Plex Mono';color:#00c896;font-size:1.05rem;">{signed(impacts[best_s])}</div>
                </div>
                """, unsafe_allow_html=True)
            with c2:
                st.markdown(f"""
                <div class="as-kpi">
                    <div class="as-label">Worst Sector</div>
                    <div style="font-size:0.92rem;font-weight:500;color:#e8eaf0;margin:0.25rem 0 0.15rem;">{worst_s}</div>
                    <div style="font-family:'IBM Plex Mono';color:#ff4757;font-size:1.05rem;">{signed(impacts[worst_s])}</div>
                </div>
                """, unsafe_allow_html=True)
            with c3:
                avg_color = "#00c896" if avg_v >= 0 else "#ff4757"
                st.markdown(f"""
                <div class="as-kpi">
                    <div class="as-label">Average Impact</div>
                    <div style="font-family:'IBM Plex Mono';color:{avg_color};font-size:1.2rem;margin-top:0.35rem;">{signed(avg_v)}</div>
                </div>
                """, unsafe_allow_html=True)

# ============================================================
# TAB 2 — METHODOLOGY
# ============================================================
with tab_method:
    st.markdown('<div style="padding-top:1rem;"></div>', unsafe_allow_html=True)

    sections = [
        ("About AlpineShock",
         "AlpineShock is a data-driven market impact analyzer that quantifies how geopolitical and macroeconomic events affect global financial markets. Built for finance professionals, researchers, and students interested in the intersection of international relations and financial markets."),
        ("Data Collection",
         "<strong style='color:#c8cad4;'>Source</strong> — Historical price data sourced via Yahoo Finance (yfinance), covering the SMI, S&P 500, and NASDAQ since 1990.<br><br>"
         "<strong style='color:#c8cad4;'>Sectors</strong> — Each market is broken into 6 representative sectors tracked via proxy tickers (e.g. UBSG.SW for Swiss Banks, NVDA for NASDAQ Semiconductors)."),
        ("Impact Measurement",
         "<strong style='color:#c8cad4;'>Indexing</strong> — Sector performance is normalized to the 5-day average before the event date, allowing cross-event comparisons regardless of absolute price level.<br><br>"
         "<strong style='color:#c8cad4;'>Window</strong> — Pre-event: 40 trading days. Post-event: 60 trading days.<br><br>"
         "<strong style='color:#c8cad4;'>Aggregation</strong> — Multi-ticker sectors are averaged before normalization."),
        ("Intensity Scoring",
         "Each event is manually scored 0–100 across three dimensions:<br><br>"
         "<strong style='color:#c8cad4;'>Amplitude</strong> — Peak-to-trough price move across affected sectors.<br>"
         "<strong style='color:#c8cad4;'>Contagion</strong> — Cross-market and cross-sector spread.<br>"
         "<strong style='color:#c8cad4;'>Duration</strong> — Days until broad market recovery to pre-event levels."),
        ("Causal Confidence",
         "The Causal Confidence chart estimates the probability that the observed market movement was <em>directly</em> caused by the event, rather than concurrent macro factors. Scores are derived from academic literature, post-event attribution analysis, and cross-market correlations.<br><br>"
         "<strong style='color:#00c896;'>High</strong> ≥ 80 &nbsp;·&nbsp; <strong style='color:#ffa502;'>Moderate</strong> ≥ 55 &nbsp;·&nbsp; <strong style='color:#ff4757;'>Low</strong> &lt; 55"),
        ("Disclaimer",
         "AlpineShock is for educational and research purposes only. It does not constitute financial advice. Past market reactions to historical events do not guarantee future outcomes. All data is provided as-is without warranty."),
    ]

    for title, body in sections:
        st.markdown(f"""
        <div class="as-card" style="margin-bottom:0.7rem;">
            <div class="as-label" style="margin-bottom:0.5rem;">{title}</div>
            <div style="font-size:0.84rem;color:#5a6070;line-height:1.9;">{body}</div>
        </div>
        """, unsafe_allow_html=True)