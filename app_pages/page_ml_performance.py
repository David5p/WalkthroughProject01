import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from src.machine_learning.evaluate_clf import load_test_evaluation
import os

def page_ml_performance_metrics():
    version = 'v1'

    st.write("### Train, Validation and Test Set: Labels Frequencies")
    labels_path = f"outputs/{version}/labels_distribution.png"
    if os.path.exists(labels_path):
        labels_distribution = plt.imread(labels_path)
        st.image(labels_distribution, caption='Labels Distribution on Train, Validation and Test Sets')
    else:
        st.warning(f"Labels distribution image not found: {labels_path}")
    st.write("---")

    st.write("### Model History")
    col1, col2 = st.columns(2)

    acc_path = f"outputs/{version}/model_training_acc.png"
    loss_path = f"outputs/{version}/model_training_losses.png"

    with col1:
        if os.path.exists(acc_path):
            model_acc = plt.imread(acc_path)
            st.image(model_acc, caption='Model Training Accuracy')
        else:
            st.warning(f"Accuracy image not found: {acc_path}")

    with col2:
        if os.path.exists(loss_path):
            model_loss = plt.imread(loss_path)
            st.image(model_loss, caption='Model Training Losses')
        else:
            st.warning(f"Loss image not found: {loss_path}")
    st.write("---")

    st.write("### Generalised Performance on Test Set")
    evaluation = load_test_evaluation(version)

    # Build dataframe safely
    df = pd.DataFrame([evaluation])
    df = df.rename(index={0: "Metrics"})
    st.dataframe(df)
