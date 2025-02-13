import streamlit as st
import pandas as pd

# Charger le fichier CSV
@st.cache_data
def load_data():
    file_path = "quiz_urbanisme.csv"
    return pd.read_csv(file_path)

df = load_data()

st.title("Quiz sur l'Urbanisme")

if "score" not in st.session_state:
    st.session_state.score = 0

if "answers" not in st.session_state:
    st.session_state.answers = {}

# Formulaire pour éviter plusieurs boutons
with st.form(key="quiz_form"):
    for i, row in df.iterrows():
        st.subheader(f"Question {i+1} : {row['Question']}")
        options = {
            "A": row['Réponse A'][3:],
            "B": row['Réponse B'][3:],
            "C": row['Réponse C'][3:],
            "D": row['Réponse D'][3:]
        }
        
        # Clé unique pour chaque question
        selected_option = st.radio(
            f"Choisissez une réponse pour la question {i+1} :",
            options.values(),
            key=f"q{i}"
        )

        # Stocker la réponse
        st.session_state.answers[i] = selected_option

    submit_button = st.form_submit_button("Valider mes réponses")

# Vérification des réponses après soumission
if submit_button:
    score = 0
    for i, row in df.iterrows():
        correct_answer = options[row['Bonne réponse']]
        if st.session_state.answers.get(i) == correct_answer:
            score += 1

    st.session_state.score = score
    st.success(f"✅ Score final : {st.session_state.score}/{len(df)}")
