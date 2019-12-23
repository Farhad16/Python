def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Function is work")


greet("Farhad", "Hossain")


def get_greeting(name):
    return f"Hi {name}"


message = get_greeting("Farhad")
file = open("content.txt", "w")
file.write(message)

print(greet("Tahmina", "Afrin"))
