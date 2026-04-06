import yfinance as yf
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

# ============================================================
# TICKERS PAR MARCHÉ ET SECTEUR
# ============================================================
MARKET_TICKERS = {
    "smi": {
        "Banques":      ["UBSG.SW"],
        "Pharma":       ["NOVN.SW", "ROG.SW"],
        "Alimentation": ["NESN.SW"],
        "Luxe/Export":  ["CFR.SW", "UHR.SW"],
        "Assurance":    ["ZURN.SW"],
        "Industrie":    ["GEBN.SW"],
    },
    "sp500": {
        "Tech":         ["AAPL", "MSFT"],
        "Banques":      ["JPM", "BAC"],
        "Energie":      ["XOM", "CVX"],
        "Sante":        ["JNJ", "PFE"],
        "Consommation": ["AMZN", "WMT"],
        "Industrie":    ["BA", "CAT"],
    },
    "nasdaq": {
        "Tech":         ["AAPL", "MSFT", "GOOGL"],
        "Biotech":      ["AMGN", "GILD"],
        "Energie":      ["XOM"],
        "Cyber":        ["PANW", "CRWD"],
        "Semi":         ["NVDA", "AMD"],
        "Defence":      ["LMT", "RTX"],
    },
}

# Couleurs par secteur
SECTOR_COLORS = {
    "Banques":      "#4a9eff",
    "Pharma":       "#00c896",
    "Alimentation": "#ffa502",
    "Luxe/Export":  "#9b59b6",
    "Assurance":    "#e74c3c",
    "Industrie":    "#f1c40f",
    "Tech":         "#4a9eff",
    "Biotech":      "#00c896",
    "Energie":      "#ffa502",
    "Sante":        "#2ecc71",
    "Consommation": "#9b59b6",
    "Semi":         "#f1c40f",
    "Cyber":        "#e74c3c",
    "Defence":      "#e67e22",
}

