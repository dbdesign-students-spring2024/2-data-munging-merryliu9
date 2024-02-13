# Place code below to do the munging part of this assignment.

# Step 1: Read the raw data file and extract relevant data lines
with open('data/raw_data.txt', 'r') as f:
    lines = f.readlines()

# Step 2: Remove notes lines from top and bottom
start_index = None
for i in range(len(lines)):
    line = lines[i]
    if line.startswith('Year'):
        start_index = i
        break

# Step 3: Remove duplicate column headings lines
unique_lines = []
for line in lines[start_index:]:
    if line.strip() not in unique_lines:
        unique_lines.append(line.strip())

# Step 5: Handle missing data indicated with "***" & Step 6: Convert temperature anomalies from Celsius to Fahrenheit
def convert_fahrenheit(original):
    try:
        int_original = int(original)
        fahrenheit_value = (int_original / 100) * 1.8
        formatted_fahrenheit = "{:.1f}".format(fahrenheit_value)
        return formatted_fahrenheit
    except ValueError:
        return 'NaN'

# Step 8: Write cleaned data into a new CSV file
with open('data/clean_data.csv', 'w') as f:
    f.write(",".join(unique_lines[0].split()) + "\n")

    # Step 7: Standardize separator spaces if needed (optional)
    for line in unique_lines[1:-1]:
        
        # Step 4: Remove blank lines
        data = line.strip().split()
        formatted_data = []

        for index, value in enumerate(data):
            if index == 0 or index == len(data) - 1:
                formatted_data.append(value)
            else:
                formatted_data.append(convert_fahrenheit(value))

        if len(data) >= 20:
            f.write(','.join(formatted_data[:20]) + '\n')
