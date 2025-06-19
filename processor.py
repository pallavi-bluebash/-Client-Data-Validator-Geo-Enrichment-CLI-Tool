import csv
import sys
from io import StringIO
from geocoder import get_coordinates
from utils import is_valid_postcode_locality_pair

def process_csv(file):
    reader = csv.DictReader(file)
    output = StringIO()

    # Desired output column format
    fieldnames = [
        "email", "first_name", "last_name",
        "res_street", "res_city", "res_state", "res_postcode",
        "post_street", "post_city", "post_state", "post_postcode",
        "latitude", "longitude"
    ]
    writer = csv.DictWriter(output, fieldnames=fieldnames)
    writer.writeheader()

    for i, row in enumerate(reader, start=1):
        # Clean postcode formatting (e.g., 4802.0 -> 4802)
        try:
            row['Residential Address Postcode'] = str(int(float(row['Residential Address Postcode'])))
            row['Postal Address Postcode'] = str(int(float(row['Postal Address Postcode'])))
        except Exception:
            continue

        if not all([row['Email'], row['First Name'], row['Last Name'],
                    row['Residential Address Street'], row['Residential Address Locality'],
                    row['Residential Address State'], row['Residential Address Postcode'],
                    row['Postal Address Street'], row['Postal Address Locality'],
                    row['Postal Address State'], row['Postal Address Postcode']]):
            continue

        if not is_valid_postcode_locality_pair(row['Residential Address Locality'], row['Residential Address Postcode']):
            continue

        if not is_valid_postcode_locality_pair(row['Postal Address Locality'], row['Postal Address Postcode']):
            continue

        res_full = f"{row['Residential Address Street']}, {row['Residential Address Locality']}, {row['Residential Address State']}, {row['Residential Address Postcode']}"
        res_coords = get_coordinates(res_full)

        if not res_coords:
            continue

        # Build formatted output row
        output_row = {
            "email": row["Email"],
            "first_name": row["First Name"],
            "last_name": row["Last Name"],
            "res_street": row["Residential Address Street"],
            "res_city": row["Residential Address Locality"],
            "res_state": row["Residential Address State"],
            "res_postcode": row["Residential Address Postcode"],
            "post_street": row["Postal Address Street"],
            "post_city": row["Postal Address Locality"],
            "post_state": row["Postal Address State"],
            "post_postcode": row["Postal Address Postcode"],
            "latitude": res_coords[0],
            "longitude": res_coords[1],
        }

        writer.writerow(output_row)

    return output.getvalue()