# ============================================================
# SCORES DE CAUSALITÉ PAR CATÉGORIE D'ÉVÈNEMENT & MARCHÉ
# ============================================================
CAUSALITY_SCORES = {
    "war": {
        "smi":   {"Banques": 55, "Pharma": 40, "Alimentation": 60, "Luxe/Export": 80, "Assurance": 65, "Industrie": 70},
        "sp500": {"Tech": 45, "Banques": 50, "Energie": 90, "Sante": 35, "Consommation": 55, "Industrie": 65},
        "nasdaq":{"Tech": 40, "Biotech": 30, "Energie": 75, "Cyber": 85, "Semi": 45, "Defence": 95},
    },
    "banking": {
        "smi":   {"Banques": 95, "Pharma": 40, "Alimentation": 50, "Luxe/Export": 60, "Assurance": 85, "Industrie": 55},
        "sp500": {"Tech": 55, "Banques": 95, "Energie": 45, "Sante": 40, "Consommation": 60, "Industrie": 65},
        "nasdaq":{"Tech": 50, "Biotech": 35, "Energie": 30, "Cyber": 40, "Semi": 55, "Defence": 25},
    },
    "central_bank": {
        "smi":   {"Banques": 85, "Pharma": 40, "Alimentation": 45, "Luxe/Export": 70, "Assurance": 80, "Industrie": 60},
        "sp500": {"Tech": 75, "Banques": 85, "Energie": 55, "Sante": 45, "Consommation": 70, "Industrie": 65},
        "nasdaq":{"Tech": 80, "Biotech": 45, "Energie": 40, "Cyber": 60, "Semi": 75, "Defence": 35},
    },
    "pandemic": {
        "smi":   {"Banques": 85, "Pharma": 75, "Alimentation": 70, "Luxe/Export": 90, "Assurance": 85, "Industrie": 80},
        "sp500": {"Tech": 60, "Banques": 85, "Energie": 95, "Sante": 80, "Consommation": 85, "Industrie": 90},
        "nasdaq":{"Tech": 55, "Biotech": 90, "Energie": 90, "Cyber": 50, "Semi": 65, "Defence": 60},
    },
    "political": {
        "smi":   {"Banques": 60, "Pharma": 45, "Alimentation": 35, "Luxe/Export": 65, "Assurance": 50, "Industrie": 40},
        "sp500": {"Tech": 50, "Banques": 70, "Energie": 60, "Sante": 75, "Consommation": 55, "Industrie": 65},
        "nasdaq":{"Tech": 55, "Biotech": 70, "Energie": 45, "Cyber": 50, "Semi": 55, "Defence": 60},
    },
    "inflation": {
        "smi":   {"Banques": 70, "Pharma": 45, "Alimentation": 75, "Luxe/Export": 65, "Assurance": 60, "Industrie": 70},
        "sp500": {"Tech": 80, "Banques": 65, "Energie": 90, "Sante": 50, "Consommation": 75, "Industrie": 70},
        "nasdaq":{"Tech": 85, "Biotech": 55, "Energie": 85, "Cyber": 70, "Semi": 80, "Defence": 40},
    },
    "tech": {
        "smi":   {"Banques": 35, "Pharma": 50, "Alimentation": 25, "Luxe/Export": 30, "Assurance": 30, "Industrie": 40},
        "sp500": {"Tech": 90, "Banques": 45, "Energie": 30, "Sante": 55, "Consommation": 65, "Industrie": 35},
        "nasdaq":{"Tech": 95, "Biotech": 60, "Energie": 25, "Cyber": 85, "Semi": 95, "Defence": 20},
    },
    "natural": {
        "smi":   {"Banques": 45, "Pharma": 35, "Alimentation": 50, "Luxe/Export": 40, "Assurance": 90, "Industrie": 55},
        "sp500": {"Tech": 30, "Banques": 50, "Energie": 75, "Sante": 40, "Consommation": 60, "Industrie": 55},
        "nasdaq":{"Tech": 25, "Biotech": 35, "Energie": 65, "Cyber": 20, "Semi": 30, "Defence": 25},
    },
    "sanctions": {
        "smi":   {"Banques": 65, "Pharma": 40, "Alimentation": 70, "Luxe/Export": 85, "Assurance": 55, "Industrie": 75},
        "sp500": {"Tech": 70, "Banques": 60, "Energie": 85, "Sante": 40, "Consommation": 65, "Industrie": 75},
        "nasdaq":{"Tech": 75, "Biotech": 35, "Energie": 80, "Cyber": 65, "Semi": 80, "Defence": 55},
    },
}

def get_causality_label(score):
    if score >= 80:
        return "High", "#00c896"
    elif score >= 55:
        return "Moderate", "#ffa502"
    else:
        return "Low", "#ff4757"

# ============================================================
# FONCTION : RÉCUPÉRER DONNÉES RÉELLES
# ============================================================
def fetch_sector_data(market_key, event_date_str, days_before=40, days_after=60):
    event_date = pd.to_datetime(event_date_str)
    start = (event_date - timedelta(days=days_before + 10)).strftime('%Y-%m-%d')
    end = (event_date + timedelta(days=days_after + 10)).strftime('%Y-%m-%d')

    tickers_dict = MARKET_TICKERS.get(market_key, {})
    sector_data = {}

    for sector, tickers in tickers_dict.items():
        combined = None
        for ticker in tickers:
            try:
                df = yf.download(ticker, start=start, end=end,
                                 auto_adjust=True, progress=False)
                if df.empty:
                    continue
                close = df['Close'].squeeze()
                if isinstance(close, pd.DataFrame):
                    close = close.iloc[:, 0]
                if combined is None:
                    combined = close
                else:
                    combined = combined.add(close, fill_value=0)
            except:
                continue

        if combined is not None and len(combined) > 5:
            if len(tickers) > 1:
                combined = combined / len(tickers)

            # Normalise to average of the 5 trading days BEFORE the event
            # This way lines arrive already spread out at the event line
            pre_event = combined[combined.index < event_date]
            if len(pre_event) >= 3:
                base = float(pre_event.iloc[-5:].mean())
            elif len(pre_event) > 0:
                base = float(pre_event.iloc[-1])
            else:
                continue

            if base > 0:
                normalized = (combined / base) * 100
                sector_data[sector] = normalized

    return sector_data, event_date

