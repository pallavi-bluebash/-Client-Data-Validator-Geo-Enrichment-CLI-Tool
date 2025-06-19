import re

def is_valid_postcode_locality_pair(locality, postcode):
    postcode = str(postcode).strip()
    locality = str(locality).strip()

    if not re.match(r'^[0-9]{4}$', postcode):
        return False

    if not re.match(r'^[A-Za-z\-\s]+$', locality):
        return False

    return True
