import csv

with open("employee_birthday.csv") as csv_file:
    csv_file = csv.reader(csv_file, delimiter=",")
    line_count = 0
    for row in csv_file:
        if line_count == 0:
            print(f'Column Names are {", ".join(row)}')
            line_count += 1
        else:
            print(
                f"{row[0]} works in {row[1]} department and birthday is in {row[2]} month"
            )
            line_count += 1
