# test.py

import sys
import json

# Read JSON input from PHP
input_data = json.loads(sys.stdin.read())

# Process the input data (for demonstration, just square each number)
output_data = input_data


# Output the result as JSON
print(json.dumps(output_data))
