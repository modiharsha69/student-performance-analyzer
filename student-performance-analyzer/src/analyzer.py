import matplotlib.pyplot as plt
import pandas as pd
import os

project_folder = os.path.dirname(os.path.dirname(__file__))
file_path = os.path.join(project_folder, "data", "students.csv")

data = pd.read_csv(file_path)

data["Average"] = data[["Python", "Java", "Math", "AI_ML"]].mean(axis=1)

print(data)
top_student = data.loc[data["Average"].idxmax()]

print("\nTop Student:")
print(top_student)
subjects = ["Python", "Java", "Math", "AI_ML"]

subject_average = data[subjects].mean()

print("\nSubject-wise Average:")
print(subject_average)
best_subject = subject_average.idxmax()

print("\nBest Subject:")
print(best_subject)
# Check pass or fail
data["Result"] = data[subjects].min(axis=1).apply(
    lambda x: "Pass" if x >= 40 else "Fail"
)

print("\nStudent Results:")
print(data[["Name", "Average", "Result"]])
# Subject-wise performance chart
subject_average.plot(kind="bar")

plt.title("Subject-wise Average Marks")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")
plt.ylim(0, 100)
plt.tight_layout()

output_file = os.path.join(project_folder, "output", "subject_average.png")

plt.savefig(output_file)
plt.show()
# Student performance chart
plt.figure()

plt.bar(data["Name"], data["Average"])

plt.title("Student Average Performance")
plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.ylim(0, 100)

plt.xticks(rotation=45)
plt.tight_layout()

student_chart = os.path.join(
    project_folder, "output", "student_performance.png"
)

plt.savefig(student_chart)
plt.show()
# Search for a student
search_name = input("\nEnter student name to search: ")

result = data[data["Name"].str.lower() == search_name.lower()]

if not result.empty:
    print("\nStudent Details:")
    print(result[["Name", "Average", "Result"]])
else:
    print("\nStudent not found.")
