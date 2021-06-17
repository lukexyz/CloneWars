# CloneWars
A reddit clone built with Streamlit and Firestore


### GCP

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

Run the application:
```sh
streamlit run app.py
```

In Cloud Shell, click Web preview (Web Preview) > Preview on port 8080

### IAM

1. In the Google Cloud Console, on the Navigation menu (Navigation menu), click Billing.
    * Verify that a Billing account is linked to the project.

2. In the Google Cloud Console, on the Navigation menu (Navigation menu), click Identity Platform.
    * Click Enable Identity Platform.

3. Click Add a Provider.
    * In the Sign-in method window, select Google
    * Click Enabled.

4. In the Authorized Domains pane, click Add Domain.

Add a user  
5. In the Identity Platform pane, click Users.
    * Click Add User.

6. Add script to html  
In the navigation pane, click Providers.

Click Application Setup Details.

In the Configure your application dialog box, copy the Identity Platform markup.

* Paste the configuration markup just before the other <script></script> tags at the bottom of the page.