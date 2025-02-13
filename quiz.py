import streamlit as st
import pandas as pd

# Charger le fichier CSV
def load_data():
    file_path = "quiz_urbanisme.csv"  # Mettez ici le chemin correct si nécessaire
    return pd.read_csv(file_path)

df = load_data()

st.title("Quiz sur l'Urbanisme")
score = 0

# Affichage des questions une par une
for i, row in df.iterrows():
    st.subheader(f"Question {i+1} : {row['Question']}")
    options = {
        "A": row['Réponse A'][3:],  # Supprimer le préfixe "A. "
        "B": row['Réponse B'][3:],
        "C": row['Réponse C'][3:],
        "D": row['Réponse D'][3:]
    }
    
    reponse = st.radio("Choisissez une réponse :", list(options.values()), key=f"q{i}")
    if st.button(f"Valider la question {i+1}"):
        bonne_reponse = options[row['Bonne réponse']]
        if reponse == bonne_reponse:
            st.success("✅ Bonne réponse !")
            score += 1
        else:
            st.error(f"❌ Mauvaise réponse. La bonne réponse était : {bonne_reponse}.")

st.write(f"**Score final : {score}/{len(df)}**")
