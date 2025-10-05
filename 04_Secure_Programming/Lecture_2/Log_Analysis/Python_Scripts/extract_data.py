import csv

def extract_data(csv_file, output_file):
    """
    Extracts data from a CSV file and writes them to a new file.
    Args:
    csv_file (str): Path to the CSV file.
    output_file (str): Path to the output file.
    """
    try:
        with open(csv_file, 'r', newline='') as infile, open(output_file, 'w') as outfile:
            reader = csv.reader(infile)
            for row in reader:
                if row: # Check if the row is not empty
                    outfile.write(row[0] + '\n') # Assuming data are in the first column
        print(f"Data extracted to {output_file}")
    except FileNotFoundError:
        print(f"Error: CSV file '{csv_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    extract_data('logfile.csv', 'data_extract.txt')
