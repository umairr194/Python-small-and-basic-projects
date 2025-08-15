history_file = "history.text"

def show_history():
    file = open(history_file, 'r')
    lines = file.readlines()
    if len(lines) == 0:
        print("no history found")
    else:
        for line in reversed(lines):
            print(line.strip())
    file.close()

def clear_history():
    file = open(history_file, 'w')
    file.close()
    print("history is clear")

def save_history(equation, result):
    file = open(history_file, 'a')
    file.write(equation + "=" + str(result) + "\n")
    file.close()

def calculate(user_input):
    parts = user_input.split()
    if len(parts) != 3:
        print("invalid input write 2 + 5 in this forms")
        return
    
    try:
        num1 = float(parts[0])
        op = parts[1]
        num2 = float(parts[2])
    except ValueError:
        print("invalid numbers")
        return
    
    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 == 0:
            print("cannot divide by zero")
            return
        result = num1 / num2
    else:
        print("invalid operation only use (+,-,*,/)")
        return
    
    if int(result) == result:
        result = int(result)
    print("result is:", result)
    save_history(user_input, result)

def main():
    print("-----welcome to my history calculator------")
    while True:
        user_input = input("enter calculation (+,-,*,/) or command (history,clear,exit): ")
        if user_input == "exit":
            print("good bye: have a good day")
            break
        elif user_input == "history":
            show_history()
        elif user_input == "clear":
            clear_history()
        else:
            calculate(user_input)

main()