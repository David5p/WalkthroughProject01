import os
import joblib
import streamlit as st

def load_test_evaluation(version):
    file_path = f'outputs/{version}/evaluation.pkl'
    
    if os.path.exists(file_path):
        return joblib.load(file_path)
    else:
        st.error(f"Evaluation file not found: {file_path}")
        # Return default values to prevent crash
        return {"Loss": None, "Accuracy": None}

