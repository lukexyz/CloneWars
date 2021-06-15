import streamlit as st
from google.cloud import firestore

# Authenticate to Firestore with the JSON account key.
db = firestore.Client.from_service_account_json("firebase/clonewars-cd499.json")

st.header('Digg 9000 🌎')

# Submit new post to firestore
form = st.form(key='new-post-form')
title = form.text_input("Post title")
url = form.text_input("Post url")
submit = form.form_submit_button('Submit new post')

if submit:
    st.write(f'Submitting: {title}')

if title and url and submit:
    # upload inputs
    st.write(f'Sending to database {url}')
    doc_ref = db.collection("posts").document(title)
    doc_ref.set({
        "title": title,
        "url" : url
        })

# And then render each post, using some light Markdown
posts_ref = db.collection("posts")
for doc in posts_ref.stream():
	post = doc.to_dict()
	title = post["title"]
	url = post["url"]

	st.subheader(f"Post: {title}")
	st.write(f":link: [{url}]({url})")

if st.button('Search'):
    # Create a reference to the a post (fast)
    search_title = st.text_input('Search Title')
    if st.button('Go'):
        print(search_title)
        doc_ref = db.collection("posts").document(search_title)

        # Get data at reference (retrieval)
        doc = doc_ref.get()

        # Let's see what we got!
        st.write("The id is: ", doc.id)
        st.write("The contents are: ", doc.to_dict())

if st.button('Fetch db'):
    # Now let's make a reference to ALL of the posts
    posts_ref = db.collection("posts")

    # For a reference to a collection, we use .stream() instead of .get()
    for doc in posts_ref.stream():
        st.write("The id is: ", doc.id)
        st.write("The contents are: ", doc.to_dict())
