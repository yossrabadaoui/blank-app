import streamlit as st
import streamlit_survey as Survey

survey = Survey.StreamlitSurvey()


st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

survey.radio("Which option best describes your role? Tick one", options=["General employee/end user (I use information but do not manage it)
1", " Manager/team leader", "Information Management/Document Control", "IT/Digital", "HR/Learning and Development", "Governance/Quality/Compliance", "Other: ______________________________"])