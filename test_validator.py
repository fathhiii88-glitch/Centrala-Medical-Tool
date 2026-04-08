import unittest
from validator import CSVValidator
import os

class TestValidator(unittest.TestCase):

    def setUp(self):
        self.validator = CSVValidator()
        with open("valid.csv", "w") as f:
            f.write("batch_id,timestamp,reading1,reading2,reading3,reading4,reading5,reading6,reading7,reading8,reading9,reading10\n")
            f.write("1,14:01:04,1,2,3,4,5,6,7,8,9,1\n")

        with open("bad_header.csv", "w") as f:
            f.write("wrong,header\n")

        with open("duplicate.csv", "w") as f:
            f.write("batch_id,timestamp,reading1,reading2,reading3,reading4,reading5,reading6,reading7,reading8,reading9,reading10\n")
            f.write("1,14:01:04,1,2,3,4,5,6,7,8,9,1\n")
            f.write("1,14:01:04,1,2,3,4,5,6,7,8,9,1\n")

        with open("bad_value.csv", "w") as f:
            f.write("batch_id,timestamp,reading1,reading2,reading3,reading4,reading5,reading6,reading7,reading8,reading9,reading10\n")
            f.write("1,14:01:04,10,2,3,4,5,6,7,8,9,1\n")

        with open("bad_length.csv", "w") as f:
            f.write("batch_id,timestamp,reading1,reading2,reading3,reading4,reading5,reading6,reading7,reading8,reading9,reading10\n")
            f.write("1,14:01:04,1,2,3\n")

        open("empty.csv", "w").close()

    def test_valid_file(self):
        result = self.validator.validate_file("valid.csv")
        self.assertTrue(result)

    def test_invalid_header(self):
        result= self.validator.validate_file("bad_header.csv")
        self.assertFalse(result)

    def test_duplicate_batch(self):
        result = self.validator.validate_file("duplicate.csv")
        self.assertFalse(result)

    def test_invalid_value(self):
        result = self.validator.validate_file("bad_value.csv")
        self.assertFalse(result)
    def test_row_length(self):
         result = self.validator.validate_file("bad_length.csv")
         self.assertFalse(result)

    def test_empty_file(self):
        result= self.validator.validate_file("empty.csv")
        self.assertFalse(result)

    def tearDown(self):
        files = ["valid.csv", "bad_header.csv", "duplicate.csv", "bad_value.csv", "empty.csv"]
        files = ["valid.csv", "bad_header.csv", "duplicate.csv", "bad_value.csv", "empty.csv", "bad_length.csv"]
        for f in files:
            if os.path.exists(f):
                os.remove(f)

if __name__ == "__main__":
    unittest.main()