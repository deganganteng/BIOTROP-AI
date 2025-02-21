import streamlit as st
from AIComponents.Crew import *

def Base():
    # Input user
    st.title("SEAMEO BIOTROP AI Assistant")
    UserQueries = st.text_input("Hi, how can I assist you?", placeholder="Enter your query here...")
    submit = st.button("Submit Query")
    
    if submit:
        if UserQueries.strip() == "":
            st.warning("Please enter a query to get started.")
        else:
            st.write('**Your Query:**')
            st.markdown(f"> {UserQueries}")
            st.write("Model is processing the answer, please wait...")

            # Jalankan layanan langsung tanpa validator tambahan
            try:
                GemaSupportServiceCrew = Crew(UserQueries).BaseCrew
                results = GemaSupportServiceCrew.kickoff()

                if results:
                    st.success("Here are the results:")
                    st.markdown(results)
                else:
                    st.warning("No relevant results were found. Please refine your query.")
            except Exception as e:
                st.error(f"An error occurred while processing your request: {e}")
