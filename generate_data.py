import csv
import random
import sys

############################################################
# Example: python3 ./generate_data.py <CSV_FILENAME.csv>
# python3 ./generate_data.py csv_input_file.csv
############################################################

csv_file = sys.argv[1]
# csv_file = "csv_input_file.csv"
csv_file_output = 'output_file.csv'
NUMBER_OF_ROWS = 500
columns = {}
new_columns = {}

with open(csv_file, mode='r', newline='') as file:
    csv_reader = csv.DictReader(file)

    for column_name in csv_reader.fieldnames:
        columns[column_name] = []

    for row in csv_reader:
        for column_name in csv_reader.fieldnames:
            columns[column_name].append(row[column_name].strip())

for column_name, row in columns.items():
    row = [x for x in row if x]
    new_row = [x for x in row if x][1:]
    split_row = row[0].split("-")

    # Generate nums
    if len(split_row) == 2:
        if split_row[0].isdigit() and split_row[1].isdigit():
            num_1, num_2 = split_row

            for i in range(NUMBER_OF_ROWS):
                generated_number = random.randint(int(num_1), int(num_2))
                new_row.append(generated_number)
            new_columns[column_name] = new_row
    # Generate strings
    else:
        row = [x for x in row if x]
        # Skip date column
        if column_name == "Date":
            new_columns[column_name] = row

        else:
            while len(row) < NUMBER_OF_ROWS:
                row.append(random.choice(row))
            new_columns[column_name] = row

with open(csv_file_output, mode='w', newline='') as file:
    writer = csv.writer(file)

    # Write the header (column names)
    writer.writerow(new_columns.keys())

    # Write the rows (values)
    rows = zip(*new_columns.values())
    writer.writerows(rows)

for key, value in new_columns.items():
    if key == "Date":
        continue

    current_row = {}
    current_row_unique = [x for x in value if x not in current_row]

    for current_element in current_row_unique:
        element_count = value.count(current_element)
        current_row[current_element] = element_count

    if isinstance(value[0], str):
        print()
        print(key)

    for k, v in sorted(current_row.items(), key=lambda x: x[1]):
        if isinstance(k, int):
            continue

        print(f"{k}: {v}")


