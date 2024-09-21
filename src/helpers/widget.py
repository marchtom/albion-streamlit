import streamlit as st

from db import mongo_db


def store_widget_value(key: str) -> None:
    """
    Saves widget's value in both, database and non-perishable attribute of st.session_state, to preserve it's state.
    """

    value = st.session_state['_' + key]
    st.session_state[key] = value

    # upsert operation, in case of widgets not yet registered in database
    query = {key: {"$exists": True}}
    record = {"$set": {key: value}}
    mongo_db['widgets'].update_one(query, record, upsert=True)


def load_widget_value(key: str) -> None:
    """Loads widget's current state from persistent st.session_state attribute."""

    if key in st.session_state:
        st.session_state['_' + key] = st.session_state[key]


class StWidgetManager:
    """Organizes and generates keys for widget groups."""

    def __init__(self, key_class: str) -> None:
        self.key_class = key_class

    def st_session_key(self, value: str) -> str:
        """Key used by st.session_state."""
        return f'{self.key_class}_{value}'

    def st_widget_key(self, value: str) -> str:
        """Key used by widget."""
        return f'_{self.st_session_key(value)}'
