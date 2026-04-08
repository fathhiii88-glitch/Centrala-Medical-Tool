from validator import CSVValidator
from logger import Logger
from storage_manager import StorageManager

def main():
    print("=== STARTING SYSTEM ===")

    validator = CSVValidator()
    logger = Logger()
    storage = StorageManager()
    processed_files = set()

    files = ["test.csv"]

    for file in files:

        if file in processed_files:
            print(f"Skipping duplicate file: {file}")
            continue

        processed_files.add(file)

        print(f"Processing {file}...")

        try:
            is_valid = validator.validate_file(file)

            if is_valid:
                storage.save_file(file)
            else:
                logger.log(f"Invalid file: {file}")

        except Exception as e:
            logger.log(f"Error processing {file}: {e}")

    print("=== SYSTEM FINISHED ===")

if __name__ == "__main__":
    main()

    # Added for commit history screenshot