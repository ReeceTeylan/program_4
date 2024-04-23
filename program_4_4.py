#"create 2 seperate files with squares of even integers and cube of odd integers from a source text file"

# open the file contatining 20 integers
with open("integers.txt", "r") as integer_file:
# identify the even integers
    for line in integer_file:
        line = int(line)
        if line % 2 == 0:
# square all the even integers and place in double.txt
# cube all the odd integers and place in triple.txt