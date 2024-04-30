from db import get_redis_connection
from classes import csvData

if __name__ == "__main__":
    r = get_redis_connection()
    csv_file = r"C:\Users\Bryan\Documents\BigData\netflix_titles.csv"  

    processor = csvData(csv_file)
    csv_data = processor.fetch_data_from_csv()
    processor.store_data_in_redis(csv_data)