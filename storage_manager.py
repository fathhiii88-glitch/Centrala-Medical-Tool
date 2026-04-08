import os
import shutil
from datetime import datetime

class StorageManager:
    def __init__(self, base_folder="data"):
        self.base_folder = base_folder

    def save_file(self, file_name):
        folder = datetime.now().strftime("%Y-%m-%d")
        path = os.path.join(self.base_folder, folder)

        os.makedirs(path, exist_ok=True)

        new_path = os.path.join(path, file_name)
        
        shutil.copy(file_name, new_path)
        print(f"File saved to {new_path}")


if __name__ == "__main__":
    storage = StorageManager()
    storage.save_file("test.csv")