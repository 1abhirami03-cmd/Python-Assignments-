age_list =[24,25,26,27,28]
print(age_list)

name_list=["Anu","Priya","Rahul","Alen","Arun"]
print(name_list)

name_list.append("Yazhini")
print(name_list)

age_list.insert(2,30)
print(age_list)

name_list.remove("Yazhini")
print(name_list)

age_list.pop()
print(age_list)

age_list.extend([29,30,26])
print(age_list)

age_list.sort(reverse =True)
print(age_list)

max_age =max(age_list)
min_age =min(age_list)
total_age =sum(age_list)

print("Maximum age:",max_age)
print("Minimum age:",min_age)
print("sum of ages:",total_age)

print(name_list[0])
print(name_list[-1])
print(name_list[2:5])
print(name_list[::-1])

student_marks = {
    "Arun": 75,
    "Priya": 88,
    "Kavin": 92,
    "Meena": 67,
    "Rahul": 79
}
print(student_marks)

print("Arun's Mark:",student_marks["Arun"])

student_marks["Janani"] =80
print(student_marks)

print("Keys:", student_marks.keys())
print("Values:", student_marks.values())
print("Items:", student_marks.items())

my_set = {'a', 'e', 'i', 'o', 'u', 'a', 'a', 'i'}
print("My Set:", my_set)


set1 = {1, 3, 5, 7, 9}
print(set1)

set2 = {2, 3, 5, 8, 10}
print(set2)

union_set = set1.union(set2)
print("Union:", union_set)

intersection_set = set1.intersection(set2)
print("Intersection:", intersection_set)

score = int(input("Enter your score (0 to 10): "))

if score < 0 or score > 10:
    print("Invalid score. Please enter a score between 0 and 10.")

elif score > 7:
   print("Above Average: Excellent performance! Keep up the great work.")

elif score >= 4:
    print("Average: Good effort! Keep practicing, there's room for improvement.")

else:
   print("Below Average: Need to improve your performance. Consistent practice will lead to better results.")

