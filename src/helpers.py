import streamlit as st

from db import mongo_db


def store_widget_value(key) -> None:
    value = st.session_state['_' + key]
    st.session_state[key] = value

    # upsert operation
    query = {key: {"$exists": True}}
    record = {"$set": {key: value}}
    mongo_db['widgets'].update_one(query, record, upsert=True)


def load_widget_value(key) -> None:
    if key in st.session_state:
        st.session_state['_' + key] = st.session_state[key]