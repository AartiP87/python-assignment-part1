# ============================================
# Student Grade Tracker (Part 1)
# ============================================

# -------------------------------
# Task 1: Cleaning raw data
# -------------------------------

raw_students = [
    {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma",       "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "  Priya Nair  ",    "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA",       "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ",    "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]

cleaned_students = []

for s in raw_students:
    # fixing name (removing extra spaces and proper format)
    name = s["name"].strip().title()

    # converting roll number to int
    roll = int(s["roll"])

    # splitting marks and converting to int list
    marks = []
    for m in s["marks_str"].split(","):
        marks.append(int(m.strip()))

    # checking if name is valid (only alphabets)
    valid = True
    for word in name.split():
        if not word.isalpha():
            valid = False
            break

    if valid:
        print(name, "✓ Valid name")
    else:
        print(name, "✗ Invalid name")

    cleaned_students.append({
        "name": name,
        "roll": roll,
        "marks": marks
    })

    # printing profile
    print("=" * 32)
    print(f"Student : {name}")
    print(f"Roll No : {roll}")
    print(f"Marks   : {marks}")
    print("=" * 32)

# special output for roll 103
for s in cleaned_students:
    if s["roll"] == 103:
        print("\nSpecial Output:")
        print(s["name"].upper())
        print(s["name"].lower())


# --------------------------------
# Task 2: Marks analysis
# --------------------------------

student_name = "Ayesha Sharma"
subjects = ["Math", "Physics", "CS", "English", "Chemistry"]
marks = [88, 72, 95, 60, 78]

print("\nSubject-wise details:")

# simple grade logic
def grade(m):
    if m >= 90:
        return "A+"
    elif m >= 80:
        return "A"
    elif m >= 70:
        return "B"
    elif m >= 60:
        return "C"
    else:
        return "F"

# printing each subject with marks and grade
for i in range(len(subjects)):
    print(subjects[i], ":", marks[i], "->", grade(marks[i]))

# total and average
total = 0
for m in marks:
    total += m

avg = round(total / len(marks), 2)

print("\nTotal:", total)
print("Average:", avg)

# highest and lowest
highest = max(marks)
lowest = min(marks)

print("Highest:", subjects[marks.index(highest)], highest)
print("Lowest:", subjects[marks.index(lowest)], lowest)


# adding new subjects using while loop
count = 0
print("\nEnter new subjects (type 'done' to stop)")

while True:
    sub = input("Subject: ")

    if sub.lower() == "done":
        break

    val = input("Marks: ")

    if not val.isdigit():
        print("Invalid input! Enter numbers only.")
        continue

    val = int(val)

    if val < 0 or val > 100:
        print("Marks should be between 0 and 100.")
        continue

    subjects.append(sub)
    marks.append(val)
    count += 1

print("\nSubjects added:", count)

new_avg = round(sum(marks) / len(marks), 2)
print("Updated average:", new_avg)


# --------------------------------
# Task 3: Class summary
# --------------------------------

class_data = [
    ("Ayesha Sharma",  [88, 72, 95, 60, 78]),
    ("Rohit Verma",    [55, 68, 49, 72, 61]),
    ("Priya Nair",     [91, 85, 88, 94, 79]),
    ("Karan Mehta",    [40, 55, 38, 62, 50]),
    ("Sneha Pillai",   [75, 80, 70, 68, 85]),
]

print("\nClass Report")
print("Name              | Average | Status")
print("----------------------------------------")

pass_c = 0
fail_c = 0
top_name = ""
top_avg = 0
total_avg = 0

for name, marks in class_data:
    avg = round(sum(marks) / len(marks), 2)
    total_avg += avg

    if avg >= 60:
        status = "Pass"
        pass_c += 1
    else:
        status = "Fail"
        fail_c += 1

    if avg > top_avg:
        top_avg = avg
        top_name = name

    print(f"{name:<18} | {avg:^7} | {status}")

class_avg = round(total_avg / len(class_data), 2)

print("\nPassed:", pass_c)
print("Failed:", fail_c)
print("Topper:", top_name, top_avg)
print("Class Average:", class_avg)


# --------------------------------
# Task 4: String operations
# --------------------------------

essay = "  python is a versatile language. it supports object oriented, functional, and procedural programming. python is widely used in data science and machine learning.  "

# removing spaces
clean_essay = essay.strip()
print("\nClean Essay:\n", clean_essay)

# title case
print("\nTitle Case:\n", clean_essay.title())

# counting 'python'
print("\nCount of 'python':", clean_essay.count("python"))

# replacing word
new_text = clean_essay.replace("python", "Python 🐍")
print("\nReplaced Text:\n", new_text)

# splitting sentences
sentences = clean_essay.split(". ")
print("\nSentence list:\n", sentences)

# printing numbered sentences
print("\nNumbered sentences:")
i = 1
for s in sentences:
    if not s.endswith("."):
        s += "."
    print(i, ".", s)
    i += 1
