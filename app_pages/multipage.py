import streamlit as st

st.set_page_config(
    page_title="Malaria Detector",
    page_icon="...",
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

        page_titles = [page["title"] for page in self.pages]

        # Initialize session state for selected page index if not exists
        if "selected_page" not in st.session_state:
            st.session_state.selected_page = 0  # default first page

        selected_index = st.sidebar.radio(
            "Menu",
            range(len(page_titles)),
            format_func=lambda i: page_titles[i],
            index=st.session_state.selected_page,
            key=f"multipage_sidebar_radio_{id(self)}"
        )
        st.session_state.selected_page = selected_index

        # Call the selected page function
        self.pages[selected_index]["function"]()


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
