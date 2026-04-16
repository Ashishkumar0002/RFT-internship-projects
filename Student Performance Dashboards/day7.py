from csv import DictReader, DictWriter
from pathlib import Path
from statistics import mean


CSV_FILE = Path(__file__).with_name("studentdata.csv")
OUTPUT_FILE = Path(__file__).with_name("studentdata_with_grades.csv")
SUBJECTS = ["MATHS", "SCIENCE", "ENGLISH"]


def calculate_grade(average_marks: float) -> str:
	if average_marks >= 90:
		return "A+"
	if average_marks >= 80:
		return "A"
	if average_marks >= 70:
		return "B"
	if average_marks >= 60:
		return "C"
	return "D"


def load_students(csv_path: Path):
	students = []

	with csv_path.open(newline="", encoding="utf-8") as file_handle:
		reader = DictReader(file_handle)

		for row in reader:
			marks = {subject: int(row[subject]) for subject in SUBJECTS}
			total_marks = sum(marks.values())
			average_marks = total_marks / len(SUBJECTS)

			students.append(
				{
					"name": row["NAME"],
					**marks,
					"total": total_marks,
					"average": round(average_marks, 2),
					"grade": calculate_grade(average_marks),
				}
			)

	return students


def write_enriched_csv(students, output_path: Path):
	fieldnames = ["NAME", *SUBJECTS, "TOTAL", "AVERAGE", "GRADE"]

	with output_path.open("w", newline="", encoding="utf-8") as file_handle:
		writer = DictWriter(file_handle, fieldnames=fieldnames)
		writer.writeheader()

		for student in students:
			writer.writerow(
				{
					"NAME": student["name"],
					"MATHS": student["MATHS"],
					"SCIENCE": student["SCIENCE"],
					"ENGLISH": student["ENGLISH"],
					"TOTAL": student["total"],
					"AVERAGE": f'{student["average"]:.2f}',
					"GRADE": student["grade"],
				}
			)


def print_student_table(students):
	header = f"{'NAME':<12}{'MATHS':>8}{'SCIENCE':>10}{'ENGLISH':>10}{'TOTAL':>8}{'AVG':>8}{'GRADE':>8}"
	print(header)
	print("-" * len(header))

	for student in students:
		print(
			f"{student['name']:<12}"
			f"{student['MATHS']:>8}"
			f"{student['SCIENCE']:>10}"
			f"{student['ENGLISH']:>10}"
			f"{student['total']:>8}"
			f"{student['average']:>8.2f}"
			f"{student['grade']:>8}"
		)


def print_summary(students):
	averages = [student["average"] for student in students]
	class_average = round(mean(averages), 2)
	topper_average = max(averages)
	toppers = [student["name"] for student in students if student["average"] == topper_average]
	above_average_count = sum(1 for student in students if student["average"] > class_average)

	print()
	print(f"Class average: {class_average:.2f}")
	print(f"Students above class average: {above_average_count}")
	print(f"Topper: {', '.join(toppers)} with {topper_average:.2f}")

	print()
	print("Subject-wise averages:")
	for subject in SUBJECTS:
		subject_average = round(mean(student[subject] for student in students), 2)
		print(f"  {subject}: {subject_average:.2f}")


def main():
	students = load_students(CSV_FILE)
	write_enriched_csv(students, OUTPUT_FILE)
	print_student_table(students)
	print_summary(students)
	print()
	print(f"Enriched CSV saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
	main()

