import csv
from pathlib import Path

CSV_FILE_PATH = 'files.csv'


def save_file_data(filename, url):
    file_exists = Path(CSV_FILE_PATH).is_file()

    with open(CSV_FILE_PATH, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["filename", "url"])
        writer.writerow([filename, url])


def read_file_data():
    data = []
    if Path(CSV_FILE_PATH).is_file():
        with open(CSV_FILE_PATH, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
    return data
