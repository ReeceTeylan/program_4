#"output  the student with highest GWA from reading a file"
import pyfiglet
import time
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
text = pyfiglet.figlet_format(f"The student with the highest GWA is {name} who received  {grade}")
final_text = (f"\033[38;5;157m{text}\033[0m")
for char in final_text:
        print(char, end="", flush=True)
        time.sleep(0.003)
# add design to output
