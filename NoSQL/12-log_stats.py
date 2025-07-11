#!/usr/bin/env python3
"""12-log_stats.py"""


from pymongo import MongoClient

def main():
    """
    Connects to the 'logs' database and 'nginx' collection to print log statistics:
    - Total number of logs
    - Number of logs for each HTTP method (GET, POST, PUT, PATCH, DELETE)
    - Number of GET requests to the /status path
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx

    total_logs = collection.count_documents({})
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    print(f"{total_logs} logs")
    print("Methods:")

    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    status_check = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check} status check")

if __name__ == "__main__":
    main()
