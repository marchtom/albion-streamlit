import streamlit as st

from db import mongo_db


def home() -> None:
    st.title('Home Page')
    st.write('Debugging purpose')
    st.write(f'st.session_state:\n\n{dict(st.session_state)}')
    st.write(f'Mongo data:\n\n{list(mongo_db['widgets'].find({}, {"_id": 0}))}')
    st.button('Flush DB', on_click=flush_db)


def flush_db() -> None:
     mongo_db['widgets'].delete_many({})
