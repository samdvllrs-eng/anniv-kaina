import streamlit as st
import time
import base64

# --- FONCTION FOND D'ÉCRAN ---
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
        background-image: url("data:image/png;base64,%s");
        background-size: cover;

        /* ON UTILISE %% POUR QUE PYTHON NE FASSE PAS D'ERREUR */
        background-position: center 35%%;

        background-attachment: fixed;
        background-repeat: no-repeat;
    }

    /* On applique le fond SEULEMENT aux vrais blocs de contenu */
    .stHeader, .stRadio, .stButton, div[data-testid="stText"], .stSuccess, .stError {
        background-color: rgba(255, 245, 247, 0.9);
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
        margin-bottom: 10px;
    }

    .gift-card {
        background: linear-gradient(135deg, #fff5f7 0%%, #ffd1dc 100%%);
        padding: 30px;
        border-radius: 20px;
        border: 2px dashed #ff4b4b;
        color: #333;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

def play_audio(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
            <audio autoplay="true" loop="true">
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """
        st.markdown(md, unsafe_allow_html=True)

# 1. Configuration
st.set_page_config(page_title="Joyeux Anniversaire Kaina ! 🎂", page_icon="💖", layout="centered")

# 2. Fond
set_background('image/fond.jpg')

# 3. Animation
if 'ballons_faits' not in st.session_state:
    st.balloons()
    st.session_state.ballons_faits = True

# 4. En-tête
st.markdown("""
    <div style="text-align: center; padding: 10px;">
        <p style="font-size: 55px; font-weight: bold; color: #ff4b4b; margin-bottom: 0px; text-shadow: 2px 2px 4px rgba(0,0,0,0.2);">
            🎂 Joyeux Anniversaire ! 🎂
        </p>
        <p style="font-size: 20px; color: #555; background-color: rgba(255,255,255,0.7); display: inline-block; padding: 5px 15px; border-radius: 10px; margin-top: 10px;">
            Une petite surprise codée rien que pour toi... ❤️
        </p>
    </div>
""", unsafe_allow_html=True)

# 5. Section Message Personnel
st.header("✨ Mon petit mot pour toi mon bb d'amour")
st.write("Kakoukakou ! J'ai voulu faire quelque chose d'un peu spécial pour tes 19 ans. Ce site n'existe que sur mon ordinateur, juste pour te dire à quel point tu comptes pour moi. Merci d'être la personne incroyable que tu es au quotidien !")

# 6. Section Galerie Photo
st.header("📸 Nos meilleurs moments")
col_a, col_b = st.columns(2)
with col_a:
    st.image("image/photo1.jpg", caption="Là où tout a commencé")
with col_b:
    st.image("image/photo2.jpg", caption="Toi et moi, pour toujours")

# 7. SECTION JEU
st.header("🎁 Le Quiz de l'Amour")

if 'etape' not in st.session_state:
    st.session_state.etape = 1

# --- ÉTAPE 1 : Le départ ---
if st.session_state.etape == 1:
    st.write("Prête à découvrir ton cadeau ? Pour débloquer ton 'Bon de Privilèges', tu dois répondre à 6 questions sur nous !")
    if st.button("LANCER LE DÉFI !"):
        st.session_state.etape = 2
        st.rerun()

# --- QUESTION 1 : Rencontre ---
elif st.session_state.etape == 2:
    st.subheader("🧐 Question 1 / 6")
    reponse = st.radio("Quel jour de la semaine nos chemins se sont-ils croisés pour la première fois ?", ["Lundi", "Jeudi", "Samedi", "Dimanche"], key="q1")
    if st.button("Valider la réponse"):
        if reponse == "Samedi":
            st.image("image/bravo.jpg", width=500)
            st.success("Bravo ! Un samedi qu'on n'oubliera jamais. ❤️")
            time.sleep(2)
            st.session_state.etape = 2.1
            st.rerun()
        else:
            st.image("image/perdu.jpg", width=250)
            st.error("Nop ! Réessaie mon cœur.")

# --- QUESTION 2 : Prénom bébé ---
elif st.session_state.etape == 2.1:
    st.subheader("🧐 Question 2 / 6")
    reponse = st.radio("Si le destin nous offre une petite fille, quel est le prénom que je rêve de lui donner ?", ["Lina", "Sana", "Maya", "Inès"], key="q2")
    if st.button("Valider la réponse"):
        if reponse == "Sana":
            st.image("image/bravo.jpg", width=500)
            st.success("Exactement ! Sana, comme une évidence. ✨")
            time.sleep(2)
            st.session_state.etape = 2.2
            st.rerun()
        else:
            st.image("image/perdu.jpg", width=250)
            st.error("Ce n'est pas celui-là... concentre-toi !")

# --- QUESTION 3 : DC ---
elif st.session_state.etape == 2.2:
    st.subheader("🧐 Question 3 / 6")
    reponse = st.radio("Quel est mon record actuel au développé couché (ton homme est costaud ou pas ?) ?", ["100kg", "110kg", "115kg", "120kg"], key="q3")
    if st.button("Valider la réponse"):
        if reponse == "115kg":
            st.image("image/bravo.jpg", width=500)
            st.success("Et oui ! 115kg de pur amour (et de muscles) ! 💪")
            time.sleep(2)
            st.session_state.etape = 2.3
            st.rerun()
        else:
            st.image("image/perdu.jpg", width=250)
            st.error("Tu me sous-estimes ! Réessaie haha.")

# --- QUESTION 4 : Pays ---
elif st.session_state.etape == 2.3:
    st.subheader("🧐 Question 4 / 6")
    reponse = st.radio("Quel est le tout premier pays que je veux qu'on aille explorer en amoureux ?", ["La Grèce", "La Sicile", "Le Portugal", "L'Islande"], key="q4")
    if st.button("Valider la réponse"):
        if reponse == "La Sicile":
            st.image("image/bravo.jpg", width=500)
            st.success("La Sicile... ça va être incroyable avec toi. 🇮🇹")
            time.sleep(2)
            st.session_state.etape = 2.4
            st.rerun()
        else:
            st.image("image/perdu.jpg", width=250)
            st.error("Ce n'est pas ma priorité actuelle !")

# --- QUESTION 5 : Habiter ---
elif st.session_state.etape == 2.4:
    st.subheader("🧐 Question 5 / 6")
    reponse = st.radio("Dans quel endroit de rêve est-ce que je nous vois habiter plus tard ?", ["Marseille centre", "Cassis", "Carry-le-Rouet", "Saulce"], key="q5")
    if st.button("Valider la réponse"):
        if reponse == "Carry-le-Rouet":
            st.image("image/bravo.jpg", width=500)
            st.success("La mer, le calme et nous... le paradis à Carry. 🌊")
            time.sleep(2)
            st.session_state.etape = 2.5
            st.rerun()
        else:
            st.image("image/perdu.jpg", width=250)
            st.error("C'est pas assez beau pour nous ça !")

# --- QUESTION 6 : La plus belle ---
elif st.session_state.etape == 2.5:
    st.subheader("🧐 Question 6 / 6 (La plus importante)")
    reponse = st.radio("Dis-moi... qui est la femme la plus belle, la plus incroyable et la seule reine de mon cœur ?", ["Une actrice connue", "Kaina (Moi)", "Ma voisine"], key="q6")
    if st.button("Valider la réponse finale"):
        if reponse == "Kaina (Moi)":
            st.image("image/bravo.jpg", width=500)
            st.success("OUI ! C'est toi et personne d'autre. ❤️")
            time.sleep(2)
            st.session_state.etape = 3
            st.rerun()
        else:
            st.image("image/perdu.jpg", width=250)
            st.error("Tu rigoles j'espère ? Réessaie !")

# --- ÉTAPE 3 : Promesse ---
elif st.session_state.etape == 3:
    st.write("Tu as prouvé que tu me connaissais par cœur. Une dernière chose : promets-tu de rester ma complice pour toujours ?")
    if st.button("JE LE JURE !"):
        st.session_state.etape = 4
        st.rerun()

# --- LE FINAL (ÉTAPE 4) ---
elif st.session_state.etape == 4:
    st.balloons()
    st.snow()

    # --- LANCEMENT DE LA MUSIQUE ---
    # Assure-toi d'avoir un fichier "musique.mp3" dans ton dossier
    try:
        play_audio("image/musique.mp3")
    except:
        pass # Évite de crash si le fichier n'est pas trouvé

    st.success("🌟 FÉLICITATIONS MON BB ! TU AS GAGNÉ ! 🌟")

    # --- CSS POUR L'ANIMATION DE LA CARTE ---
    st.markdown("""
        <style>
        .card-container {
            perspective: 1000px;
            display: flex;
            justify-content: center;
            margin-top: 50px;
        }

        .card {
            width: 350px;
            height: 500px;
            position: relative;
            transform-style: preserve-3d;
            animation: openCard 2.5s forwards; /* Animation d'ouverture auto */
            box-shadow: 0 20px 40px rgba(0,0,0,0.2);
            border-radius: 15px;
        }

        @keyframes openCard {
            0% { transform: rotateY(0deg); }
            100% { transform: rotateY(-10deg); } /* Légère inclinaison pour l'effet 3D */
        }

        .gift-card {
            background: linear-gradient(135deg, #fff5f7 0%, #ffd1dc 100%);
            padding: 30px;
            border-radius: 20px;
            border: 3px dashed #ff4b4b;
            color: #333;
            text-align: center;
            backface-visibility: hidden;
            border: 5px solid white;
        }

        /* Animation de flottement pour rendre ça vivant */
        .floating {
            animation: float 3s ease-in-out infinite;
        }
        @keyframes float {
            0% { transform: translateY(0px); }
            50% { transform: translateY(-10px); }
            100% { transform: translateY(0px); }
        }
        </style>

        <div class="card-container">
            <div class="card floating">
                <div class="gift-card">
                    <h2 style="color: #ff4b4b;">🎫 BON POUR UNE VIE DE PRIVILÈGES</h2>
                    <p style="font-style: italic; font-size: 14px;">Valable à n'importe quel instant, sans date d'expiration.</p>
                    <hr style="border: 1px solid #ffb1c1;">
                    <p style="font-size: 16px; text-align: left;">Mon bb, tu débloques l'accès illimité :</p>
                    <ul style="font-size: 15px; line-height: 1.4; text-align: left; list-style-type: '💖 ';">
                        <li><b>Cunnilingus Royal</b> (30 min+)</li>
                        <li><b>Massage Intégral</b> (20 min)</li>
                        <li><b>Pack 10 Bisous</b> (au choix)</li>
                        <li><b>Séance Papouilles</b> (mode dodo)</li>
                        <li><b>Soirée "C'est toi la chef"</b></li>
                    </ul>
                    <p style="font-weight: bold; margin-top: 20px; font-size: 20px;">JE T'AIME À LA FOLIE ❤️</p>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.write("") # Espace
    st.image("image/photo3.jpg", caption="Ton cadeau final, c'est nous.")

    if st.button("Recommencer le quiz"):
        st.session_state.etape = 1
        st.rerun()
