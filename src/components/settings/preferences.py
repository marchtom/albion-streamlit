import streamlit as st

from helpers import load_widget_value, store_widget_value


def settings_preferences() -> None:
    load_widget_value('display_columns')

    st.number_input(
        'Number of columns in displays',
        min_value=1,
        max_value=10,
        step=1,
        key='_display_columns',
        on_change=store_widget_value,
        args=['display_columns'],
    )

settings_preferences_page = st.Page(settings_preferences, title='Preferences', icon=':material/settings:')