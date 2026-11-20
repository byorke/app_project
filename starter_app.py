"""Starting point for Workshop 2. Run: python -m streamlit run app.py"""
import streamlit as st

st.title("Molecular solubility predictor")
st.write("Build an app to explore predicted aqueous solubility.")

# Try a Streamlit widget. Decide how to obtain six descriptor values,
# load the supplied model, and display its predictions.
logp = st.slider("Explore LogP", -2.0, 7.0, 2.0, 0.1)
st.write(f"Selected LogP: {logp:.1f}")
