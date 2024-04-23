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
        while proceed:
            again = input("Are there more lines y/n? ")
# finish the code
            if again.lower() == "y":
                break
            elif again.lower() == "n":
                print ("Thanks")
                proceed = False
            else:
                print("Type y/n only!")
                continue
