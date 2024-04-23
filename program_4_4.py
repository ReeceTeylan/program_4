#"create 2 seperate files with squares of even integers and cube of odd integers from a source text file"

# open the file contatining 20 integers
with open("integers.txt", "r") as integer_file:
# identify the even integers
    for line in integer_file:
        line = int(line)
        if line % 2 == 0:
# square all the even integers and place in double.txt
            square_number = line ** 2
            with open("double.txt", "a") as squared_file:
                squared_file.write(str(square_number)+"\n")
# cube all the odd integers and place in triple.txt
        else:
            cube_number = line ** 3
            with open("triple.txt", "a") as cubed_file:
                cubed_file.write(str(cube_number)+"\n")