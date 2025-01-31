import os
import json
import time

class JSONDatabase:
    def __init__(self, filename="records.json"):
        self.filename = filename
        if not os.path.exists(self.filename):
            self.save_records([])  # Create an empty JSON file if it doesn't exist

    def load_records(self):
        """Load records from JSON file."""
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    def save_records(self, records):
        """Save records to JSON file."""
        with open(self.filename, "w") as file:
            json.dump(records, file, indent=4)