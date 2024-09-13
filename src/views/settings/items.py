import streamlit as st

from helpers import load_widget_value, store_widget_value

ITEMS = [
    'T1_CARROT',
    'T2_BEAN',
    'T3_WHEAT',
    'T4_TURNIP',
    'T5_CABBAGE',
    'T6_POTATO',
    'T7_CORN',
    'T8_PUMPKIN',
    'T2_AGARIC',
    'T3_COMFREY',
    'T4_BURDOCK',
    'T5_TEASEL',
    'T6_FOXGLOVE',
    'T7_MULLEIN',
    'T8_YARROW',
    'T3_EGG',
    'T4_MILK',
    'T5_EGG',
    'T6_MILK',
    'T8_MILK',
    'T1_SEAWEED',
    'T1_WORM',
]


def items() -> None:
    search_query = st.text_input("Search / Filter", "")

    columns = st.columns(st.session_state.display_columns)

    filtered_items = [item for item in ITEMS if search_query.strip() in item]

    for idx, item in enumerate(filtered_items):
        st_key = f'item_checkbox_{item}'
        widget_key = f'_{st_key}'
        load_widget_value(st_key)

        col = columns[idx % st.session_state.display_columns]
        col.checkbox(
            item,
            key=widget_key,
            on_change=store_widget_value,
            args=[st_key],
        )
