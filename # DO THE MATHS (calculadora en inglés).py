# DO THE MATHS (calculadora de operaciones básicas en inglés)
print ("Welcome to DO THE MATHS! The interactive calculator!")
while ("True"):
    print ("""Enter a choice:
    1) ADD UP TWO NUMBERS
    2) SUBTRACT TWO NUMBERS
    3) MULTIPLY TWO NUMBERS
    4) DIVIDE TWO NUMBERS
    5) CALCULATE PERCENTAGE
    6) EXIT""")
    choice = input ()
    
    if choice == "1":
        n1= float (input ("Enter the first number: "))
        n2= float (input ("Enter the second number: "))
        print ("The result of the ADDITION is: ", n1 + n2)
    elif choice == "2":
        a1= float (input ("Enter the first number: "))
        a2= float (input ("Enter the second number: "))
        print  ("The result of the SUBTRACTION is: ", a1 - a2)
    elif choice == "3":
        d1= float (input ("Enter the first number: "))
        d2= float (input ("Enter the second number: "))
        print  ("The result of the MULTIPLICATION is: ", d1 * d2)
    elif choice == "4":
        d1= float (input ("Enter the first number: "))
        d2= float (input ("Enter the second number: "))
        print  ("The result of the DIVISION is: ", d1 / d2)
    elif choice == "5":
        n1= float (input ("Enter the %: "))
        n2= float (input ("Enter the number: "))
        print ("The", n1, "% " "of", n2, "is:",  n1 * n2 / 100 )
    elif choice == "6":
        print ("SEE YOU! HAVE A NICE DAY!")
        break
    else:
        print ("Unknow command, TRAY AGAIN PLEASE!")