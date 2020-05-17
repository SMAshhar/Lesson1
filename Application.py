# Program to enroll yourself and give you a roll number



applied = {
    "PIAIC1": ["Muhammad", "Ahmed", 10, "AI"],
    "PIAIC2": ["Muhammad", "Saad", 20, "CNC"],
    "PIAIC3": ["Syed", "Ali", 30, "IOT"],
    "PIAIC4": ["Tooba", "Tanveer", 40, "BCC"],
    "PIAIC5": ["Tamoor", "Khan", 50, "AI"],
    }

def new():
    print("\t\t========================================================\t\t")
    
    application = []                    # asking the persone to insert their data
    name = input("\t\t Enter your first name : ")
    application.append(name)
    last = input("\t\t Enter your last name : ")
    application.append(last)
    fname = input("\t\t Enter your Fathre's name : ")
    application.append(fname)
    cnic = input("\t\t Enter your CNIC : ")
    application.append(cnic)
    course = input("\t\t Enter your course : ")
    application.append(course)

    print("\t\t========================================================\t\t")

    rno = len(applied)                  # assigning roll number
    applied[rno] = application          # inserting in dictionary

    print("\t\t========================================================\t\t")

    print(f"\t\t {application}")         # printing their application and issuing card
                                
    card = f"""                        
    \t\tName = {name} {last}
    \t\tFather's Name = {fname}
    \t\tCNIC = {cnic}
    \t\tCourse Applied = {course}
    \t\tR. No = PIAIC{rno}


    \t\tPlease remember your assigned PIAIC roll number
    \t\t========================================================\t
    """

    return card

# new()

choice = str(input("\t\tPlease enter if you want to : \n 1) Fresh enrollment \n 2) Knowing if you are enrolled"))

if choice == "1":
    x = new()
    print(x)

if choice == "2":
    x = str(input("\t\tEnter your PIAIC issued number"))
    if x in applied:
        print("\t\t===================================\t\t")
        print("\t\tCongradulations, you are enrolled")
        print("\t\t===================================\t\t")
    else:
        print("\t\t=======================\t\t")
        print("\t\tBetter luck next time")
        print("\t\t=======================\t\t")


