import streamlit as st
import time
import base64
import os

# --- FONCTION FOND D'ÉCRAN ---
def set_background(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as f:
            data = f.read()
            b64 = base64.b64encode(data).decode()
        # On utilise une f-string SANS % pour éviter les erreurs de syntaxe
        page_bg_img = f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{b64}");
            background-size: cover;
            background-position: center 35%;
            background-attachment: fixed;
            background-repeat: no-repeat;
        }}
        .stHeader, .stRadio, .stButton, div[data-testid="stText"], .stSuccess, .stError {{
            background-color: rgba(255, 245, 247, 0.9);
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
            margin-bottom: 10px;
        }}
        </style>
        """
        st.markdown(page_bg_img, unsafe_allow_html=True)
    else:
        st.error(f"⚠️ Image introuvable : {image_path}. Vérifie que le fichier est bien dans le dossier 'image'.")

# 1. Configuration
st.set_page_config(page_title="Joyeux Anniversaire Kaina ! 🎂", page_icon="💖", layout="centered")

# 2. Application du fond
set_background('image/fond.jpg')

# 3. Gestion des étapes
if 'etape' not in st.session_state:
    st.session_state.etape = 1

# 4. En-tête (Toujours visible)
st.markdown("""
    <div style="text-align: center; padding: 10px;">
        <h1 style="color: #ff4b4b; text-shadow: 2px 2px 4px rgba(0,0,0,0.2);">🎂 Joyeux Anniversaire Kaina ! 🎂</h1>
        <p style="font-size: 20px; color: #555; background: rgba(255,255,255,0.7); display: inline-block; padding: 5px 15px; border-radius: 10px;">
            Une surprise codée rien que pour toi... ❤️
        </p>
    </div>
""", unsafe_allow_html=True)

# --- LOGIQUE DU QUIZ ---

if st.session_state.etape == 1:
    st.header("✨ Mon petit mot pour toi")
    st.write("Kakoukakou ! Pour tes 20 ans, j'ai voulu créer ce petit coin spécial. Réponds aux questions pour débloquer ton cadeau !")
    if st.button("LANCER LE DÉFI !"):
        st.session_state.etape = 2
        st.rerun()

elif st.session_state.etape == 2:
    st.subheader("🧐 Question 1 / 6")
    reponse = st.radio("Quel jour nous sommes-nous vus la première fois ?", ["Lundi", "Jeudi", "Samedi", "Dimanche"])
    if st.button("Valider"):
        if reponse == "Samedi":
            st.success("Bravo ! ❤️")
            st.session_state.etape = 2.1
            st.rerun()
        else: st.error("Faux ! Réessaie.")

elif st.session_state.etape == 2.1:
    st.subheader("🧐 Question 2 / 6")
    reponse = st.radio("Prénom de notre future fille ?", ["Lina", "Sana", "Maya", "Inès"])
    if st.button("Valider"):
        if reponse == "Sana":
            st.success("Exactement ! ✨")
            st.session_state.etape = 2.2
            st.rerun()
        else: st.error("Non...")

elif st.session_state.etape == 2.2:
    st.subheader("🧐 Question 3 / 6")
    reponse = st.radio("Mon record au DC ?", ["100kg", "110kg", "115kg", "120kg"])
    if st.button("Valider"):
        if reponse == "115kg":
            st.success("Costaud ton homme ! 💪")
            st.session_state.etape = 2.3
            st.rerun()
        else: st.error("Tu me sous-estimes !")

elif st.session_state.etape == 2.3:
    st.subheader("🧐 Question 4 / 6")
    reponse = st.radio("Premier voyage ?", ["La Grèce", "La Sicile", "Le Portugal", "L'Islande"])
    if st.button("Valider"):
        if reponse == "La Sicile":
            st.success("Andiamo ! 🇮🇹")
            st.session_state.etape = 2.4
            st.rerun()
        else: st.error("Raté !")

elif st.session_state.etape == 2.4:
    st.subheader("🧐 Question 5 / 6")
    reponse = st.radio("Où habiter ?", ["Marseille", "Cassis", "Carry-le-Rouet", "Saulce"])
    if st.button("Valider"):
        if reponse == "Carry-le-Rouet":
            st.success("Le rêve... 🌊")
            st.session_state.etape = 2.5
            st.rerun()
        else: st.error("Non !")

elif st.session_state.etape == 2.5:
    st.subheader("🧐 Question 6 / 6")
    reponse = st.radio("Qui est la plus belle ?", ["Une actrice", "Kaina", "La voisine"])
    if st.button("Valider la finale"):
        if reponse == "Kaina":
            st.success("Évidemment ! ❤️")
            st.session_state.etape = 3
            st.rerun()

elif st.session_state.etape == 3:
    st.write("Promets-tu de m'aimer pour toujours ?")
    if st.button("JE LE JURE !"):
        st.session_state.etape = 4
        st.rerun()

elif st.session_state.etape == 4:
    st.balloons()
    st.success("🌟 FÉLICITATIONS MON BB ! 🌟")

    # CARTE POP-UP CORRIGÉE SANS % DE FORMATAGE
    st.markdown("""
        <style>
        .card-container {
            perspective: 1000px;
            display: flex;
            justify-content: center;
            margin: 50px 0;
            height: 400px;
        }
        .card {
            width: 350px;
            height: 250px;
            position: relative;
            transform-style: preserve-3d;
            animation: openCard 4s forwards;
            box-shadow: 0 20px 40px rgba(0,0,0,0.2);
            border-radius: 15px;
            background: #d32f2f;
        }
        @keyframes openCard {
            0% { transform: rotateX(0deg); }
            100% { transform: rotateX(-15deg) rotateY(-5deg); }
        }
        .inner-card {
            background: linear-gradient(135deg, #fff5f7 0%, #ffd1dc 100%);
            padding: 20px;
            border-radius: 15px;
            border: 3px dashed #ff4b4b;
            height: 100%;
            text-align: center;
        }
        </style>
        <div class="card-container">
            <div class="card">
                <div class="inner-card">
                    <h2 style="color: #ff4b4b; font-size: 18px;">🎫 BON DE PRIVILÈGES</h2>
                    <ul style="text-align: left; font-size: 14px; list-style: '💖 ';">
                        <li><b>Service Royal</b> (30 min+)</li>
                        <li><b>Massage Intégral</b> (20 min)</li>
                        <li><b>Pack 10 Bisous</b></li>
                        <li><b>Séance Papouilles</b></li>
                        <li><b>Soirée Totale Liberté</b></li>
                    </ul>
                    <p style="font-weight: bold;">JE T'AIME ❤️</p>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    if st.button("Recommencer"):
        st.session_state.etape = 1
        st.rerun()
