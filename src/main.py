import json
import logging
import logging.config
import pathlib

import streamlit as st

from db import mongo_db
from views.home import home
from views.settings.cities import cities
from views.settings.items import items
from views.settings.preferences import preferences

# initial session_state values
INIT_STATE = {
    'display_columns': 3,
}


class DashboardApp:
    """Main class for streamlit dashboard configuration and utilities."""

    def __init__(self, logger: logging.Logger) -> None:
        self.logger = logger

        self._populate_session_state()

    def _populate_session_state(self) -> None:
        """Retrieve state from storage and load it into st.session_state."""

        for key, value in INIT_STATE.items():
            if key not in st.session_state:
                st.session_state[key] = value

        stored_settings = mongo_db['widgets'].find({}, {"_id": 0})
        for setting in stored_settings:
            st.session_state.update(setting)


def main(app: DashboardApp) -> None:
    """The main function executed after every interaction with streamlit web UI."""

    app.logger.info('main() executed')

    pg = st.navigation(
        {
            'Home': [
                st.Page(home, title='Home Page', icon=':material/home:'),
            ],
            'Settings': [
                st.Page(preferences, title='Preferences', icon=':material/settings:'),
                st.Page(cities, title='Cities', icon=':material/settings:'),
                st.Page(items, title='Items', icon=':material/settings:'),
            ],
        }
    )

    pg.run()


def setup_logging() -> None:
    config_file = pathlib.Path("logging_configs/stdout.json")

    with open(config_file) as f:
        config = json.load(f)

    logging.config.dictConfig(config)


if __name__ == '__main__':

    if 'logger' not in st.session_state:
        setup_logging()
        logger = logging.getLogger(__name__)
        logger.info('logging initialized')
        st.session_state.logger = logger

    if 'app' not in st.session_state:
        logger.info("create Dashboard()")
        st.session_state.app = DashboardApp(logger)

    main(st.session_state.app)
