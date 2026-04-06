import re
import numpy as np
from events_db import EVENTS, CATEGORY_LABELS

# ============================================================
# MOTS-CLÉS PAR CATÉGORIE
# ============================================================
KEYWORDS = {
    "war": [
        "war", "guerre", "military", "militaire", "attack", "attaque", "invasion",
        "missile", "bomb", "bombe", "conflict", "conflit", "troops", "troupes",
        "nuclear", "nucléaire", "strike", "frappe", "army", "armée", "soldier",
        "combat", "battle", "bataille", "weapon", "arme", "nato", "otan",
        "terrorism", "terrorisme", "coup", "rebel", "rébellion", "siege",
        "blockade", "blocus", "sanction militaire", "airstrike", "bombardement"
    ],
    "banking": [
        "bank", "banque", "collapse", "effondrement", "bankruptcy", "faillite",
        "credit", "crédit", "lehman", "svb", "silicon valley", "financial crisis",
        "crise financière", "bailout", "sauvetage", "liquidity", "liquidité",
        "default", "défaut", "debt", "dette", "mortgage", "hypothèque",
        "subprime", "hedge fund", "leverage", "levier", "systemic risk",
        "risque systémique", "too big to fail", "fdic", "ubs", "credit suisse"
    ],
    "central_bank": [
        "interest rate", "taux d'intérêt", "fed", "federal reserve", "bns", "snb",
        "ecb", "bce", "rate hike", "hausse des taux", "rate cut", "baisse des taux",
        "quantitative easing", "qe", "monetary policy", "politique monétaire",
        "inflation target", "cible d'inflation", "central bank", "banque centrale",
        "tapering", "pivot", "basis points", "points de base", "yield curve",
        "courbe des taux", "negative rates", "taux négatifs", "tightening"
    ],
    "pandemic": [
        "pandemic", "pandémie", "virus", "epidemic", "épidémie", "covid",
        "coronavirus", "lockdown", "confinement", "quarantine", "quarantaine",
        "vaccine", "vaccin", "outbreak", "foyer", "disease", "maladie",
        "health crisis", "crise sanitaire", "who", "oms", "variant", "mutation",
        "contagion", "transmission", "mortality", "mortalité", "hospital",
        "hôpital", "icu", "réanimation", "ebola", "sars", "flu", "grippe"
    ],
    "political": [
        "election", "élection", "president", "président", "government", "gouvernement",
        "political crisis", "crise politique", "coup d'état", "impeachment",
        "referendum", "référendum", "brexit", "parliament", "parlement",
        "democracy", "démocratie", "populism", "populisme", "protest", "manifestation",
        "revolution", "révolution", "nationalist", "nationaliste", "coalition",
        "minister", "ministre", "policy", "politique", "regulation", "réglementation",
        "trump", "macron", "biden", "modi", "xi jinping"
    ],
    "inflation": [
        "inflation", "cpi", "ipc", "deflation", "déflation", "recession", "récession",
        "gdp", "pib", "unemployment", "chômage", "stagflation", "supply chain",
        "chaîne d'approvisionnement", "energy prices", "prix de l'énergie",
        "oil price", "prix du pétrole", "commodity", "matière première",
        "consumer price", "prix à la consommation", "wage growth", "croissance des salaires",
        "purchasing power", "pouvoir d'achat", "cost of living", "coût de la vie",
        "hyperinflation", "price surge", "hausse des prix"
    ],
    "tech": [
        "ai", "artificial intelligence", "intelligence artificielle", "chatgpt",
        "machine learning", "deep learning", "crypto", "bitcoin", "blockchain",
        "technology", "technologie", "disruption", "innovation", "startup",
        "silicon valley", "nvidia", "openai", "automation", "automatisation",
        "robot", "cybersecurity", "cybersécurité", "data", "cloud", "semiconductor",
        "chip", "puce", "metaverse", "quantum", "quantique", "ftx", "crypto crash",
        "digital", "numérique", "platform", "plateforme"
    ],
    "natural": [
        "earthquake", "séisme", "tremblement de terre", "tsunami", "hurricane",
        "ouragan", "flood", "inondation", "drought", "sécheresse", "wildfire",
        "incendie", "volcano", "volcan", "natural disaster", "catastrophe naturelle",
        "climate", "climat", "storm", "tempête", "cyclone", "typhoon", "typhon",
        "heat wave", "canicule", "nuclear accident", "accident nucléaire",
        "fukushima", "chernobyl", "famine", "disease outbreak", "epidemic"
    ],
    "sanctions": [
        "sanctions", "tariff", "tarif", "trade war", "guerre commerciale",
        "embargo", "export ban", "interdiction d'exportation", "import restriction",
        "restriction d'importation", "trade restriction", "restriction commerciale",
        "wto", "omc", "protectionism", "protectionnisme", "customs", "douanes",
        "trade deal", "accord commercial", "nafta", "usmca", "swift ban",
        "asset freeze", "gel des avoirs", "blacklist", "liste noire"
    ],
}

# ============================================================
# MOTS INVALIDES — filtre les requêtes hors scope
# ============================================================
INVALID_PATTERNS = [
    r"cookie", r"pizza", r"sport", r"foot", r"music", r"film", r"movie",
    r"alien", r"extraterrestrial", r"zombie", r"explode.*earth", r"earth.*explode",
    r"weather.*today", r"meteo", r"recipe", r"recette", r"joke", r"blague",
]

