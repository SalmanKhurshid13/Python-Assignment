def calculate():
    expression = entry.get()

    try:
        if "+" in expression:
            parts = expression.split("+")
            answer = float(parts[0]) + float(parts[1])

        elif "-" in expression:
            parts = expression.split("-")
            answer = float(parts[0]) - float(parts[1])

        elif "*" in expression:
            parts = expression.split("*")
            answer = float(parts[0]) * float(parts[1])

        elif "/" in expression:
            parts = expression.split("/")

            if float(parts[1]) == 0:
                raise ZeroDivisionError

            answer = float(parts[0]) / float(parts[1])

        else:
            answer = expression

        entry.delete(0, END)
        entry.insert(0, str(answer))

    except ZeroDivisionError:
        entry.delete(0, END)
        entry.insert(0, "Cannot divide by zero")

    except:
        entry.delete(0, END)
        entry.insert(0, "Invalid Input")