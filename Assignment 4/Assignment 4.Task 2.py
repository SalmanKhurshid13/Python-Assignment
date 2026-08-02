# Task 2

# Take user input
data = input("Enter text to write to the file: ")

# Write data to output.txt
with open("output.txt", "w") as file:
    file.write(data + "\n")

print("Data successfully written to output.txt.")

# Take additional input
more_data = input("Enter additional text to append: ")

# Append data
with open("output.txt", "a") as file:
    file.write(more_data + "\n")

print("Data successfully appended.")

# Read and display final content
print("\nFinal content of output.txt:")

with open("output.txt", "r") as file:
    print(file.read())