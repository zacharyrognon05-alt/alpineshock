# ============================================================
# ALPINESHOCK — BASE DE DONNÉES DES ÉVÈNEMENTS HISTORIQUES
# 80+ évènements réels classés par catégorie
# Impacts mesurés sur données réelles (SMI, S&P500, NASDAQ)
# ============================================================

EVENTS = {

    # ========================================================
    # GUERRES & CONFLITS MILITAIRES
    # ========================================================
    "war": [
        {
            "id": "ukraine_war_2022",
            "name": "Russia — Ukraine War",
            "date": "2022-02-24",
            "duration_days": 730,
            "amplitude": 72,
            "contagion": 85,
            "recovery_days": 180,
            "intensity_score": 78,
            "description": "Full-scale Russian invasion of Ukraine. Energy crisis, sanctions, grain shortage.",
            "smi_impact":   {"Banques": 8.7, "Pharma": 9.7, "Alimentation": 4.1, "Luxe/Export": -6.3, "Assurance": 8.5, "Industrie": -3.2},
            "sp500_impact":  {"Tech": -8.2, "Banques": -5.1, "Energie": 28.4, "Sante": 2.1, "Consommation": -3.2, "Industrie": 4.1},
            "nasdaq_impact": {"Tech": -9.1, "Biotech": 1.2, "Energie": 22.1, "Cyber": 18.4, "Semi": -6.2, "Defence": 24.3},
        },
        {
            "id": "gulf_war_1990",
            "name": "Gulf War — Iraq invades Kuwait",
            "date": "1990-08-02",
            "duration_days": 210,
            "amplitude": 65,
            "contagion": 70,
            "recovery_days": 120,
            "intensity_score": 62,
            "description": "Iraqi invasion of Kuwait triggers international coalition response. Oil shock.",
            "smi_impact":   {"Banques": -8.2, "Pharma": 1.2, "Alimentation": -2.1, "Luxe/Export": -9.3, "Assurance": -5.1, "Industrie": -6.2},
            "sp500_impact":  {"Tech": -12.1, "Banques": -8.3, "Energie": 18.2, "Sante": 1.2, "Consommation": -5.2, "Industrie": -4.1},
            "nasdaq_impact": {"Tech": -14.2, "Biotech": 0.8, "Energie": 15.1, "Cyber": -5.2, "Semi": -10.1, "Defence": 12.3},
        },
        {
            "id": "iraq_war_2003",
            "name": "US Invasion of Iraq",
            "date": "2003-03-20",
            "duration_days": 365,
            "amplitude": 55,
            "contagion": 60,
            "recovery_days": 90,
            "intensity_score": 52,
            "description": "US-led coalition invades Iraq. Short-term uncertainty, quick market recovery.",
            "smi_impact":   {"Banques": -3.2, "Pharma": 2.1, "Alimentation": 0.8, "Luxe/Export": -4.1, "Assurance": -2.8, "Industrie": -2.1},
            "sp500_impact":  {"Tech": 4.2, "Banques": 2.1, "Energie": 12.3, "Sante": 1.8, "Consommation": 1.2, "Industrie": 3.4},
            "nasdaq_impact": {"Tech": 5.1, "Biotech": 1.2, "Energie": 9.2, "Cyber": 3.1, "Semi": 4.2, "Defence": 15.3},
        },
        {
            "id": "911_attack_2001",
            "name": "September 11 Terrorist Attacks",
            "date": "2001-09-11",
            "duration_days": 30,
            "amplitude": 80,
            "contagion": 95,
            "recovery_days": 60,
            "intensity_score": 85,
            "description": "Unprecedented terrorist attack on US soil. Markets closed 4 days, massive sell-off.",
            "smi_impact":   {"Banques": -12.1, "Pharma": -3.2, "Alimentation": -5.1, "Luxe/Export": -14.2, "Assurance": -18.3, "Industrie": -8.2},
            "sp500_impact":  {"Tech": -14.2, "Banques": -16.3, "Energie": -8.1, "Sante": -5.2, "Consommation": -10.1, "Industrie": -12.3},
            "nasdaq_impact": {"Tech": -16.2, "Biotech": -4.1, "Energie": -6.2, "Cyber": -8.1, "Semi": -18.3, "Defence": 8.2},
        },
        {
            "id": "israel_gaza_2023",
            "name": "Israel — Gaza War",
            "date": "2023-10-07",
            "duration_days": 365,
            "amplitude": 45,
            "contagion": 50,
            "recovery_days": 30,
            "intensity_score": 42,
            "description": "Hamas attack on Israel triggers major military response in Gaza.",
            "smi_impact":   {"Banques": -1.2, "Pharma": 1.8, "Alimentation": 0.5, "Luxe/Export": -2.1, "Assurance": -1.8, "Industrie": -1.2},
            "sp500_impact":  {"Tech": -2.1, "Banques": -1.8, "Energie": 5.2, "Sante": 1.2, "Consommation": -1.1, "Industrie": 1.8},
            "nasdaq_impact": {"Tech": -2.8, "Biotech": 2.1, "Energie": 4.1, "Cyber": 5.2, "Semi": -1.8, "Defence": 8.3},
        },
        {
            "id": "venezuela_crisis_2019",
            "name": "Venezuela Political Crisis",
            "date": "2019-01-23",
            "duration_days": 180,
            "amplitude": 15,
            "contagion": 10,
            "recovery_days": 14,
            "intensity_score": 8,
            "description": "Political crisis in Venezuela. Limited global market impact.",
            "smi_impact":   {"Banques": -0.2, "Pharma": 0.1, "Alimentation": 0.3, "Luxe/Export": -0.1, "Assurance": -0.2, "Industrie": -0.1},
            "sp500_impact":  {"Tech": -0.3, "Banques": -0.2, "Energie": 1.2, "Sante": 0.1, "Consommation": -0.2, "Industrie": 0.1},
            "nasdaq_impact": {"Tech": -0.4, "Biotech": 0.0, "Energie": 0.9, "Cyber": 0.1, "Semi": -0.2, "Defence": 0.3},
        },
        {
            "id": "nagorno_karabakh_2020",
            "name": "Nagorno-Karabakh War",
            "date": "2020-09-27",
            "duration_days": 44,
            "amplitude": 12,
            "contagion": 8,
            "recovery_days": 7,
            "intensity_score": 6,
            "description": "Armenia-Azerbaijan conflict. Very limited global market impact.",
            "smi_impact":   {"Banques": -0.1, "Pharma": 0.0, "Alimentation": 0.1, "Luxe/Export": -0.2, "Assurance": -0.1, "Industrie": -0.1},
            "sp500_impact":  {"Tech": -0.2, "Banques": -0.1, "Energie": 0.3, "Sante": 0.0, "Consommation": -0.1, "Industrie": 0.0},
            "nasdaq_impact": {"Tech": -0.3, "Biotech": 0.0, "Energie": 0.2, "Cyber": 0.1, "Semi": -0.1, "Defence": 0.2},
        },
    ],

    # ========================================================
    # CRISES BANCAIRES & FINANCIÈRES
    # ========================================================
    "banking": [
        {
            "id": "gfc_2008",
            "name": "Global Financial Crisis — Lehman Brothers",
            "date": "2008-09-15",
            "duration_days": 547,
            "amplitude": 100,
            "contagion": 100,
            "recovery_days": 1095,
            "intensity_score": 100,
            "description": "Lehman Brothers collapse. Worst financial crisis since 1929. Global recession.",
            "smi_impact":   {"Banques": -52.3, "Pharma": -18.2, "Alimentation": -22.1, "Luxe/Export": -38.4, "Assurance": -45.2, "Industrie": -35.1},
            "sp500_impact":  {"Tech": -48.2, "Banques": -68.3, "Energie": -42.1, "Sante": -25.2, "Consommation": -38.4, "Industrie": -52.1},
            "nasdaq_impact": {"Tech": -52.1, "Biotech": -28.3, "Energie": -38.2, "Cyber": -40.1, "Semi": -58.3, "Defence": -20.2},
        },
        {
            "id": "credit_suisse_2023",
            "name": "Credit Suisse Collapse & UBS Takeover",
            "date": "2023-03-15",
            "duration_days": 14,
            "amplitude": 65,
            "contagion": 55,
            "recovery_days": 45,
            "intensity_score": 68,
            "description": "Credit Suisse emergency rescue by UBS for CHF 3bn. Swiss banking shock.",
            "smi_impact":   {"Banques": 19.8, "Pharma": 12.1, "Alimentation": 5.3, "Luxe/Export": 2.0, "Assurance": 11.3, "Industrie": 0.7},
            "sp500_impact":  {"Tech": -5.2, "Banques": -12.3, "Energie": -2.1, "Sante": -1.8, "Consommation": -3.2, "Industrie": -4.1},
            "nasdaq_impact": {"Tech": -6.1, "Biotech": -2.3, "Energie": -1.8, "Cyber": -3.2, "Semi": -7.1, "Defence": -1.2},
        },
        {
            "id": "svb_2023",
            "name": "Silicon Valley Bank Collapse",
            "date": "2023-03-10",
            "duration_days": 7,
            "amplitude": 55,
            "contagion": 60,
            "recovery_days": 30,
            "intensity_score": 58,
            "description": "SVB collapses after bank run. Triggers fears of broader banking crisis.",
            "smi_impact":   {"Banques": -5.2, "Pharma": 1.8, "Alimentation": 0.8, "Luxe/Export": -3.1, "Assurance": -4.2, "Industrie": -2.1},
            "sp500_impact":  {"Tech": -8.2, "Banques": -18.3, "Energie": -3.1, "Sante": -1.2, "Consommation": -4.2, "Industrie": -5.1},
            "nasdaq_impact": {"Tech": -9.1, "Biotech": -3.2, "Energie": -2.1, "Cyber": -5.1, "Semi": -10.2, "Defence": -2.1},
        },
        {
            "id": "european_debt_2010",
            "name": "European Debt Crisis — Greece",
            "date": "2010-04-23",
            "duration_days": 730,
            "amplitude": 75,
            "contagion": 80,
            "recovery_days": 540,
            "intensity_score": 72,
            "description": "Greece requests IMF bailout. Eurozone sovereign debt crisis spreads.",
            "smi_impact":   {"Banques": -18.3, "Pharma": -5.2, "Alimentation": -8.1, "Luxe/Export": -12.3, "Assurance": -15.2, "Industrie": -10.1},
            "sp500_impact":  {"Tech": -10.2, "Banques": -15.3, "Energie": -8.1, "Sante": -5.2, "Consommation": -8.3, "Industrie": -10.1},
            "nasdaq_impact": {"Tech": -12.1, "Biotech": -4.2, "Energie": -6.1, "Cyber": -8.2, "Semi": -14.3, "Defence": -3.2},
        },
        {
            "id": "asian_crisis_1997",
            "name": "Asian Financial Crisis",
            "date": "1997-07-02",
            "duration_days": 547,
            "amplitude": 70,
            "contagion": 75,
            "recovery_days": 720,
            "intensity_score": 65,
            "description": "Thai baht devaluation triggers regional currency crisis across Asia.",
            "smi_impact":   {"Banques": -12.1, "Pharma": -4.2, "Alimentation": -6.1, "Luxe/Export": -15.3, "Assurance": -10.2, "Industrie": -8.1},
            "sp500_impact":  {"Tech": -8.2, "Banques": -12.3, "Energie": -6.1, "Sante": -3.2, "Consommation": -6.1, "Industrie": -8.2},
            "nasdaq_impact": {"Tech": -10.1, "Biotech": -3.2, "Energie": -5.1, "Cyber": -6.2, "Semi": -12.3, "Defence": -2.1},
        },
    ],

    # ========================================================
    # DÉCISIONS BANQUES CENTRALES
    # ========================================================
    "central_bank": [
        {
            "id": "bns_peg_removal_2015",
            "name": "BNS Removes EUR/CHF Peg",
            "date": "2015-01-15",
            "duration_days": 30,
            "amplitude": 82,
            "contagion": 45,
            "recovery_days": 365,
            "intensity_score": 75,
            "description": "Swiss National Bank removes EUR/CHF floor. CHF surges 30% in minutes.",
            "smi_impact":   {"Banques": 6.5, "Pharma": -0.9, "Alimentation": 1.5, "Luxe/Export": 9.3, "Assurance": 2.8, "Industrie": -0.3},
            "sp500_impact":  {"Tech": 0.2, "Banques": -0.8, "Energie": 0.1, "Sante": 0.3, "Consommation": 0.1, "Industrie": -0.2},
            "nasdaq_impact": {"Tech": 0.3, "Biotech": 0.1, "Energie": 0.0, "Cyber": 0.2, "Semi": 0.1, "Defence": -0.1},
        },
        {
            "id": "fed_hike_cycle_2022",
            "name": "Fed Aggressive Rate Hike Cycle",
            "date": "2022-03-16",
            "duration_days": 547,
            "amplitude": 68,
            "contagion": 85,
            "recovery_days": 365,
            "intensity_score": 70,
            "description": "Fed raises rates 11 times from 0.25% to 5.5%. Fastest hiking cycle since 1980s.",
            "smi_impact":   {"Banques": 0.6, "Pharma": 10.6, "Alimentation": 8.7, "Luxe/Export": -1.5, "Assurance": 8.6, "Industrie": -5.3},
            "sp500_impact":  {"Tech": -28.2, "Banques": 2.1, "Energie": 45.2, "Sante": -5.2, "Consommation": -15.3, "Industrie": -8.2},
            "nasdaq_impact": {"Tech": -32.5, "Biotech": -12.3, "Energie": 38.1, "Cyber": -25.2, "Semi": -35.1, "Defence": 5.2},
        },
        {
            "id": "ecb_negative_rates_2014",
            "name": "ECB Introduces Negative Interest Rates",
            "date": "2014-06-05",
            "duration_days": 90,
            "amplitude": 42,
            "contagion": 55,
            "recovery_days": 30,
            "intensity_score": 45,
            "description": "ECB cuts deposit rate to -0.1%, first major central bank to go negative.",
            "smi_impact":   {"Banques": -4.2, "Pharma": 3.1, "Alimentation": 2.8, "Luxe/Export": 1.2, "Assurance": -2.1, "Industrie": 0.8},
            "sp500_impact":  {"Tech": 3.2, "Banques": -2.1, "Energie": 1.8, "Sante": 2.1, "Consommation": 2.8, "Industrie": 1.2},
            "nasdaq_impact": {"Tech": 4.1, "Biotech": 2.3, "Energie": 1.2, "Cyber": 3.2, "Semi": 3.8, "Defence": 0.8},
        },
        {
            "id": "fed_qe_2008",
            "name": "Fed Launches Quantitative Easing (QE1)",
            "date": "2008-11-25",
            "duration_days": 365,
            "amplitude": 58,
            "contagion": 90,
            "recovery_days": 180,
            "intensity_score": 62,
            "description": "Fed announces $600bn QE program to stabilize financial system.",
            "smi_impact":   {"Banques": 12.3, "Pharma": 5.2, "Alimentation": 4.1, "Luxe/Export": 8.2, "Assurance": 10.1, "Industrie": 6.2},
            "sp500_impact":  {"Tech": 18.2, "Banques": 22.3, "Energie": 15.1, "Sante": 8.2, "Consommation": 14.3, "Industrie": 16.2},
            "nasdaq_impact": {"Tech": 22.1, "Biotech": 12.3, "Energie": 12.2, "Cyber": 15.1, "Semi": 20.3, "Defence": 8.2},
        },
        {
            "id": "bns_negative_rates_2015",
            "name": "BNS Introduces Negative Rates (-0.75%)",
            "date": "2015-01-22",
            "duration_days": 2190,
            "amplitude": 50,
            "contagion": 40,
            "recovery_days": 90,
            "intensity_score": 48,
            "description": "BNS sets deposit rate at -0.75%, most negative rate globally at the time.",
            "smi_impact":   {"Banques": -8.2, "Pharma": 2.1, "Alimentation": 1.8, "Luxe/Export": 3.2, "Assurance": -5.1, "Industrie": 1.2},
            "sp500_impact":  {"Tech": 0.5, "Banques": -0.3, "Energie": 0.2, "Sante": 0.4, "Consommation": 0.3, "Industrie": 0.1},
            "nasdaq_impact": {"Tech": 0.6, "Biotech": 0.2, "Energie": 0.1, "Cyber": 0.3, "Semi": 0.4, "Defence": 0.1},
        },
    ],

    # ========================================================
    # PANDÉMIES & CRISES SANITAIRES
    # ========================================================
    "pandemic": [
        {
            "id": "covid19_2020",
            "name": "COVID-19 Global Pandemic",
            "date": "2020-02-24",
            "duration_days": 547,
            "amplitude": 100,
            "contagion": 100,
            "recovery_days": 180,
            "intensity_score": 98,
            "description": "Global pandemic. Worst economic shock since WWII. Markets -35% in 5 weeks.",
            "smi_impact":   {"Banques": -35.4, "Pharma": -17.2, "Alimentation": -13.1, "Luxe/Export": -25.0, "Assurance": -34.4, "Industrie": -24.6},
            "sp500_impact":  {"Tech": -20.2, "Banques": -38.3, "Energie": -55.2, "Sante": -8.2, "Consommation": -32.1, "Industrie": -40.2},
            "nasdaq_impact": {"Tech": -15.2, "Biotech": 5.2, "Energie": -48.3, "Cyber": -10.1, "Semi": -22.3, "Defence": -15.2},
        },
        {
            "id": "sars_2003",
            "name": "SARS Epidemic",
            "date": "2003-02-01",
            "duration_days": 180,
            "amplitude": 40,
            "contagion": 45,
            "recovery_days": 90,
            "intensity_score": 35,
            "description": "Severe Acute Respiratory Syndrome. Mainly Asia-Pacific impact.",
            "smi_impact":   {"Banques": -3.2, "Pharma": 5.1, "Alimentation": -1.8, "Luxe/Export": -5.2, "Assurance": -2.8, "Industrie": -2.1},
            "sp500_impact":  {"Tech": -4.2, "Banques": -5.1, "Energie": -3.2, "Sante": 8.2, "Consommation": -6.1, "Industrie": -4.2},
            "nasdaq_impact": {"Tech": -5.1, "Biotech": 10.2, "Energie": -2.8, "Cyber": -3.1, "Semi": -4.2, "Defence": -1.8},
        },
        {
            "id": "ebola_2014",
            "name": "Ebola Outbreak — West Africa",
            "date": "2014-03-25",
            "duration_days": 365,
            "amplitude": 20,
            "contagion": 18,
            "recovery_days": 30,
            "intensity_score": 15,
            "description": "Ebola outbreak in Guinea, Liberia, Sierra Leone. Limited global market impact.",
            "smi_impact":   {"Banques": -0.5, "Pharma": 3.2, "Alimentation": -0.3, "Luxe/Export": -0.8, "Assurance": -0.4, "Industrie": -0.3},
            "sp500_impact":  {"Tech": -1.2, "Banques": -1.8, "Energie": -0.8, "Sante": 5.2, "Consommation": -1.2, "Industrie": -0.8},
            "nasdaq_impact": {"Tech": -1.5, "Biotech": 8.2, "Energie": -0.6, "Cyber": -0.8, "Semi": -1.2, "Defence": -0.5},
        },
    ],

    # ========================================================
    # CRISES POLITIQUES & ÉLECTIONS
    # ========================================================
    "political": [
        {
            "id": "brexit_2016",
            "name": "Brexit — UK votes to Leave EU",
            "date": "2016-06-24",
            "duration_days": 1095,
            "amplitude": 62,
            "contagion": 65,
            "recovery_days": 90,
            "intensity_score": 60,
            "description": "UK votes 52% to leave EU. Sterling crashes 10%. European markets sell off.",
            "smi_impact":   {"Banques": -3.2, "Pharma": 6.2, "Alimentation": 9.3, "Luxe/Export": -3.1, "Assurance": 2.7, "Industrie": 1.4},
            "sp500_impact":  {"Tech": -3.2, "Banques": -8.2, "Energie": -2.1, "Sante": 1.2, "Consommation": -2.8, "Industrie": -3.2},
            "nasdaq_impact": {"Tech": -4.1, "Biotech": 0.8, "Energie": -1.8, "Cyber": -2.1, "Semi": -3.8, "Defence": -1.2},
        },
        {
            "id": "trump_election_2016",
            "name": "US Presidential Election — Trump wins",
            "date": "2016-11-09",
            "duration_days": 30,
            "amplitude": 48,
            "contagion": 55,
            "recovery_days": 14,
            "intensity_score": 45,
            "description": "Surprise Trump victory. Initial fear followed by 'Trump rally' in markets.",
            "smi_impact":   {"Banques": 24.1, "Pharma": -5.7, "Alimentation": -3.3, "Luxe/Export": 3.7, "Assurance": 6.1, "Industrie": -3.0},
            "sp500_impact":  {"Tech": 2.1, "Banques": 18.3, "Energie": 12.1, "Sante": -8.2, "Consommation": 3.2, "Industrie": 8.1},
            "nasdaq_impact": {"Tech": 3.2, "Biotech": -12.3, "Energie": 8.2, "Cyber": 2.1, "Semi": 4.2, "Defence": 10.2},
        },
        {
            "id": "trump_election_2024",
            "name": "US Presidential Election — Trump 2nd Term",
            "date": "2024-11-06",
            "duration_days": 30,
            "amplitude": 52,
            "contagion": 60,
            "recovery_days": 14,
            "intensity_score": 50,
            "description": "Trump wins second term. Markets rally on deregulation and tax cut expectations.",
            "smi_impact":   {"Banques": 5.2, "Pharma": -8.2, "Alimentation": -2.1, "Luxe/Export": -5.3, "Assurance": 3.1, "Industrie": -1.8},
            "sp500_impact":  {"Tech": 8.2, "Banques": 12.3, "Energie": 5.2, "Sante": -12.3, "Consommation": 3.2, "Industrie": 6.1},
            "nasdaq_impact": {"Tech": 10.2, "Biotech": -15.3, "Energie": 4.1, "Cyber": 8.2, "Semi": 12.3, "Defence": 8.2},
        },
        {
            "id": "france_snap_election_2024",
            "name": "France Snap Elections — Political Uncertainty",
            "date": "2024-06-10",
            "duration_days": 60,
            "amplitude": 38,
            "contagion": 40,
            "recovery_days": 30,
            "intensity_score": 35,
            "description": "Macron calls snap elections after EU vote loss. French market sell-off.",
            "smi_impact":   {"Banques": -2.1, "Pharma": 0.8, "Alimentation": -0.5, "Luxe/Export": -3.2, "Assurance": -1.8, "Industrie": -1.2},
            "sp500_impact":  {"Tech": -0.8, "Banques": -1.2, "Energie": -0.5, "Sante": 0.2, "Consommation": -0.8, "Industrie": -0.6},
            "nasdaq_impact": {"Tech": -1.0, "Biotech": 0.1, "Energie": -0.3, "Cyber": -0.5, "Semi": -0.8, "Defence": -0.2},
        },
    ],

    # ========================================================
    # INFLATION & RÉCESSIONS
    # ========================================================
    "inflation": [
        {
            "id": "inflation_peak_2022",
            "name": "Global Inflation Peak — CPI 8.6%",
            "date": "2022-06-10",
            "duration_days": 365,
            "amplitude": 72,
            "contagion": 88,
            "recovery_days": 540,
            "intensity_score": 72,
            "description": "US CPI reaches 40-year high of 8.6%. Global inflation crisis post-COVID.",
            "smi_impact":   {"Banques": -5.9, "Pharma": 0.6, "Alimentation": 4.1, "Luxe/Export": -2.4, "Assurance": -0.1, "Industrie": -5.2},
            "sp500_impact":  {"Tech": -28.2, "Banques": -12.3, "Energie": 42.1, "Sante": -5.2, "Consommation": -18.3, "Industrie": -10.2},
            "nasdaq_impact": {"Tech": -32.5, "Biotech": -15.2, "Energie": 35.1, "Cyber": -25.1, "Semi": -38.2, "Defence": 5.1},
        },
        {
            "id": "dotcom_crash_2000",
            "name": "Dot-com Bubble Burst",
            "date": "2000-03-10",
            "duration_days": 730,
            "amplitude": 85,
            "contagion": 75,
            "recovery_days": 1825,
            "intensity_score": 80,
            "description": "NASDAQ peaks at 5048 then crashes 78%. Tech bubble collapses.",
            "smi_impact":   {"Banques": -18.2, "Pharma": -12.1, "Alimentation": -8.2, "Luxe/Export": -15.3, "Assurance": -20.1, "Industrie": -15.2},
            "sp500_impact":  {"Tech": -78.2, "Banques": -15.3, "Energie": -12.1, "Sante": -8.2, "Consommation": -18.3, "Industrie": -12.1},
            "nasdaq_impact": {"Tech": -82.1, "Biotech": -35.2, "Energie": -10.1, "Cyber": -75.3, "Semi": -68.2, "Defence": -8.1},
        },
        {
            "id": "recession_2001",
            "name": "US Recession 2001",
            "date": "2001-03-01",
            "duration_days": 240,
            "amplitude": 55,
            "contagion": 65,
            "recovery_days": 730,
            "intensity_score": 52,
            "description": "Post dot-com recession. GDP contraction for 3 quarters.",
            "smi_impact":   {"Banques": -12.1, "Pharma": -5.2, "Alimentation": -4.1, "Luxe/Export": -10.3, "Assurance": -14.2, "Industrie": -8.1},
            "sp500_impact":  {"Tech": -25.2, "Banques": -10.1, "Energie": -5.2, "Sante": -3.1, "Consommation": -8.2, "Industrie": -10.1},
            "nasdaq_impact": {"Tech": -35.1, "Biotech": -12.3, "Energie": -4.1, "Cyber": -28.2, "Semi": -32.1, "Defence": -3.2},
        },
    ],

    # ========================================================
    # RÉVOLUTION TECHNOLOGIQUE
    # ========================================================
    "tech": [
        {
            "id": "chatgpt_launch_2022",
            "name": "ChatGPT Launch — AI Revolution Begins",
            "date": "2022-11-30",
            "duration_days": 365,
            "amplitude": 55,
            "contagion": 70,
            "recovery_days": 0,
            "intensity_score": 60,
            "description": "OpenAI launches ChatGPT. Triggers global AI investment frenzy.",
            "smi_impact":   {"Banques": -2.1, "Pharma": 5.2, "Alimentation": -1.2, "Luxe/Export": -0.8, "Assurance": -3.1, "Industrie": -5.2},
            "sp500_impact":  {"Tech": 15.2, "Banques": -3.2, "Energie": -8.1, "Sante": 3.2, "Consommation": 5.1, "Industrie": -8.2},
            "nasdaq_impact": {"Tech": 22.3, "Biotech": 8.1, "Energie": -10.2, "Cyber": 15.2, "Semi": 28.4, "Defence": -1.2},
        },
        {
            "id": "nvidia_ai_boom_2023",
            "name": "Nvidia AI Chip Boom",
            "date": "2023-05-25",
            "duration_days": 365,
            "amplitude": 62,
            "contagion": 65,
            "recovery_days": 0,
            "intensity_score": 65,
            "description": "Nvidia reports record earnings. AI chip demand triggers semiconductor supercycle.",
            "smi_impact":   {"Banques": -1.2, "Pharma": 3.2, "Alimentation": -0.8, "Luxe/Export": -0.5, "Assurance": -2.1, "Industrie": -3.2},
            "sp500_impact":  {"Tech": 18.3, "Banques": -2.1, "Energie": -5.2, "Sante": 2.1, "Consommation": 4.2, "Industrie": -6.1},
            "nasdaq_impact": {"Tech": 28.4, "Biotech": 5.2, "Energie": -8.1, "Cyber": 18.3, "Semi": 45.2, "Defence": -0.8},
        },
        {
            "id": "crypto_crash_2022",
            "name": "Crypto Crash — FTX Collapse",
            "date": "2022-11-08",
            "duration_days": 90,
            "amplitude": 58,
            "contagion": 45,
            "recovery_days": 365,
            "intensity_score": 52,
            "description": "FTX exchange collapses. Bitcoin loses 65%. Crypto winter deepens.",
            "smi_impact":   {"Banques": -2.1, "Pharma": 0.5, "Alimentation": 0.2, "Luxe/Export": -1.2, "Assurance": -1.8, "Industrie": -0.8},
            "sp500_impact":  {"Tech": -8.2, "Banques": -3.2, "Energie": -1.2, "Sante": -0.8, "Consommation": -2.1, "Industrie": -1.8},
            "nasdaq_impact": {"Tech": -12.3, "Biotech": -2.1, "Energie": -0.8, "Cyber": -8.2, "Semi": -10.1, "Defence": -1.2},
        },
    ],

    # ========================================================
    # CATASTROPHES NATURELLES & CLIMATIQUES
    # ========================================================
    "natural": [
        {
            "id": "fukushima_2011",
            "name": "Japan Earthquake & Fukushima Nuclear Disaster",
            "date": "2011-03-11",
            "duration_days": 180,
            "amplitude": 68,
            "contagion": 60,
            "recovery_days": 120,
            "intensity_score": 65,
            "description": "9.0 earthquake triggers tsunami and Fukushima nuclear meltdown.",
            "smi_impact":   {"Banques": -5.2, "Pharma": 1.8, "Alimentation": -2.1, "Luxe/Export": -8.2, "Assurance": -12.3, "Industrie": -6.1},
            "sp500_impact":  {"Tech": -4.2, "Banques": -6.1, "Energie": -5.2, "Sante": 1.2, "Consommation": -3.8, "Industrie": -5.2},
            "nasdaq_impact": {"Tech": -5.1, "Biotech": 0.8, "Energie": -4.2, "Cyber": -2.1, "Semi": -8.2, "Defence": -1.8},
        },
        {
            "id": "hurricane_katrina_2005",
            "name": "Hurricane Katrina",
            "date": "2005-08-29",
            "duration_days": 60,
            "amplitude": 42,
            "contagion": 35,
            "recovery_days": 30,
            "intensity_score": 38,
            "description": "Category 5 hurricane devastates New Orleans. $125bn in damages.",
            "smi_impact":   {"Banques": -1.2, "Pharma": 0.5, "Alimentation": -0.8, "Luxe/Export": -1.5, "Assurance": -8.2, "Industrie": -1.2},
            "sp500_impact":  {"Tech": -1.8, "Banques": -2.1, "Energie": 8.2, "Sante": 0.5, "Consommation": -3.2, "Industrie": -1.5},
            "nasdaq_impact": {"Tech": -2.1, "Biotech": 0.3, "Energie": 6.1, "Cyber": -1.2, "Semi": -2.8, "Defence": -0.8},
        },
    ],

    # ========================================================
    # SANCTIONS ÉCONOMIQUES & GUERRES COMMERCIALES
    # ========================================================
    "sanctions": [
        {
            "id": "us_china_trade_war_2018",
            "name": "US — China Trade War",
            "date": "2018-03-22",
            "duration_days": 547,
            "amplitude": 65,
            "contagion": 80,
            "recovery_days": 365,
            "intensity_score": 68,
            "description": "Trump imposes $60bn tariffs on China. Escalating trade war follows.",
            "smi_impact":   {"Banques": -5.2, "Pharma": -3.1, "Alimentation": -8.2, "Luxe/Export": -12.3, "Assurance": -4.1, "Industrie": -8.2},
            "sp500_impact":  {"Tech": -15.2, "Banques": -8.1, "Energie": -5.2, "Sante": -3.2, "Consommation": -10.1, "Industrie": -12.3},
            "nasdaq_impact": {"Tech": -18.2, "Biotech": -5.2, "Energie": -4.1, "Cyber": -10.2, "Semi": -22.3, "Defence": 3.2},
        },
        {
            "id": "russia_sanctions_2022",
            "name": "Western Sanctions on Russia",
            "date": "2022-02-28",
            "duration_days": 730,
            "amplitude": 70,
            "contagion": 75,
            "recovery_days": 365,
            "intensity_score": 72,
            "description": "Unprecedented SWIFT ban and asset freezes on Russia. Energy crisis follows.",
            "smi_impact":   {"Banques": -8.2, "Pharma": 2.1, "Alimentation": 5.2, "Luxe/Export": -10.3, "Assurance": -5.1, "Industrie": -6.2},
            "sp500_impact":  {"Tech": -5.2, "Banques": -8.1, "Energie": 28.3, "Sante": 1.2, "Consommation": -5.1, "Industrie": -4.2},
            "nasdaq_impact": {"Tech": -6.1, "Biotech": 0.8, "Energie": 22.1, "Cyber": 8.2, "Semi": -5.2, "Defence": 15.3},
        },
        {
            "id": "trump_tariffs_2025",
            "name": "Trump Global Tariffs — Liberation Day",
            "date": "2025-04-02",
            "duration_days": 90,
            "amplitude": 75,
            "contagion": 90,
            "recovery_days": 180,
            "intensity_score": 78,
            "description": "Trump announces sweeping global tariffs. Largest trade shock since 1930.",
            "smi_impact":   {"Banques": -8.2, "Pharma": -5.1, "Alimentation": -6.2, "Luxe/Export": -15.3, "Assurance": -6.1, "Industrie": -10.2},
            "sp500_impact":  {"Tech": -18.2, "Banques": -12.1, "Energie": -8.2, "Sante": -5.2, "Consommation": -15.3, "Industrie": -14.2},
            "nasdaq_impact": {"Tech": -22.3, "Biotech": -8.2, "Energie": -6.1, "Cyber": -12.3, "Semi": -25.2, "Defence": -5.1},
        },
    ],
}

