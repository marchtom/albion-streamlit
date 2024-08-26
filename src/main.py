import streamlit as st

from views.home import home

from views.settings.cities import settings_cities_page
from views.settings.items import settings_items_page
from views.settings.preferences import settings_preferences_page

from db import mongo_db

# initial session_state values
INIT_STATE = {
    'display_columns': 3,
}


def main() -> None:
    for key, value in INIT_STATE.items():
        if key not in st.session_state:
            st.session_state[key] = value

    stored_settings = mongo_db['widgets'].find({}, {"_id": 0})
    for setting in stored_settings:
        st.session_state.update(setting)

    # home page must be defined in `main`
    home_page = st.Page(home, title='Home Page', icon=':material/home:')

    pg = st.navigation(
        {
            'Home': [
                home_page,
            ],
            'Settings': [
                settings_preferences_page,
                settings_cities_page,
                settings_items_page,
            ],
        }
    )

    pg.run()


if __name__ == '__main__':
    main()
