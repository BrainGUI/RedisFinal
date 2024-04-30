import csv
from itertools import islice
from db import get_redis_connection

class csvData:
    """A class to read CSV data and store it in Redis."""

    def __init__(self, csv_file):
        """
        Initialize the class with the CSV file path.

        Args:
            csv_file (str): The path to the CSV file.
        """
        self.csv_file = csv_file
        self.redis_conn = get_redis_connection()

    def fetch_data_from_csv(self, limit=None):
        """Read data from the CSV file."""
        with open(self.csv_file, "r", newline="", encoding="utf-8", errors="replace") as file: 
            reader = csv.DictReader(file)
            if limit:
                return list(islice(reader, limit))
            else:
                return list(reader)

    def store_data_in_redis(self, data):
        """Store data in Redis."""
        for item in data:
            key = f"show:{item['show_id']}_{item['type']}"
            self.redis_conn.hmset(key, item)