# ============================================================
# GRAPHIQUE TIME SERIES PRINCIPAL
# ============================================================
def plot_time_series(event, market_key, sector_data, event_date):
    if not sector_data:
        return None

    fig = go.Figure()

    # Ligne verticale de l'évènement
    all_dates = []
    for s, data in sector_data.items():
        all_dates.extend(data.index.tolist())

    # Tracer chaque secteur
    for sector, data in sector_data.items():
        color = SECTOR_COLORS.get(sector, "#5a6070")

        # Split cleanly at event date
        pre_data  = data[data.index < event_date]
        post_data = data[data.index >= event_date]

        # PRE-EVENT — solid line
        if len(pre_data) > 0:
            fig.add_trace(go.Scatter(
                x=pre_data.index,
                y=pre_data.values,
                name=sector,
                line=dict(color=color, width=2),
                mode='lines',
                legendgroup=sector,
                showlegend=True,
                hovertemplate=f"<b>{sector}</b><br>%{{x|%d %b %Y}}<br>%{{y:.1f}}<extra></extra>",
            ))

        # POST-EVENT — dotted, starts exactly at event date
        # Connect with last pre-event point so there's no gap
        if len(post_data) > 0:
            if len(pre_data) > 0:
                connect_x = [pre_data.index[-1]] + list(post_data.index)
                connect_y = [pre_data.values[-1]] + list(post_data.values)
            else:
                connect_x = list(post_data.index)
                connect_y = list(post_data.values)

            fig.add_trace(go.Scatter(
                x=connect_x,
                y=connect_y,
                name=sector,
                line=dict(color=color, width=2, dash='2px,5px'),
                mode='lines',
                legendgroup=sector,
                showlegend=False,
                hovertemplate=f"<b>{sector}</b><br>%{{x|%d %b %Y}}<br>%{{y:.1f}}<extra></extra>",
            ))

    # Ligne verticale event
    fig.add_vline(
        x=event_date,
        line=dict(color="#ffffff", width=1, dash="dash"),
        opacity=0.3,
    )

    # Annotation event
    fig.add_annotation(
        x=event_date,
        y=1.02,
        xref="x",
        yref="paper",
        text=event['name'][:30] + "..." if len(event['name']) > 30 else event['name'],
        showarrow=False,
        font=dict(color="#5a6070", size=10, family="IBM Plex Sans"),
        xanchor="left",
    )

    # Zone grisée avant event
    if all_dates:
        fig.add_vrect(
            x0=min(all_dates),
            x1=event_date,
            fillcolor="#ffffff",
            opacity=0.02,
            layer="below",
            line_width=0,
        )

    # Ligne de base à 100
    fig.add_hline(
        y=100,
        line=dict(color="#2a3040", width=1, dash="dot"),
        opacity=0.8,
    )

    market_names = {
        "smi": "SMI — Swiss Market Index",
        "sp500": "S&P 500",
        "nasdaq": "NASDAQ",
    }

    fig.update_layout(
        paper_bgcolor='#08090e',
        plot_bgcolor='#0d0f17',
        font=dict(color='#5a6070', family='IBM Plex Sans', size=12),
        title=dict(
            text=f"Market Impact — {event['name']} | {market_names.get(market_key, market_key)}",
            font=dict(color='#e8eaf0', size=14, family='IBM Plex Sans'),
            x=0,
        ),
        xaxis=dict(
            gridcolor='#1a1d2e',
            linecolor='#1e2130',
            tickfont=dict(color='#5a6070', size=11),
            showgrid=True,
        ),
        yaxis=dict(
            gridcolor='#1a1d2e',
            linecolor='#1e2130',
            tickfont=dict(color='#5a6070', size=11),
            title=dict(text="Indexed (100 = event day)", font=dict(color='#5a6070', size=11)),
            showgrid=True,
        ),
        legend=dict(
            bgcolor='#0d0f17',
            bordercolor='#1e2130',
            borderwidth=1,
            font=dict(color='#e8eaf0', size=11),
            orientation='h',
            yanchor='bottom',
            y=1.02,
            xanchor='right',
            x=1,
        ),
        hovermode='x unified',
        hoverlabel=dict(
            bgcolor='#12141f',
            bordercolor='#1e2130',
            font=dict(color='#e8eaf0', size=12, family='IBM Plex Mono'),
        ),
        margin=dict(t=80, b=40, l=60, r=20),
        height=480,
        dragmode='pan',
    )

    return fig

