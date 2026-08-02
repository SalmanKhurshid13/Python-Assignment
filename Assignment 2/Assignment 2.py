# Task 1

num = int(input("Enter a number: "))

if num % 2 == 0:
    print(f"{num} It is Even")
else:
    print(f"{num}It is Odd")



# Task 2

def main():
    total = 0

    for i in range(1, 51):
        total += i

    
    print("The sum of number from 1 to 50 is:", total)

if __name__ == "__main__":
    main()


