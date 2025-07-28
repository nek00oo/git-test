def greet(name):
    return f"Hello, {name}! Welcome to the project."

def greet(name):
    if not name:
        return "Hello, stranger! No name provided."
    return f"HELLO, {name.upper()}! WELCOME ABOARD!"

def calculate_area(length, width):
    return length * width

if __name__ == "__main__":
    print(greet("Alice"))
    print("Area of rectangle:", calculate_area(5, 3))