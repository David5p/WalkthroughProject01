import streamlit as st

st.set_page_config(
    page_title="Malaria Detector",
    page_icon="🖥️",
    layout="wide"
)

# Import pages (sibling imports inside app_pages folder)
from app_pages.page_summary import page_summary_body
from app_pages.page_cells_visualizer import page_cells_visualizer_body as cells_visualizer_page
from app_pages.page_malaria_detector import page_malaria_detector_body
from app_pages.page_project_hypothesis import page_project_hypothesis_body
from app_pages.page_ml_performance import page_ml_performance_metrics

# Class to generate multiple Streamlit pages
class MultiPage:
    def __init__(self, app_name) -> None:
        self.pages = []
        self.app_name = app_name

    def add_page(self, title, func) -> None:
        self.pages.append(
            {
                "title": title,
                "function": func
            }
        )

    def run(self):
        st.title(self.app_name)

        page = st.sidebar.radio(
            "Menu",
            self.pages,
            format_func=lambda page: page["title"]
        )

        # Call the selected page function
        page["function"]()


# Create app instance
app = MultiPage("Malaria Detector")

# Add pages
app.add_page("Quick Project Summary", page_summary_body)
app.add_page("Cells Visualizer", cells_visualizer_page)
app.add_page("Malaria Detection", page_malaria_detector_body)
app.add_page("Project Hypothesis", page_project_hypothesis_body)
app.add_page("ML Performance Metrics", page_ml_performance_metrics)

# Run the app
app.run()
