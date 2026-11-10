import streamlit as st
import streamlit_survey as Survey

survey = Survey.StreamlitSurvey()


st.title("Stakeholder Questionnaire")
st.write("""

This survey explores how people find workplace information, including policies, procedures, forms and training
costs. Participation is voluntary, and the survey is designed to be brief; the pilot will confirm the expected
completion time.

We will not ask for your name or employer. 
Results will be reported by stakeholder group rather than by
individual. 
Please do not include names or other identifying information in written responses. 
An alternativeresponse method can be provided where required. Responses will be used only for this university project.

""")

survey.radio("1. Which option best describes your role? Tick one", options=["General employee/end user (I use information but do not manage it)", " Manager/team leader", "Information Management/Document Control", "IT/Digital", "HR/Learning and Development", "Governance/Quality/Compliance", "Other: ______________________________"])
survey.radio("2. How often do you look for policies, procedures, guides, forms or training resources? Tick one.", options=["Daily", "A few times a week",  "Weekly", "Monthly", "Less often", "Never"])