"""
This module demonstrates how to connect to an Apache CouchDB instance using the IBM Cloudant SDK,
authenticate using CouchDb Session Authenticator, retrieve a list of all databases,
and fetch a specific document from a database.
"""

from ibmcloudant import CouchDbSessionAuthenticator
from ibmcloudant.cloudant_v1 import CloudantV1


def connect_and_fetch_data():
    """
    Connects to a local Apache CouchDB instance, retrieves a list of all databases,
    and fetches a specific document from a database.
    """
    # Create a CouchDb Session Authenticator using the username and password
    authenticator = CouchDbSessionAuthenticator("admin", "ca7uwaxa")

    # Connect to your Apache CouchDB server running on localhost
    service = CloudantV1(authenticator=authenticator)
    service.set_service_url("http://localhost:5984")

    # Get a list of all the databases your local CouchDB instance
    response = service.get_all_dbs().get_result()
    print("List of databases:", response)

    # Get a document by id in the database
    response = service.get_document(
        db="bio_blitz", doc_id="0c9a55653527e00c7936d5540a000e45"
    ).get_result()
    print("Document fetched:", response)


if __name__ == "__main__":
    connect_and_fetch_data()
