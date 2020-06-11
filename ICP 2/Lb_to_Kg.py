"""
Write a program, which reads weights (lbs.) of N students into a list and convert these weights to kilograms in a separate list using:
1) Loops and
2) List comprehensions
N: No of students (Read input from user)
Ex: 	L1: [150,155, 145, 148]
Output: [68.03, 70.3, 65.77, 67.13]
"""

students_count = int(input("Enter the Number of Students:"))
lb_list = []
kg_list = []

# using loops
for x in range(1, students_count+1):
    elem = int(input(f"Enter the Student {x} weight:"))
    lb_list.append(elem)
    kg_list.append(elem * 0.453592)  # appending the elements to list directly
print("\nUsing Loops:")
print(lb_list)
print(kg_list)

kg_list = []
for x in range(0, len(lb_list)):  # Iterating the array in which the input elements are stored
    kg_list.append(lb_list[x] * 0.453592)
print(kg_list)


# Using List Comprehension
print("\nUsing List Comprehension")
print(lb_list)
kg_list = [lb_list[x] * 0.453592 for x in range(0, len(lb_list))]
print(kg_list)
