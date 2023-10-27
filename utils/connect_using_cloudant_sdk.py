from ibm_cloud_sdk_core.authenticators import BasicAuthenticator
from ibmcloudant import CouchDbSessionAuthenticator
from ibmcloudant.cloudant_v1 import CloudantV1

# Create a Basic Authenticator with your 'admin' username and 'ca7uwaxa' password
basic_authenticator = BasicAuthenticator("admin", "ca7uwaxa")

# Create a CouchDb Session Authenticator using the username and password
authenticator = CouchDbSessionAuthenticator("admin", "ca7uwaxa")

# Connect to your Apache CouchDB server running on localhost
service = CloudantV1(authenticator=authenticator)
service.set_service_url('http://localhost:5984')

# Get a list of all the databases your local CouchDB instance
response = service.get_all_dbs().get_result()
print(response)

# Get a document by id in the database
response = service.get_document(db='bio_blitz', doc_id='0c9a55653527e00c7936d5540a000e45').get_result()
print(response)



