# Program to identify if you are enrolled or not and your data



applied = {
    "Ahmed": ["Muhammad", "Ahmed", 10, "AI"],
    "Saad": ["Muhammad", "Saad", 20, "CNC"],
    "Ali": ["Syed", "Ali", 30, "IOT"],
    "Tooba": ["Tooba", "Tanveer", 40, "BCC"],
    "Tamoor": ["Tamoor", "Khan", 50, "AI"],
    }

def new():
    print("\t\t========================================================\t\t")
    
    application = []                    # asking the persone to insert their data
    name = str(input(print("\t\t Enter your first name : ", sep = "")))
    application.append(name)
    last = application.append(str(input(print("\t\t Enter your last name : "))))
    cnic = application.append(int(input(print("\t\t Enter your CNIC : "))))
    course = application.append(str(input(print("\t\t Enter your course : "))))

    print("\t\t========================================================\t\t")

    applied[name] = application

    print("\t\t========================================================\t\t")

    print(f"\t\t {application}")                  # printing their application
   

new()




