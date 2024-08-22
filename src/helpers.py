import streamlit as st


def store_widget_value(key) -> None:
    st.session_state[key] = st.session_state['_' + key]


def load_widget_value(key) -> None:
    if key in st.session_state:
        st.session_state['_' + key] = st.session_state[key]