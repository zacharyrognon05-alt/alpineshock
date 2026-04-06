import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import warnings
import os
warnings.filterwarnings('ignore')

# ============================================================
# BASE DE DONNÉES DES ÉVÈNEMENTS HISTORIQUES
# ============================================================
EVENTS_DB = [
    {"name": "COVID-19 Pandemic", "date": "2020-02-24", "type": "pandemic", "intensity": 10},
    {"name": "Russia Ukraine War", "date": "2022-02-24", "type": "war", "intensity": 8},
    {"name": "BNS Taux Negatifs", "date": "2015-01-15", "type": "central_bank", "intensity": 7},
    {"name": "US Fed Rate Hike 2022", "date": "2022-03-16", "type": "central_bank", "intensity": 6},
    {"name": "Credit Suisse Collapse", "date": "2023-03-15", "type": "banking_crisis", "intensity": 8},
    {"name": "Global Financial Crisis", "date": "2008-09-15", "type": "banking_crisis", "intensity": 10},
    {"name": "Brexit Vote", "date": "2016-06-24", "type": "political", "intensity": 6},
    {"name": "US Election Trump 2016", "date": "2016-11-09", "type": "political", "intensity": 5},
    {"name": "Inflation Peak 2022", "date": "2022-06-10", "type": "inflation", "intensity": 7},
    {"name": "SVB Bank Collapse", "date": "2023-03-10", "type": "banking_crisis", "intensity": 6},
]

# ============================================================
# SECTEURS SMI ET S&P 500
# ============================================================
SMI_SECTORS = {
    "Banques":      ["UBSG.SW"],
    "Pharma":       ["NOVN.SW", "ROG.SW"],
    "Alimentation": ["NESN.SW"],
    "Luxe/Export":  ["CFR.SW", "UHR.SW"],
    "Assurance":    ["ZURN.SW"],
    "Industrie":    ["GEBN.SW"],
}

SP500_SECTORS = {
    "Tech":         ["AAPL", "MSFT", "GOOGL"],
    "Banques":      ["JPM", "BAC", "GS"],
    "Energie":      ["XOM", "CVX"],
    "Sante":        ["JNJ", "PFE"],
    "Consommation": ["AMZN", "WMT"],
    "Industrie":    ["BA", "CAT"],
}

SAVE_DIR = os.path.expanduser("~/Desktop")

# ============================================================
# FONCTION : CALCULER L'IMPACT D'UN ÉVÈNEMENT
# ============================================================
def get_event_impact(event, sectors, window_after=20):
    date = pd.to_datetime(event["date"])
    impacts = {}
    for sector_name, tickers in sectors.items():
        sector_returns = []
        for ticker in tickers:
            try:
                start = (date - timedelta(days=15)).strftime('%Y-%m-%d')
                end = (date + timedelta(days=window_after + 15)).strftime('%Y-%m-%d')
                df = yf.download(ticker, start=start, end=end, auto_adjust=True, progress=False)
                if df.empty or len(df) < 5:
                    continue
                close = df['Close'].squeeze().dropna()
                pre = close[close.index <= date]
                post = close[close.index > date]
                if len(pre) == 0 or len(post) == 0:
                    continue
                pre_price = float(pre.iloc[-1])
                post_price = float(post.iloc[min(window_after-1, len(post)-1)])
                ret = ((post_price - pre_price) / pre_price) * 100
                sector_returns.append(ret)
            except:
                continue
        impacts[sector_name] = round(np.mean(sector_returns), 2) if sector_returns else 0.0
    return impacts

# ============================================================
# FONCTION : ANALYSER TOUS LES ÉVÈNEMENTS
# ============================================================
def build_historical_impacts(market="SMI"):
    sectors = SMI_SECTORS if market == "SMI" else SP500_SECTORS
    print(f"\n📊 Analyse historique {market} en cours...")
    print("(Cela peut prendre 2-3 minutes)\n")
    results = []
    for i, event in enumerate(EVENTS_DB):
        print(f"[{i+1}/{len(EVENTS_DB)}] {event['name']}...")
        impacts = get_event_impact(event, sectors)
        row = {"event": event["name"], "type": event["type"], "intensity": event["intensity"], "date": event["date"]}
        row.update(impacts)
        results.append(row)
    df = pd.DataFrame(results)
    path = os.path.join(SAVE_DIR, f'historical_impacts_{market}.csv')
    df.to_csv(path, index=False)
    print(f"\n✅ Sauvegardé : {path}")
    return df

# ============================================================
# VISUALISATION : HEATMAP
# ============================================================
def plot_heatmap(df, market="SMI"):
    sector_cols = [c for c in df.columns if c not in ['event','type','intensity','date']]
    data = df[sector_cols].astype(float)
    data.index = df['event']
    plt.figure(figsize=(14, 8))
    sns.heatmap(data, annot=True, fmt=".1f", cmap="RdYlGn", center=0,
                linewidths=0.5, cbar_kws={'label': 'Impact (%)'})
    plt.title(f'Impact des évènements historiques — {market}', fontsize=14, pad=20)
    plt.xlabel('Secteurs')
    plt.ylabel('Évènements')
    plt.tight_layout()
    path = os.path.join(SAVE_DIR, f'heatmap_{market}.png')
    plt.savefig(path, dpi=150)
    plt.show()
    print(f"✅ Heatmap sauvegardée : {path}")

# ============================================================
# LANCEMENT
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("  SWISS & GLOBAL MARKET STRESS TESTER")
    print("  Phase 1 : Construction base de données historique")
    print("=" * 60)
    df_smi = build_historical_impacts("SMI")
    print("\n", df_smi.to_string())
    plot_heatmap(df_smi, "SMI")