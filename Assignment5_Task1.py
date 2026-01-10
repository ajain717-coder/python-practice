# Create a dictionary with student names as keys and marks as values
students = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92
}

# Ask the user to input a student's name
name = input("Enter the student's name: ")

# Check if the student exists in the dictionary
if name in students:
    print(f"{name}'s marks: {students[name]}")
else:
    print("Student not found.")