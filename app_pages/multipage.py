import streamlit as st

# Import pages (sibling imports inside app_pages folder)
from .page_summary import summary_page
from .page_cells_visualizer import page_cells_visualizer_body as cells_visualizer_page
from .page_malaria_detector import page_malaria_detector_body
from .page_project_hypothesis import page_project_hypothesis_body
from .page_ml_performance import page_ml_performance_metrics



# Class to generate multiple Streamlit pages
class MultiPage:
    def __init__(self, app_name) -> None:
        self.pages = []
        self.app_name = app_name

        st.set_page_config(
            page_title=self.app_name,
            page_icon="🖥️",
            layout="wide"
        )

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
app.add_page("Quick Project Summary", summary_page)
app.add_page("Cells Visualizer", cells_visualizer_page)
app.add_page("Malaria Detection", page_malaria_detector_body)
app.add_page("Project Hypothesis", page_project_hypothesis_body)
app.add_page("ML Performance Metrics", page_ml_performance_metrics)

# Run the app
app.run()
