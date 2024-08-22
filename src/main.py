import streamlit as st

from components.home import home

from components.settings.cities import settings_cities_page
from components.settings.items import settings_items_page
from components.settings.preferences import settings_preferences_page

# initial session_state values
INIT_STATE = {
    'display_columns': 4,
}


def main() -> None:
    for key, value in INIT_STATE.items():
        if key not in st.session_state:
            st.session_state[key] = value

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
