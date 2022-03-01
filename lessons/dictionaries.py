"""Demonstrations of dictionary capabilities."""


# Declaring the type of a dictionary
schools: dict[str, int]

# Initialize to an empty dictionary
schools = dict()

# Set a key-value pairing in the dictionary
schools["UNC"] = 19_400
schools["Duke"] = 6_717
schools["NCSU"] = 26_150

# Print a dictionary literal expression
print(schools)

# Access a value by its key -- "lookup"
print(f"UNC has {schools['UNC']} students.")

# Remove a key-value pair from a dictionary
# by its key
schools.pop("Duke")

# Test for the existence of a key
is_duke_present: bool = "Duke" in schools
print(f"Is Duke present? {is_duke_present}.")

# Dictionaries cannot have duplicate keys, but can have duplicate values

# Demonstration of dictionary literals
schools = {}  # Same as dict()

# Altenatively, initialize key-value pairs
schools = {
    "UNC": 19_400, 
    "Dukie": 6_717, 
    "NCSU": 26_150
}

# print(schools["UNCC"])

# Example looping over the keys of a dict
for school in schools:
    print(f"Key: {school} -> Value: {schools[school]}")