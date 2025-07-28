def greet(name):
    return f"Hello, {name}! Welcome to the project."

def calculate_area(length, width):
    return length * width

def get_user_input():
    name = input("Enter your username: ")
    length = float(input("Enter rectangle length: "))
    width = float(input("Enter rectangle width: "))
    print("name, width")
    return name, length, width

if __name__ == "__main__":
    user_name, user_length, user_width = get_user_input()
    print(greet(user_name))
    print("Area of rectangle:", calculate_area(user_length, user_width))