import logging
import types

import streamlit as st

from views.home import home

from views.settings.cities import cities
from views.settings.items import items
from views.settings.preferences import preferences

from db import mongo_db

# initial session_state values
INIT_STATE = {
    'display_columns': 3,
}


class Dashboard:
    """Main class for Dashboard serving and configuration."""

    def __init__(self) -> None:
        self.home = types.MethodType(home, self)
        self.cities = types.MethodType(cities, self)
        self.items = types.MethodType(items, self)
        self.preferences = types.MethodType(preferences, self)

        self._populate_session_state()

    def _populate_session_state(self) -> None:
        """Retrieve state from storage and load it into st.session_state."""

        for key, value in INIT_STATE.items():
            if key not in st.session_state:
                st.session_state[key] = value

        stored_settings = mongo_db['widgets'].find({}, {"_id": 0})
        for setting in stored_settings:
            st.session_state.update(setting)

    def main(self) -> None:
        logger.info('main() executed')

        pg = st.navigation(
            {
                'Home': [
                    st.Page(self.home, title='Home Page', icon=':material/home:'),
                ],
                'Settings': [
                    st.Page(self.preferences, title='Preferences', icon=':material/settings:'),
                    st.Page(self.cities, title='Cities', icon=':material/settings:'),
                    st.Page(self.items, title='Items', icon=':material/settings:'),
                ],
            }
        )

        pg.run()

if __name__ == '__main__':

    if 'logger' not in st.session_state:
        logging.basicConfig(
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            level=logging.INFO,
        )
        logger = logging.getLogger(__name__)
        logger.info('logging initialized')
        st.session_state.logger = logger

    if 'app' not in st.session_state:
        logger.info("create Dashboard()")
        st.session_state.app = Dashboard()

    st.session_state.app.main()
