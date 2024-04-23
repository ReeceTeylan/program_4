#"write multiple line of contents into a text file"

# add input for the lines
proceed = True
while proceed:
    line = input("Enter line: ")
    break_line = line+("\n")
# open mylife.txt to store the lines
    with open("mylife.txt", "a") as life_file:
        life_file.write(break_line)
# add a loop for more lines
# finish the code
