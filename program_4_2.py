#"output  the student with highest GWA from reading a file"

# read the file with student names and GWA
def find_highest():
    with open("students.txt", "r") as student_file:
        info = student_file.read()
        info_list = eval(info)
        highest_gwa = None
        highest_gwa_student = None
# find the student with highest GWA
# output the name of the student with the highest GWA
# add design to output

