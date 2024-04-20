#"split integers into 2 files, odd or even"

# open numbers.txt file
with open("numbers.txt", "r") as number_file:
# read the 20 integers
    numbers = [int(line.strip()) for line in number_file.readlines()[:20]]
# open even.txt file
# write even numbers to the file
# open odd.txt file
# write odd numbers to the file