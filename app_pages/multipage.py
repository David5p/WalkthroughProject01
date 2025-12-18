import os
import streamlit as st

st.write("Current working directory:", os.getcwd())


# Import pages (RELATIVE imports because this file is inside app_pages/)
from app_pages.page_summary import summary_page
from page_cells_visualizer import page_cells_visualizer_body as cells_visualizer_page
from app_pages.page_malaria_detector import malaria_detector_page
from app_pages.page_project_hypothesis import project_hypothesis_page
from app_pages.page_ml_performance import ml_performance_page


# Class to generate multiple Streamlit pages using an object-oriented approach
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


app = MultiPage("Malaria Detector")

app.add_page("Quick Project Summary", summary_page)
app.add_page("Cells Visualizer", cells_visualizer_page)
app.add_page("Malaria Detection", malaria_detector_page)
app.add_page("Project Hypothesis", project_hypothesis_page)
app.add_page("ML Performance Metrics", ml_performance_page)

app.run()

