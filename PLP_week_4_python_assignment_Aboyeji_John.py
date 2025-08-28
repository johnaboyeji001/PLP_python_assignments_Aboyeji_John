# Reading from a file and writing modified version to new file:

with open("input.txt", "r") as f:
    content = f.read()

modified_content = content + " - Modified"

with open("output.txt", "w") as f:
    f.write(modified_content)

print("File has been modified and saved to output.txt")


# Error Handling: 

filename = input("Enter filename: ")

try:
    with open(filename, "r") as f:
        print(f.read())
except FileNotFoundError:
    print("Error: File not found")
except IOError:
    print("Error: Cannot read file")
