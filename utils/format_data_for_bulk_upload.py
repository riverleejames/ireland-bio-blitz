"""
Figure 1: Format data for bulk upload
This script reads data from a JSON file, formats it for CouchDB bulk upload, 
and then writes the formatted data to another JSON file.

Attributes:
    INPUT_FILE_PATH (str): Path to the input JSON file containing raw data.
    OUTPUT_FILE_PATH (str): Path to the output JSON file where the formatted data will be written.
"""

import json

INPUT_FILE_PATH = "../dataset/IrelandsBioBlitz.json"
OUTPUT_FILE_PATH = "../dataset/formatted_data_for_bulk_upload.json"


def format_data_for_couchdb(input_path, output_path):
    """
    Reads data from the input JSON file, formats it for CouchDB bulk upload,
    and writes the formatted data to the output JSON file.

    Args:
        input_path (str): Path to the input JSON file.
        output_path (str): Path to the output JSON file.
    """

    # Read the data from the input JSON file
    with open(input_path, "r", encoding="utf-8") as infile:
        raw_data = json.load(infile)

    # Format the data for CouchDB bulk upload
    formatted_data = {"docs": raw_data}

    # Write the formatted data to the output JSON file
    with open(output_path, "w", encoding="utf-8") as outfile:
        json.dump(formatted_data, outfile)


if __name__ == "__main__":
    format_data_for_couchdb(INPUT_FILE_PATH, OUTPUT_FILE_PATH)
