import streamlit as st
from google.cloud import firestore

# Authenticate to Firestore with the JSON account key.
db = firestore.Client.from_service_account_json("firebase/clonewars-cd499.json")

# Create a reference to the a post.
doc_ref = db.collection("posts").document("Hacker News")

st.header('Digg 9000 🌎')

if st.button('Frontpage?'):

    # Get data at reference.
    doc = doc_ref.get()

    # Let's see what we got!
    st.write("The id is: ", doc.id)
    st.write("The contents are: ", doc.to_dict())

