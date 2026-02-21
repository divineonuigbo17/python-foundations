import csv

# Open the CSV file
with open('data.csv', 'r') as file:
    reader = csv.DictReader(file)

    total_Score = 0
    row_count = 0

    for row in reader:
        print(f"{row['Name']} scored {row['Score']} and is {row['Age']} years old")
        total_Score += int(row['Score'])
        row_count +=1

# Calculate average
if row_count > 0:
    average = total_Score / row_count
    print(f"Total rows: {row_count}")
    print(f"Average score: {average:.2f}")
