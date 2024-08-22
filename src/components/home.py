import streamlit as st


def home() -> None:
    st.title('Home Page')
    st.write('Debugging purpose')
    st.write(f'{dict(st.session_state)}')
