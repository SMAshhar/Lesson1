print("\t\t==========================================================\t")
print("\t\t A Simple Calculator \t")
print("\t\t==========================================================\t")
f_no = float(input("\t\t Please Enter the first Number : \t"))
s_no = float(input("\t\t Please Enter the second Number : \t"))
print("\t\t==========================================================\t")
fnxn = input("\t\t Please enter the desired function to be performed : \t")
print("\t\t==========================================================\t")
if fnxn == "+":
    a = (f_no + s_no)
    print("\t\t The answer is = " , a)
if fnxn == "-":
    a = (f_no - s_no)
    print("\t\t The answer is = " , a)
if fnxn == "*":
    a = (f_no * s_no)
    print("\t\t The answer is = " , a)
if fnxn == "/":
    a = (f_no / s_no)
    print("\t\t The answer is = " , a)
if fnxn == "%":
    a = (f_no / s_no * 100)
    print("\t\t The answer is = " , a)