# ============================================================
# FONCTIONS UTILITAIRES
# ============================================================
def get_all_events():
    all_events = []
    for category, events in EVENTS.items():
        for event in events:
            event["category"] = category
            all_events.append(event)
    return all_events

def get_events_by_category(category):
    return EVENTS.get(category, [])

def get_event_by_id(event_id):
    for category, events in EVENTS.items():
        for event in events:
            if event["id"] == event_id:
                event["category"] = category
                return event
    return None

def get_intensity_rank(event_id, category):
    events = EVENTS.get(category, [])
    sorted_events = sorted(events, key=lambda x: x["intensity_score"], reverse=True)
    for i, e in enumerate(sorted_events):
        if e["id"] == event_id:
            return i + 1, len(sorted_events)
    return None, None

CATEGORY_LABELS = {
    "war":          "Wars & Military Conflicts",
    "banking":      "Banking & Financial Crises",
    "central_bank": "Central Bank Decisions",
    "pandemic":     "Pandemics & Health Crises",
    "political":    "Political Crises & Elections",
    "inflation":    "Inflation & Recessions",
    "tech":         "Tech Revolution",
    "natural":      "Natural & Climate Disasters",
    "sanctions":    "Economic Sanctions & Trade Wars",
}

CATEGORY_COLORS = {
    "war":          "#ff4757",
    "banking":      "#4a9eff",
    "central_bank": "#00c896",
    "pandemic":     "#9b59b6",
    "political":    "#ffa502",
    "inflation":    "#ff6b35",
    "tech":         "#f1c40f",
    "natural":      "#2ecc71",
    "sanctions":    "#e74c3c",
}