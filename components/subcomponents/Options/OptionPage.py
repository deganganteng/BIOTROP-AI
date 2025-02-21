import streamlit as st
from AIComponents.Crew import *

class OptionPage:
    def __init__(self, question: str, info: str, Context, lang, crew_method):
        self.crew_method = crew_method
        self.question = question
        self.Context = Context
        self.info = info
        self.lang = lang

    def BaseIO(self):
        st.markdown(self.info)
        UserQueries = st.text_input(self.question)
        context = self.Context
        language = self.lang
        submit = st.button("Ask!")
        if submit and UserQueries != "":
            st.write('**Your Query:**')
            st.write(f"> {UserQueries}")
            with st.spinner("AI is processing your question!"):
                biotrop_instance = BioCrew(UserQueries, context, language)
                results = self.crew_method(biotrop_instance)

            st.success("Here are the results:")
            st.markdown(results)

        elif submit and UserQueries == "":
            st.warning("Please enter a query to get started.")
    
    def Book(self):
        st.markdown(self.info)
        UserQueries = st.text_input(self.question)
        context = self.Context
        language = self.lang
        submit = st.button("Ask!")
        if submit and UserQueries != "":
            st.write('**Your Query:**')
            st.write(f"> {UserQueries}")
            with st.spinner("AI is processing your question!"):
                book_instance = BioCrew(UserQueries, context, language)
                results = self.crew_method(book_instance)

            st.success("Here are the results:")
            st.markdown(results)

        elif submit and UserQueries == "":
            st.warning("Please enter a query to get started.")
    
    def StartPage(self):
        st.info("Please select a menu above to get started, along with explanations of each available menu!")
        st.markdown("""
##### SEAMEO BIOTROP
A research center for the sustainable management of tropical biodiversity in Southeast Asia. Here is the available information:

##### General Information about SEAMEO BIOTROP
- General information about SEAMEO BIOTROP
- Organizational profile and its history
- Mission and vision of SEAMEO BIOTROP
- Role in biodiversity conservation and resource management

##### Research Information
- Ongoing and upcoming research projects
- Collaborations with universities and research institutions
- Opportunities to contribute to research

##### Training and Workshop Information
- Available training programs
- Training topics such as sustainable agriculture, biotechnology, and environmental technology
- Training schedules and registration procedures

##### Collaboration Information
- How to become a partner or collaborator with SEAMEO BIOTROP
- Ongoing collaboration projects
- Benefits of collaborating with SEAMEO BIOTROP

##### SEAMEO BIOTROP E-Library
- Access to digital book collections and research publications
- Guidelines for using the e-library
""")
