import streamlit as st

# ------------------------
# Page configuration
# ------------------------
st.set_page_config(
    page_title="Malaria Detector",
    page_icon=None,  # No icon
    layout="wide"
)

# ------------------------
# Import pages
# ------------------------
from app_pages.page_summary import page_summary_body
from app_pages.page_cells_visualizer import page_cells_visualizer_body as cells_visualizer_page
from app_pages.page_malaria_detector import page_malaria_detector_body
from app_pages.page_project_hypothesis import page_project_hypothesis_body
from app_pages.page_ml_performance import page_ml_performance_metrics

# ------------------------
# MultiPage class
# ------------------------
class MultiPage:
    def __init__(self, app_name: str) -> None:
        self.pages = []
        self.app_name = app_name

    def add_page(self, title: str, func) -> None:
        self.pages.append({"title": title, "function": func})

    def run(self):
        # Initialize session state to persist selected page
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

        # Run the selected page
        selected_page = self.pages[st.session_state.selected_page]
        selected_page["function"]()


# ------------------------
# App instance
# ------------------------
app = MultiPage("Malaria Detector")

# ------------------------
# Add pages
# ------------------------
app.add_page("Quick Project Summary", page_summary_body)
app.add_page("Cells Visualizer", cells_visualizer_page)
app.add_page("Malaria Detection", page_malaria_detector_body)
app.add_page("Project Hypothesis", page_project_hypothesis_body)
app.add_page("ML Performance Metrics", page_ml_performance_metrics)

# ------------------------
# Run app
# ------------------------
app.run()
