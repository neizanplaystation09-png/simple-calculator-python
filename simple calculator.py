#copyright(c) 2026
#name:simple calculator
#creator:neizan miras
#license:mit license
print("simple calculator, operators(+,-,*,/,**)")
while True:
    v1 = input("number1\n")
    operator = input("operator\n")
    v2 = input(("number2\n"))
    if operator == "+":
        output = float(v1) + float(v2)
    elif operator == "-":
        output = float(v1) - float(v2)
    elif operator == "*":
        if float(v1) == 0:
            v1 = 1
        if float(v2) == 0:
            v2 = 1
        output = float(v1) * float(v2)
    elif operator == "/":
        if float(v1) == 0:
            v1 = 1
        if float(v2) == 0:
            v2 = 1
        output = float(v1) / float(v2)
    elif operator == "**":
        if float(v1) == 0:
            v1 = 1
        if float(v2) == 0:
            v2 = 1
        output = float(v1) ** float(v2)
    else:
        print("not valid operation")
    if operator in "+-*/" or operator == "**":
        if output % 1 == 0:
            print(v1, operator, v2, "=", int(output))
        else:
            print(v1, operator, v2, "=", output)
    print("\n")
