#"output  the student with highest GWA from reading a file"

# read the file with student names and GWA
def find_highest():
    with open("students.txt", "r") as student_file:
        info = student_file.read()
        info_list = eval(info)
        highest_gwa = None
        highest_gwa_student = None
# find the student with highest GWA
        for name, grade in info_list.items():
            float_value = float(grade)
            if highest_gwa is None or float_value < float(highest_gwa):
                highest_gwa_student = name
                highest_gwa = grade
        return highest_gwa_student, highest_gwa
name, grade = find_highest()
# output the name of the student with the highest GWA
# add design to output

