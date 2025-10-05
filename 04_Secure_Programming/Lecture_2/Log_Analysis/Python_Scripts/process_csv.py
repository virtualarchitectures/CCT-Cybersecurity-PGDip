import csv

def process_csv_file(file_path):
    """
    Reads a CSV file and processes its data.
    """
    try:
        with open(file_path, 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
                #Example processing:
                if len(row) > 1:
                    print(f"Column 1: {row[0]}, Column 2: {row[1]}")
    except FileNotFoundError:
        print(f"Error: CSV file '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    process_csv_file("logfile.csv")
