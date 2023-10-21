"""
This module provides functionality to convert TSV (Tab-Separated Values) files 
to CSV (Comma-Separated Values) files.

It includes the following main functions:
- tsv_to_csv: Converts a single TSV file to a CSV file.
- convert_all_tsv_to_csv: Converts all TSV files in a specified directory to CSV format.

When run as a standalone script, this module will prompt the user for a directory path and convert 
all TSV files in that directory to CSV format.
"""

import csv
import os


def _convert_file(input_file_path, output_file_path, encoding):
    """
    Convert a file from TSV format to CSV format using the specified encoding.

    Parameters:
    - input_file_path (str): Path to the input TSV file.
    - output_file_path (str): Path to save the converted CSV file.
    - encoding (str): Character encoding to be used (e.g., 'utf-8' or 'ISO-8859-1').
    """
    with open(input_file_path, 'r', newline='', encoding=encoding) as tsv_file:
        with open(output_file_path, 'w', newline='', encoding=encoding) as csv_file:
            tsv_reader = csv.reader(tsv_file, delimiter='\t')
            csv_writer = csv.writer(csv_file)
            for row in tsv_reader:
                csv_writer.writerow(row)


def tsv_to_csv(input_file_path, output_file_path):
    """
    Convert a TSV file to a CSV file.

    Parameters:
    - input_file_path (str): Path to the input TSV file.
    - output_file_path (str): Path to save the output CSV file.

    Note: This function tries to open the TSV file with UTF-8 encoding initially.
          If a UnicodeDecodeError occurs, it switches to ISO-8859-1 encoding.
    """
    try:
        _convert_file(input_file_path, output_file_path, 'utf-8')
    except UnicodeDecodeError:
        _convert_file(input_file_path, output_file_path, 'ISO-8859-1')


def convert_all_tsv_to_csv(directory_path):
    """
    Convert all TSV files present in the specified directory to CSV format.

    Parameters:
    - directory_path (str): Path to the directory containing TSV files.

    Note: This function scans the directory for TSV files and for each found TSV file, 
          it generates a CSV file in the same directory.
    """
    for filename in os.listdir(directory_path):
        if filename.endswith(".tsv"):
            input_path = os.path.join(directory_path, filename)
            output_path = os.path.join(directory_path, filename.replace(".tsv", ".csv"))
            tsv_to_csv(input_path, output_path)
            print(f"Converted {input_path} to {output_path}")


def main():
    """
    Main execution function for the script.
    
    Prompts the user for a directory path and then converts all TSV files within that directory 
    to CSV format.
    """
    dir_path = input("Enter the directory path containing TSV files: ")
    convert_all_tsv_to_csv(dir_path)


if __name__ == "__main__":
    main()