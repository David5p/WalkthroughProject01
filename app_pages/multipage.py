import streamlit as st

class MultiPage:
    def __init__(self, app_name: str) -> None:
        self.pages = []
        self.app_name = app_name

    def add_page(self, title: str, func) -> None:
        self.pages.append({"title": title, "function": func})

    def run(self):
        # Initialize session state for selected page
        if "selected_page" not in st.session_state:
            st.session_state.selected_page = 0

        page_titles = [p["title"] for p in self.pages]
        st.session_state.selected_page = st.sidebar.radio(
            "Menu",
            range(len(self.pages)),
            format_func=lambda i: page_titles[i],
            index=st.session_state.selected_page
        )

        # Display app title
        st.title(self.app_name)

        # Call the selected page
        selected_page = self.pages[st.session_state.selected_page]
        selected_page["function"]()
