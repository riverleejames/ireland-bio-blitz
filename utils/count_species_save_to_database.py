"""
This module is designed to interact with a CouchDB database to fetch species occurrence counts,
create new documents for each species with its count,and store these documents in a target 
database.
"""

import requests


def save_species_counts_to_db(url, source_db, target_db, view_name):
    """
    Queries a CouchDB view to fetch species occurrence counts, creates new documents for 
    each species with its count, and stores these documents in a target database.

    :param url: URL to the CouchDB instance
    :type url: str
    :param source_db: Name of the source database containing the species data
    :type source_db: str
    :param target_db: Name of the target database to store the species count documents
    :type target_db: str
    :param view_name: Name of the design document and view in the source database
    :type view_name: str
    """
    # Step 1: Query the view for species counts
    response = requests.get(
        f"{url}/{source_db}/_design/{view_name}/_view/by_taxon_name_count?group=true",
        timeout=300,
    )

    # Check if the request was successful
    if response.status_code != 200:
        print("Failed to query the view. Status Code:", response.status_code)
        print("Response:", response.text)
        return

    data = response.json()

    # Step 2: Create new documents for each species count
    for row in data.get("rows", []):
        species = row["key"]
        count = row["value"]
        doc = {"species": species, "count": count}

        # Step 3: Store the documents in the target database
        response = requests.post(f"{url}/{target_db}", json=doc, timeout=300)
        if response.status_code == 201:
            print(f"Document for {species} created successfully!")
        else:
            print(
                f"Failed to create document for {species}. Status Code: {response.status_code}"
            )


if __name__ == "__main__":
    # CouchDB credentials and URL
    URL = "http://admin:ca7uwaxa@localhost:5984"
    SOURCE_DB = "bio_blitz"
    TARGET_DB = "total_species_count"
    VIEW_NAME = "taxonomy"

    save_species_counts_to_db(URL, SOURCE_DB, TARGET_DB, VIEW_NAME)