# ============================================================
# SHOCK PROFILE — horizontal bar chart
# ============================================================
def plot_radar(event):
    recovery_speed = max(0, 100 - min(event.get('recovery_days', 365) / 10, 100))
    duration_score = min(event.get('duration_days', 90) / 10, 100)

    labels = ['Intensity', 'Amplitude', 'Contagion', 'Duration', 'Recovery Speed']
    values = [
        event.get('intensity_score', 50),
        event.get('amplitude', 50),
        event.get('contagion', 50),
        duration_score,
        recovery_speed,
    ]

    bar_colors = []
    for v in values:
        if v >= 75:
            bar_colors.append("#ff4757")
        elif v >= 50:
            bar_colors.append("#ffa502")
        else:
            bar_colors.append("#4a9eff")

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=values,
        y=labels,
        orientation='h',
        marker=dict(color=bar_colors, opacity=0.85),
        text=[f"{v:.0f}" for v in values],
        textposition='outside',
        textfont=dict(color='#8892b0', size=11, family='IBM Plex Mono'),
        hovertemplate='<b>%{y}</b><br>Score: %{x:.0f}/100<extra></extra>',
    ))

    fig.update_layout(
        paper_bgcolor='#08090e',
        plot_bgcolor='#0d0f17',
        font=dict(color='#5a6070', family='IBM Plex Sans'),
        xaxis=dict(
            range=[0, 115],
            gridcolor='#1a1d2e',
            linecolor='#1e2130',
            tickfont=dict(color='#3a4050', size=10),
            showgrid=True,
            zeroline=False,
        ),
        yaxis=dict(
            gridcolor='#1a1d2e',
            linecolor='#1e2130',
            tickfont=dict(color='#8892b0', size=11),
            showgrid=False,
        ),
        showlegend=False,
        margin=dict(t=10, b=20, l=10, r=40),
        height=300,
        bargap=0.35,
    )
    return fig

# ============================================================
# GRAPHIQUE CAUSALITÉ
# ============================================================
def plot_causality(event, market_key):
    cat = event.get('category', 'war')
    scores = CAUSALITY_SCORES.get(cat, {}).get(market_key, {})
    if not scores:
        return None

    sectors = list(scores.keys())
    values = list(scores.values())
    colors = []
    for v in values:
        if v >= 80:
            colors.append("#00c896")
        elif v >= 55:
            colors.append("#ffa502")
        else:
            colors.append("#ff4757")

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=sectors,
        y=values,
        marker_color=colors,
        marker_opacity=0.8,
        text=[f"{v}%" for v in values],
        textposition='outside',
        textfont=dict(color='#e8eaf0', size=11, family='IBM Plex Mono'),
    ))

    fig.add_hline(y=80, line=dict(color="#00c896", width=1, dash="dot"), opacity=0.4)
    fig.add_hline(y=55, line=dict(color="#ffa502", width=1, dash="dot"), opacity=0.4)

    fig.update_layout(
        paper_bgcolor='#08090e',
        plot_bgcolor='#0d0f17',
        font=dict(color='#5a6070', family='IBM Plex Sans'),
        title=dict(
            text="Causal Confidence by Sector",
            font=dict(color='#e8eaf0', size=13, family='IBM Plex Sans'),
            x=0,
        ),
        xaxis=dict(gridcolor='#1a1d2e', linecolor='#1e2130', tickfont=dict(color='#8892b0', size=11)),
        yaxis=dict(
            gridcolor='#1a1d2e', linecolor='#1e2130',
            range=[0, 110],
            tickfont=dict(color='#5a6070', size=11),
            title=dict(text="Confidence (%)", font=dict(color='#5a6070', size=11)),
        ),
        showlegend=False,
        margin=dict(t=50, b=30, l=50, r=20),
        height=300,
    )
    return fig