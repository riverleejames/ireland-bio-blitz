"""
This script reads formatted data from a JSON file 
and then uploads it to CouchDB using a bulk upload request.

Attributes:
    COUCHDB_URL (str): The URL of the CouchDB instance.
    DATABASE_NAME (str): The name of the CouchDB database to upload to.
    USERNAME (str): The username for CouchDB authentication.
    PASSWORD (str): The password for CouchDB authentication.
    bulk_upload_url (str): The endpoint URL for CouchDB bulk upload.
    headers (dict): Headers for the HTTP request.
"""

import json
import requests

# CouchDB credentials and URL
COUCHDB_URL = "http://localhost:5984/"
DATABASE_NAME = "bio_blitz"
USERNAME = "admin"
PASSWORD = "ca7uwaxa"

# Endpoint for bulk upload
bulk_upload_url = f"{COUCHDB_URL}/{DATABASE_NAME}/_bulk_docs"

# Headers for the request
headers = {"Content-Type": "application/json", "Accept": "application/json"}


def upload_data_to_couchdb(file_path, upload_url, headers, auth, timeout=300):
    """
    Reads formatted data from a JSON file and uploads it to CouchDB.

    Args:
        file_path (str): Path to the JSON file containing the formatted data.
        upload_url (str): The endpoint URL for CouchDB bulk upload.
        headers (dict): Headers for the HTTP request.
        auth (tuple): A tuple containing the username and password for CouchDB authentication.
        timeout (int, optional): The request timeout in seconds. Defaults to 300 seconds.

    Returns:
        bool: True if the upload was successful, False otherwise.
    """
    # Read the data from the input JSON file
    with open(file_path, "r", encoding="utf-8") as infile:
        data = json.load(infile)

    # Send the request to CouchDB
    response = requests.post(
        upload_url, data=json.dumps(data), headers=headers, auth=auth, timeout=timeout
    )

    # Check the response
    if response.status_code == 201:
        print("Data uploaded successfully!")
        return True
    else:
        print("Failed to upload data. Response:", response.text)
        return False


if __name__ == "__main__":
    upload_data_to_couchdb(
        "../dataset/formatted_data_for_bulk_upload.json",
        bulk_upload_url,
        headers,
        (USERNAME, PASSWORD),
    )
