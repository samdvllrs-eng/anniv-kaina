import streamlit as st
import time
import base64

# ==========================================
# 1. FONCTIONS TECHNIQUES (AUDIO & VISUEL)
# ==========================================

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def play_audio(file_path):
    try:
        with open(file_path, "rb") as f:
            data = f.read()
            b64 = base64.b64encode(data).decode()
            unique_id = int(time.time())
            md = f"""
                <audio autoplay="true" id="player_{unique_id}" style="display:none;">
                    <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
                </audio>
                """
            st.markdown(md, unsafe_allow_html=True)
    except:
        pass

# ==========================================
# 2. CONFIGURATION ET STYLE CSS ULTIME
# ==========================================

st.set_page_config(page_title="Pour ma Reine Kaina ❤️", page_icon="💍", layout="centered")

def apply_ultra_design(image_file):
    bin_str = get_base64(image_file)
    st.markdown(f"""
    <style>
    /* Import de polices élégantes */
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Poppins:wght@300;400;600&display=swap');

    /* Fond d'écran plein écran */
    .stApp {{
        background: linear-gradient(rgba(0,0,0,0.3), rgba(0,0,0,0.3)), url("data:image/png;base64,{bin_str}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        font-family: 'Poppins', sans-serif;
    }}

    /* Conteneurs Glassmorphism */
    .stHeader, .stMarkdown, .stButton, .stRadio, div[data-testid="stVerticalBlock"] > div {{
        background: rgba(255, 255, 255, 0.85);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 25px;
        border: 1px solid rgba(255, 255, 255, 0.3);
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.15);
        margin-bottom: 20px;
    }}

    /* Titres magiques */
    h1, h2, .main-title {{
        font-family: 'Dancing Script', cursive;
        color: #ff4b4b !important;
        text-align: center;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }}

    /* Boutons stylisés */
    .stButton>button {{
        width: 100%;
        background: linear-gradient(45deg, #ff4b4b, #ff8a8a);
        color: white;
        border: none;
        padding: 15px;
        border-radius: 50px;
        font-weight: 600;
        transition: all 0.3s ease;
        text-transform: uppercase;
        letter-spacing: 1px;
    }}
    .stButton>button:hover {{
        transform: scale(1.02);
        box-shadow: 0 5px 15px rgba(255, 75, 75, 0.4);
    }}

    /* Animations de transition */
    .fade-in {{
        animation: fadeIn 1.5s ease-in-out;
    }}
    @keyframes fadeIn {{
        from {{ opacity: 0; transform: translateY(20px); }}
        to {{ opacity: 1; transform: translateY(0); }}
    }}

    /* LA CARTE FINALE POP-UP 3D */
    .card-container {{
        perspective: 1000px;
        display: flex;
        justify-content: center;
        height: 500px;
    }}
    .card-3d {{
        width: 400px;
        height: 300px;
        position: relative;
        transform-style: preserve-3d;
        animation: openCard 4s forwards ease-in-out;
    }}
    @keyframes openCard {{
        0% {{ transform: rotateX(0deg); }}
        100% { transform: rotateX(-15deg) rotateY(-5deg); }
    }}
    .card-face {{
        position: absolute;
        width: 100%;
        height: 100%;
        backface-visibility: hidden;
        border-radius: 15px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }}
    .card-front {{
        background: #d32f2f;
        color: white;
        z-index: 2;
        border: 5px solid #fff;
    }}
    .card-back {{
        background: #fff8e1;
        transform: rotateY(180deg);
        z-index: 1;
        padding: 20px;
        border: 2px solid #ffd700;
    }}
    .gift-ticket {{
        background: white;
        border: 2px dashed #ff4b4b;
        padding: 15px;
        margin-top: -100px;
        animation: popUp 1.5s 3s forwards;
        opacity: 0;
        box-shadow: 0 10px 20px rgba(0,0,0,0.2);
    }}
    @keyframes popUp {{
        from {{ transform: translateY(50px) scale(0.5); opacity: 0; }}
        to {{ transform: translateY(-30px) scale(1); opacity: 1; }}
    }}
    </style>
    """, unsafe_allow_html=True)

apply_ultra_design('image/fond.jpg')

# ==========================================
# 3. LOGIQUE DU QUIZ
# ==========================================

if 'etape' not in st.session_state:
    st.session_state.etape = 0

# Barre de progression calculée
progress_map = {0:0, 1:0, 2:15, 2.1:30, 2.2:45, 2.3:60, 2.4:75, 2.5:90, 3:95, 4:100}
st.progress(progress_map.get(st.session_state.etape, 0) / 100)

