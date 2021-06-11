import streamlit as st
from google.cloud import firestore

# Authenticate to Firestore with the JSON account key.
db = firestore.Client.from_service_account_json("firebase/clonewars-cd499.json")


st.header('Digg 9000 🌎')

if st.button('Frontpage'):
    # Now let's make a reference to ALL of the posts
    posts_ref = db.collection("posts")

    # For a reference to a collection, we use .stream() instead of .get()
    for doc in posts_ref.stream():
        st.write("The id is: ", doc.id)
        st.write("The contents are: ", doc.to_dict())


if st.button('New Post'):
    title = st.text_input("Post title")
    url = st.text_input("Post url")
    submit = st.button(("Submit new post"))

    if title and url and submit:
        # upload inputs
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