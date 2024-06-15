import csv

def multiply_csv_time(input_file, output_file, factor):
    with open(input_file, 'r') as file:
        reader = csv.DictReader(file)
        data = list(reader)

    for row in data:
        row['Time'] = str(float(row['Time']) * factor)

    with open(output_file, 'w', newline='') as file:
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

# Usage example
input_file = 'C:/Users/juanc/Desktop/repos/dibujo-kit/sinewaveps.csv'
output_file = 'C:/Users/juanc/Desktop/repos/dibujo-kit/sinewavepsxd.csv'
factor = 1e6

multiply_csv_time(input_file, output_file, factor)