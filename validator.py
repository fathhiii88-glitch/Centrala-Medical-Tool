import csv
class CSVValidator:
    def validate_file(self, filename):
        print(f"Validating {filename}...")
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            try:
                headers = next(reader)
            except:
                print("Missing header")
                return False
            required = ["batch_id","timestamp"] + [f"reading{i}" for i in range(1,11)]
            if headers != required:
                print("Invalid headers")
                return False
            batch_ids = set()   
            for row in reader:
                if len(row) != 12:
                    print("Invalid row length")
                    return False
                if row[0] in batch_ids:
                    print("Duplicate batch_id found")
                    return False
                batch_ids.add(row[0])
                try:
                    values = [float(x) for x in row[2:]]
                    if any(v > 9.999 for v in values):
                        print("Value out of range")
                        return False
                except:
                    print("Invalid data type")
                    return False
        print("File is valid")
        return True
if __name__ == "__main__":
    validator = CSVValidator()
    validator.validate_file("test.csv")
      # Added for commit history screenshot
 # Added for commit history screenshot again
