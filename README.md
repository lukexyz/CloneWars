# CloneWars
A reddit clone built with Streamlit and Firestore


# GCP

```sh
# run in gcp cloud shell
$ git clone https://github.com/lukexyz/CloneWars
$ cd CloneWars
$ . prepare_environment.sh
```
This script file:

* Creates an App Engine application.
* Creates a Cloud Storage bucket named gs:[Project-ID]-media.
* Exports two environment variables: GCLOUD_PROJECT and GCLOUD_BUCKET.
* Creates a virtualenv isolated Python environment for Python 3 and activates it.
* Runs > pip install -r requirements.txt.
* Creates entities in Cloud Datastore.
* Prints out the Google Cloud Platform Project ID.