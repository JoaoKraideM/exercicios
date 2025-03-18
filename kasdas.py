def reverse_input():
    user_input = input("Enter something: ")
    reversed_input = user_input[::-1]
    print(reversed_input)

if __name__ == "__main__":
    reverse_input()