import streamlit as st

from helpers import load_widget_value, store_widget_value

CITIES = [
    'Bridgewatch',
    'Fort Sterling',
    'Lymhurst',
    'Martlock',
    'Thetford',
    'Brecilien',
    'Caerleon',
]


def cities() -> None:
    search_query = st.text_input("Search / Filter", "")

    columns = st.columns(st.session_state.display_columns)

    filtered_cities = [city for city in CITIES if search_query.strip() in city]

    for idx, city in enumerate(filtered_cities):
        st_key = f'city_checkbox_{city}'
        widget_key = f'_{st_key}'
        load_widget_value(st_key)

        col = columns[idx % st.session_state.display_columns]
        col.checkbox(
            city,
            key=widget_key,
            on_change=store_widget_value,
            args=[st_key],
        )