# ============================================================
# FONCTION : CLASSIFIER UN ÉVÈNEMENT LIBRE
# ============================================================
def classify_event(text):
    text_lower = text.lower()

    # Vérifier si hors scope
    for pattern in INVALID_PATTERNS:
        if re.search(pattern, text_lower):
            return None, 0, "out_of_scope"

    # Compter les mots-clés par catégorie
    scores = {}
    for category, keywords in KEYWORDS.items():
        score = 0
        for kw in keywords:
            if kw.lower() in text_lower:
                score += 1
        scores[category] = score

    best_category = max(scores, key=scores.get)
    best_score = scores[best_category]

    if best_score == 0:
        # Aucun mot-clé trouvé — essayer de deviner par contexte général
        return None, 0, "unknown"

    confidence = min(100, best_score * 25)
    return best_category, confidence, "ok"

# ============================================================
# FONCTION : TROUVER LES ÉVÈNEMENTS SIMILAIRES
# ============================================================
def find_similar_events(category, intensity_estimate, top_n=3):
    if category not in EVENTS:
        return []

    events = EVENTS[category]
    similarities = []

    for event in events:
        intensity_diff = abs(event["intensity_score"] - intensity_estimate)
        similarity = max(0, 100 - intensity_diff)
        similarities.append((event, similarity))

    similarities.sort(key=lambda x: x[1], reverse=True)
    return similarities[:top_n]

# ============================================================
# FONCTION : GÉNÉRER UNE PRÉDICTION
# ============================================================
def generate_prediction(text, intensity_input, market_key):
    category, confidence, status = classify_event(text)

    if status == "out_of_scope":
        return {
            "status": "out_of_scope",
            "message": "This event does not appear to have a direct financial market impact. Please describe a geopolitical, economic, or financial event.",
            "message_fr": "Cet évènement ne semble pas avoir d'impact direct sur les marchés financiers. Décrivez un évènement géopolitique, économique ou financier.",
        }

    if status == "unknown" or category is None:
        return {
            "status": "unknown",
            "message": "Unable to classify this event. Try adding more context (e.g. 'military conflict', 'banking crisis', 'interest rate decision').",
            "message_fr": "Impossible de classifier cet évènement. Ajoutez plus de contexte (ex: 'conflit militaire', 'crise bancaire', 'décision de taux').",
        }

    similar_events = find_similar_events(category, intensity_input, top_n=3)
    if not similar_events:
        return {"status": "no_data", "message": "No similar historical events found."}

    impact_key = f"{market_key}_impact"
    predicted_impacts = {}
    total_weight = 0

    for event, similarity in similar_events:
        weight = similarity / 100
        impacts = event.get(impact_key, {})
        for sector, value in impacts.items():
            if sector not in predicted_impacts:
                predicted_impacts[sector] = 0
            predicted_impacts[sector] += value * weight
            total_weight += weight

    if total_weight > 0:
        for sector in predicted_impacts:
            predicted_impacts[sector] = round(predicted_impacts[sector] / len(similar_events), 2)

    # Ajuster par intensité
    intensity_factor = intensity_input / 50
    predicted_impacts = {k: round(v * intensity_factor, 2) for k, v in predicted_impacts.items()}

    return {
        "status": "ok",
        "category": category,
        "category_label": CATEGORY_LABELS.get(category, category),
        "confidence": confidence,
        "intensity": intensity_input,
        "predicted_impacts": predicted_impacts,
        "similar_events": similar_events,
        "market": market_key,
    }

# ============================================================
# FONCTION : GÉNÉRER EXPLICATION
# ============================================================
def generate_explanation(result, lang="EN"):
    if result["status"] != "ok":
        return ""

    cat_label = result["category_label"]
    similar = result["similar_events"]
    impacts = result["predicted_impacts"]

    if not impacts:
        return ""

    best = max(impacts, key=impacts.get)
    worst = min(impacts, key=impacts.get)
    sign_b = "+" if impacts[best] >= 0 else ""
    sign_w = "+" if impacts[worst] >= 0 else ""

    similar_names = [e["name"] for e, _ in similar[:2]]

    if lang == "EN":
        return (
            f"This event has been classified as a **{cat_label}** scenario "
            f"with a confidence of **{result['confidence']}%**. "
            f"Based on similar historical events — particularly **{' and '.join(similar_names)}** — "
            f"the model predicts **{best}** to be the most resilient sector ({sign_b}{impacts[best]:.1f}%) "
            f"and **{worst}** to be the most exposed ({sign_w}{impacts[worst]:.1f}%)."
        )
    else:
        return (
            f"Cet évènement a été classifié comme un scénario de type **{cat_label}** "
            f"avec une confiance de **{result['confidence']}%**. "
            f"En se basant sur des évènements similaires — notamment **{' et '.join(similar_names)}** — "
            f"le modèle prédit que **{best}** sera le secteur le plus résilient ({sign_b}{impacts[best]:.1f}%) "
            f"et **{worst}** le plus exposé ({sign_w}{impacts[worst]:.1f}%)."
        )