# --- ACCUEIL ---
if st.session_state.etape == 0:
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    st.markdown('<h1 class="main-title">✨ Bienvenue dans ton Univers, Kaina ✨</h1>', unsafe_allow_html=True)
    st.write("Aujourd'hui, tu as 20 ans. J'ai créé ce petit bout de code pour te prouver que même dans le monde digital, mon amour pour toi est bien réel.")
    if st.button("DÉCOUVRIR MA SURPRISE"):
        st.balloons()
        st.session_state.etape = 1
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# --- ETAPE 1 : INTRO QUIZ ---
elif st.session_state.etape == 1:
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    st.header("📸 Nos Souvenirs")
    col1, col2 = st.columns(2)
    with col1: st.image("image/photo1.jpg", use_container_width=True)
    with col2: st.image("image/photo2.jpg", use_container_width=True)
    
    st.info("Avant d'accéder au cadeau final, prouve-moi que tu te souviens de tout... Réponds correctement aux 6 questions !")
    if st.button("JE SUIS PRÊTE !"):
        st.session_state.etape = 2
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# --- LES QUESTIONS (Même logique que ton code mais plus propre) ---
elif 2 <= st.session_state.etape < 3:
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    
    # Question 1
    if st.session_state.etape == 2:
        st.subheader("📍 Question 1 : Le début")
        reponse = st.radio("Quel jour nos chemins se sont-ils croisés ?", ["Lundi", "Jeudi", "Samedi", "Dimanche"])
        if st.button("Valider"):
            if reponse == "Samedi":
                st.success("Correct ! ❤️"); time.sleep(1); st.session_state.etape = 2.1; st.rerun()
            else: st.error("Cherche encore mon coeur...")

    # Question 2
    elif st.session_state.etape == 2.1:
        st.subheader("👶 Question 2 : Le futur")
        reponse = st.radio("Le prénom de notre future petite fille ?", ["Lina", "Sana", "Maya", "Inès"])
        if st.button("Valider"):
            if reponse == "Sana":
                st.success("Sana... la plus belle. ✨"); time.sleep(1); st.session_state.etape = 2.2; st.rerun()
            else: st.error("C'est pas ça !")

    # Question 3
    elif st.session_state.etape == 2.2:
        st.subheader("💪 Question 3 : Ma force")
        reponse = st.radio("Mon record au développé couché ?", ["100kg", "110kg", "115kg", "120kg"])
        if st.button("Valider"):
            if reponse == "115kg":
                st.success("Gagné ! Je suis ton roc. 💪"); time.sleep(1); st.session_state.etape = 2.3; st.rerun()
            else: st.error("Plus que ça !")

    # Question 4
    elif st.session_state.etape == 2.3:
        st.subheader("✈️ Question 4 : Évasion")
        reponse = st.radio("Premier pays qu'on visitera ensemble ?", ["Grèce", "Sicile", "Portugal", "Islande"])
        if st.button("Valider"):
            if reponse == "Sicile":
                st.success("Destination l'Italie ! 🇮🇹"); time.sleep(1); st.session_state.etape = 2.4; st.rerun()
            else: st.error("Non, devine encore !")

    # Question 5
    elif st.session_state.etape == 2.4:
        st.subheader("🏠 Question 5 : Notre nid")
        reponse = st.radio("Où vivrons-nous notre rêve ?", ["Marseille", "Cassis", "Carry-le-Rouet", "Saulce"])
        if st.button("Valider"):
            if reponse == "Carry-le-Rouet":
                st.success("La mer et nous... 🌊"); time.sleep(1); st.session_state.etape = 2.5; st.rerun()
            else: st.error("Pas ici !")

    # Question 6
    elif st.session_state.etape == 2.5:
        st.subheader("👑 Question 6 : L'évidence")
        reponse = st.radio("Qui est la seule reine de ma vie ?", ["Une actrice", "Kaina", "La voisine"])
        if st.button("LA RÉPONSE FINALE"):
            if reponse == "Kaina":
                st.success("Pour l'éternité. ❤️"); time.sleep(1); st.session_state.etape = 3; st.rerun()
            else: st.error("Tu doutes ?")
    
    st.markdown('</div>', unsafe_allow_html=True)

# --- ÉTAPE 3 : LA PROMESSE ---
elif st.session_state.etape == 3:
    st.markdown('<div class="fade-in" style="text-align:center;">', unsafe_allow_html=True)
    st.header("🤝 Une dernière chose...")
    st.write("Avant d'ouvrir ton cadeau, promets-tu de rester ma complice, ma meilleure amie et mon grand amour pour les 80 prochaines années ?")
    if st.button("JE LE JURE DEVANT DIEU !"):
        st.session_state.etape = 4
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# --- ÉTAPE 4 : LE FINAL EXPLOSIF ---
elif st.session_state.etape == 4:
    st.balloons()
    st.snow()
    play_audio("image/musique.mp3")

    st.markdown('<h1 style="font-size: 50px;">JOYEUX 20 ANS MA VIE ! 🎂</h1>', unsafe_allow_html=True)
    
    # CARTE 3D
    st.markdown("""
    <div class="card-container">
        <div class="card-3d">
            <div class="card-face card-front">
                <h2 style="color:white;">OUVRE-MOI BB</h2>
                <p>❤️ 20 ans d'Amour ❤️</p>
            </div>
            <div class="card-face card-back">
                <div class="gift-ticket">
                    <h3 style="color:#ff4b4b; margin:0;">🎫 PRIVILÈGE INFINI</h3>
                    <ul style="font-size:12px; list-style:none; padding:0; text-align:left;">
                        <li>💖 <b>Cunnilingus Royal</b> (30min+)</li>
                        <li>💆 <b>Massage Intégral</b> (Mains de fée)</li>
                        <li>💋 <b>Bisous illimités</b> (Où tu veux)</li>
                        <li>☁️ <b>Dodo Papouilles</b> (Priorité 1)</li>
                        <li>👑 <b>Soirée "C'est toi la Chef"</b></li>
                    </ul>
                    <p style="font-weight:bold; font-size:14px; color:#ff4b4b;">JE T'AIME À LA FOLIE</p>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.image("image/photo3.jpg", caption="Toi et Moi, contre le monde entier.")
    
    if st.button("Recommencer pour le plaisir"):
        st.session_state.etape = 0
        st.rerun()
