def greet(name):
    if not name:
        return "Hello, stranger! No name provided."
    print("Hiiii")
    return f"HELLO, {name.upper()}! WELCOME ABOARD!"

def calculate_area(length, width):
    return length * width

def get_user_input():
    name = input("Enter your name: ")
    length = float(input("Enter rectangle length: "))
    width = float(input("Enter rectangle width: "))
    return name, length, width

if __name__ == "__main__":
    user_name, user_length, user_width = get_user_input()
    print(greet(user_name))
    print("Area of rectangle:", calculate_area(user_length, user_width))