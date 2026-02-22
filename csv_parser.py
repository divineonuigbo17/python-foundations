import csv
import operator

# Generalized function for highest or lowest
def update_extreme(score, name, extreme_score, student_list, compare):
    if extreme_score is None or compare(score, extreme_score):
        extreme_score = score
        student_list = [name]
    elif score == extreme_score:
        student_list.append(name)
    return extreme_score, student_list

# Open the CSV file
with open('data.csv', 'r') as file:
    reader = csv.DictReader(file)

    total_score = 0
    row_count = 0
    highest_score = None
    lowest_score = None
    top_students = []
    bottom_students = []

    for row in reader:
        name = row['Name']
        score = int(row['Score'])
        age = row['Age']
        weight = row['Weight']

        print(f"{name} scored {score}, is {age} years old and weighs {weight}kg")

        total_score += score
        row_count += 1

        # Update highest and lowest using the generalized function
        highest_score, top_students = update_extreme(score, name, highest_score, top_students, operator.gt)
        lowest_score, bottom_students = update_extreme(score, name, lowest_score, bottom_students, operator.lt)

# Calculate average
if row_count > 0:
    average = total_score / row_count
    print(f"Highest score: {highest_score} by {', '.join(top_students)}")
    print(f"Lowest score: {lowest_score} by {', '.join(bottom_students)}")
    print(f"Total rows: {row_count}")
    print(f"Average score: {average:.2f}")