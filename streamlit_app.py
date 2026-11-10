import streamlit as st
import streamlit_survey as Survey

survey = Survey.StreamlitSurvey()


st.title("""IOT453U QUALITY DRIVEN DEVELOPMENT
ASSESSMENT 001: GROUP SURVEY PLAN
Centralised Workplace Knowledge and Procedures Hub
""")
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

st.write("A. About You")

survey.radio("1. Which option best describes your role? Tick one", options=["General employee/end user (I use information but do not manage it)", " Manager/team leader", "Information Management/Document Control", "IT/Digital", "HR/Learning and Development", "Governance/Quality/Compliance", "Other: ______________________________"])
survey.radio("2. How often do you look for policies, procedures, guides, forms or training resources? Tick one.", options=["Daily", "A few times a week",  "Weekly", "Monthly", "Less often", "Never"])

st.write("B. How It Works Now")

survey.multiselect("3.  Where do you usually look for workplace information? Tick all that apply", options=["Microsoft Teams", "Shared drives", "Email", "SharePoint/intranet", "Department folders", "Ask a colleague"])
survey.radio("4. How easy is it to find the workplace information you need? Tick one.", options=["1 - Very difficult", "2", "3", "4", "5 - Very easy", "Not applicable"])
survey.radio("5. How confident are you that the information you find is the latest or authoritative version? Tick one.", options=["1 - Very confident", "2", "3", "4", "5 - Very confident", "Not applicable"])
survey.radio("6. During a typical week, approximately how much time do you spend looking for workplace information? Tick one.", options=["Under 15 minutes", "15-30 minutes", "31-60 minutes", "More than one hour", "None"])
survey.multiselect("7. Which of the following have you experienced? Tick all that apply.", options=["I did not know where to look", "The search was slow or did not work", "I found multiple versions of the same information", "I was unsure which version was the latest", "I used out-of-date information", "I could not access the information", "I had to ask a colleague", "None of these"])