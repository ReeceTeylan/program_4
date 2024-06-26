#"split integers into 2 files, odd or even"

# open numbers.txt file
with open("numbers.txt", "r") as number_file:
# read the 20 integers
    numbers = [int(line.strip()) for line in number_file.readlines()[:20]]
# open even.txt file
with open("even.txt", "w") as even_file:
# write even numbers to the file
    for num in numbers:
        if num % 2 == 0:
            even_file.write(f"{num}\n")
# open odd.txt file
with open("odd.txt", "w") as odd_file:
# write odd numbers to the file
    for num in numbers:
        if num % 2 != 0:
            odd_file.write(f"{num}\n")