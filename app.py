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
        # On ajoute un ID unique basé sur le temps pour forcer le navigateur à lire
        unique_id = int(time.time()) 
        md = f"""
            <audio autoplay="autoplay" id="player_{unique_id}" style="display:none;">
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
st.write("Kakoukakou ! J'ai voulu faire quelque chose d'un peu spécial pour tes 20 ans. Ce site n'existe que sur mon ordinateur, juste pour te dire à quel point tu comptes pour moi. Merci d'être la personne incroyable que tu es au quotidien !")

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
# --- LE FINAL (ÉTAPE 4) ---
elif st.session_state.etape == 4:
    # On garde les animations Streamlit, c'est festif
    st.balloons()
    st.snow()

    # --- LANCEMENT DE LA MUSIQUE (on garde la version ID unique) ---
    try:
        play_audio("image/musique.mp3") 
    except:
        pass 

    st.success("🌟 FÉLICITATIONS MON BB ! TU AS GAGNÉ ! 🌟")

    # --- CSS AVANCÉ POUR LA CARTE POP-UP RÉALISTE ---
    # Nous reproduisons la structure de image_0.png
    st.markdown("""
        <style>
        .pop-up-container {
            perspective: 2000px; /* Force l'effet 3D */
            display: flex;
            justify-content: center;
            margin-top: 50px;
            height: 600px; /* Espace pour la carte ouverte */
        }

        .card {
            width: 500px;
            height: 350px;
            position: relative;
            transform-style: preserve-3d;
            animation: openRealisticCard 3s forwards; /* Animation d'ouverture auto réaliste */
            box-shadow: 0 20px 40px rgba(0,0,0,0.3);
            border-radius: 10px;
        }

        /* L'animation mime l'ouverture d'un livre */
        @keyframes openRealisticCard {
            0% { transform: rotateY(0deg); }
            100% { transform: rotateY(-15deg) rotateX(10deg); } /* Inclinaison pour voir l'intérieur */
        }

        /* --- FACE AVANT (Le dos rouge de la carte fermée) --- */
        .card-front {
            position: absolute;
            width: 100%%;
            height: 100%%;
            background-color: #d32f2f; /* Rouge vif comme dans image_0.png */
            border-radius: 10px;
            backface-visibility: hidden; /* Cacher quand ouvert */
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            color: white;
            z-index: 2;
        }

        /* Petit gâteau sur le dos rouge */
        .card-front-cake {
            font-size: 50px;
            margin-bottom: 20px;
        }

        .card-front-title {
            font-size: 30px;
            font-weight: bold;
            text-transform: uppercase;
            letter-spacing: 2px;
        }

        /* --- FACE INTÉRIEURE (L'intérieur blanc avec le pop-up) --- */
        .card-inside {
            position: absolute;
            width: 100%%;
            height: 100%%;
            background-color: #fff8e1; /* Blanc cassé/crème comme dans image_0.png */
            border-radius: 10px;
            backface-visibility: hidden;
            transform: rotateY(180deg); /* Pour être à l'intérieur */
            padding: 30px;
            display: flex;
            flex-direction: column;
            z-index: 1;
            /* Petits dessins de fruits en fond, comme sur ton image */
            background-image: 
                url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" viewBox="0 0 30 30"><text x="5" y="20" font-size="20">🍓</text><text x="15" y="25" font-size="15">🍇</text></svg>'),
                url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" viewBox="0 0 30 30"><text x="5" y="20" font-size="20">🍓</text><text x="15" y="25" font-size="15">🍇</text></svg>');
            background-position: top right, bottom left;
            background-repeat: no-repeat;
        }

        /* --- LE POP-UP LUI-MÊME (Ton Bon de Privilèges) --- */
        .gift-pop-up {
            background-color: white;
            border: 2px solid #ffb1c1;
            border-radius: 10px;
            padding: 15px;
            position: absolute;
            top: 40px;
            left: 40px;
            right: 40px;
            box-shadow: 0 10px 20px rgba(0,0,0,0.15);
            /* C'est cet effet qui donne l'impression de "découpe" */
            transform-origin: bottom center;
            animation: popUpEffect 1s forwards;
            animation-delay: 2.5s; /* Attend que la carte soit presque ouverte */
            opacity: 0;
            backface-visibility: visible;
        }

        @keyframes popUpEffect {
            0% { transform: scaleY(0) translateY(100px); opacity: 0; }
            100% { transform: scaleY(1) translateY(0); opacity: 1; }
        }

        /* Liste de tes privilèges, stylisée */
        .privilege-list {
            font-size: 15px;
            line-height: 1.4;
            text-align: left;
            list-style-type: '💖 ';
            color: #d32f2f; /* Texte rouge */
            margin-top: 10px;
        }
        
        .privilege-list b {
            color: black;
        }

        /* La zone blanche en bas pour ton mot de la fin, comme sur image_0.png */
        .card-inside-note {
            background-color: white;
            border: 1px solid #ddd;
            height: 100px;
            position: absolute;
            bottom: 20px;
            left: 20px;
            right: 20px;
            border-radius: 5px;
            display: flex;
            justify-content: center;
            align-items: center;
            font-weight: bold;
            font-size: 20px;
            color: #ff4b4b;
        }
        </style>

        <div class="pop-up-container">
            <div class="card">
                <div class="card-front">
                    <div class="card-front-cake">🎂</div>
                    <div class="card-front-title">Joyeux Anniversaire</div>
                </div>

                <div class="card-inside">
                    <div class="card-inside-note">JE T'AIME À LA FOLIE ❤️</div>

                    <div class="gift-pop-up">
                        <h2 style="color: #ff4b4b; text-align: center; margin-bottom: 5px; font-size: 20px;">
                            🎫 BON POUR UNE VIE DE PRIVILÈGES
                        </h2>
                        <p style="font-style: italic; font-size: 12px; text-align: center; color: #777;">
                            Valable à n'importe quel instant.
                        </p>
                        <ul class="privilege-list">
                            <li><b>Cunnilingus Royal</b> (30 min+)</li>
                            <li><b>Massage Intégral</b> (20 min)</li>
                            <li><b>Pack 10 Bisous</b></li>
                            <li><b>Séance Papouilles</b> (mode dodo)</li>
                            <li><b>Soirée "C'est toi la chef"</b></li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.write("") # Espace
    # On peut garder la photo d'un bisou en dessous, c'est sympa
    st.image("image/photo3.jpg", caption="Ton cadeau final, c'est nous.")

    if st.button("Recommencer le quiz"):
        st.session_state.etape = 1
        st.rerun()
