# GoogleSheet Connector

## By [Matheus Almeida](https://twitter.com/mat_almeida)

Create your service account in this link

https://console.developers.google.com/projectselector/iam-admin/serviceaccounts

Download the credentials as json and save in the folder as `service_secret.json`

Run this command on folder to install dependencies

    $ pip3 install -r requeriments.txt

Run the server with

    $ python3 api.py

Access the `localhost:5000/` to see if shows the message `running`

Read the `api.py` code for the others entry points

You can create using the api provided by [gsheet](https://github.com/burnash/gspread)
