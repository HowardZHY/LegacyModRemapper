import os
import subprocess

# Read the content of info.txt
with open('run.txt', 'r') as file:
    lines = file.readlines()

# Extracting values from the file
version = lines[0].strip()
input_jar = lines[1].strip()
output_jar = lines[2].strip()

# Construct the command
command = [
    'java', '-jar', 'SpecialSource.jar',
    '--in-jar', input_jar,
    '--out-jar', output_jar,
    '--read-inheritance', f'{version}.srg.inheritmap',
    '--srg-in', f'{version}.srg'
]

# Execute the command
result = subprocess.run(command, capture_output=True, text=True)

# Print the result
print(f"Return code: {result.returncode}")
print(f"Output: {result.stdout}")
print(f"Error: {result.stderr}")
