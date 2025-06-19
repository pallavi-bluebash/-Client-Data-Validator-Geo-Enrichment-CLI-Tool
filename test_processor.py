import unittest
from unittest.mock import patch, mock_open
from processor import process_csv

class TestProcessor(unittest.TestCase):
    @patch("geocoder.get_coordinates")
    def test_process_csv_valid(self, mock_geo):
        mock_geo.return_value = (-33.86, 151.21)
        sample_csv = """Email,First Name,Last Name,Residential Address Street,Residential Address Locality,Residential Address State,Residential Address Postcode,Postal Address Street,Postal Address Locality,Postal Address State,Postal Address Postcode
john@example.com,John,Doe,12 Argyle St,SYDNEY,NSW,2000,12 Argyle St,SYDNEY,NSW,2000
"""
        result = process_csv(mock_open(read_data=sample_csv)())
        self.assertIn("john@example.com", result)
        self.assertIn("latitude", result)
        self.assertIn("longitude", result)

    @patch("geocoder.get_coordinates")
    def test_process_csv_missing_fields(self, mock_geo):
        mock_geo.return_value = (-33.86, 151.21)
        sample_csv = """Email,First Name,Last Name,Residential Address Street,Residential Address Locality,Residential Address State,Residential Address Postcode,Postal Address Street,Postal Address Locality,Postal Address State,Postal Address Postcode
jane@example.com,Jane,,12 Argyle St,SYDNEY,NSW,2000,12 Argyle St,SYDNEY,NSW,2000
"""
        result = process_csv(mock_open(read_data=sample_csv)())
        self.assertNotIn("jane@example.com", result)

    @patch("geocoder.get_coordinates")
    def test_process_csv_invalid_postcode(self, mock_geo):
        mock_geo.return_value = (-33.86, 151.21)
        sample_csv = """Email,First Name,Last Name,Residential Address Street,Residential Address Locality,Residential Address State,Residential Address Postcode,Postal Address Street,Postal Address Locality,Postal Address State,Postal Address Postcode
bob@example.com,Bob,Smith,12 Argyle St,SYDNEY,NSW,99999,12 Argyle St,SYDNEY,NSW,2000
"""
        result = process_csv(mock_open(read_data=sample_csv)())
        self.assertNotIn("bob@example.com", result)

    @patch("processor.get_coordinates")
    def test_process_csv_failed_geocode(self, mock_geo):
        mock_geo.return_value = None
        sample_csv = """Email,First Name,Last Name,Residential Address Street,Residential Address Locality,Residential Address State,Residential Address Postcode,Postal Address Street,Postal Address Locality,Postal Address State,Postal Address Postcode
alice@example.com,Alice,Wong,12 Argyle St,SYDNEY,NSW,2000,12 Argyle St,SYDNEY,NSW,2000
"""
        result = process_csv(mock_open(read_data=sample_csv)())
        self.assertNotIn("alice@example.com", result)

if __name__ == '__main__':
    unittest.main()
