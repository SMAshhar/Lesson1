
ID = 1
All_profiles = {}
Entry = 0

def listOfOptions():

    print(
        '''
        Please select a mode
        
        1. For Profile construction
        2. For Profile Re-construction
        3. For viewing Profile
        4. For Searching Profile
        5. To exit

        '''
    )
    print("==================================================================================================")

listOfOptions()

def enterProfile():

    name = input("\t Enter your name : ")
    email = input("\t Enter your email address : ")
    phone = int(input("\t Enter your phone number : "))
    return [CNIC, name, email, phone]

def changeProfile():
    
    newName = input("\t Enter the new Name : ")
    newEmail = input("\t Enter the new Email address : ")
    newPhone = int(input("\t Enter the new phone number : "))
    return [newName, newEmail, newPhone]

while ID >= 0:

    if Entry == 0:
        print('''
        Welcome to Profile Management. Enter any key to continue (l to list, q to quit):
        '''
        )
        print("==================================================================================================")
        continuition = input("\t")
        Entry = 1

    else:
        continuition = input("\t Press Enter to continue (l to list options, q to quit)")
        print("==================================================================================================")

    if continuition == "q" or  continuition == "Q":
        print("**************************************************************************************************")
        break

    if continuition == "l" or continuition == "L":
        listOfOptions()
        print("==================================================================================================")

    choice = input("\t Please enter your choice : ")

    
    if choice == "1":
        CNIC = int(input("\t Enter CNIC Number : "))   
        if CNIC in All_profiles.keys():
            print("\t Profile already exist")
                
        else:
            x = enterProfile()
            All_profiles[x[0]] = x
            
            print("==================================================================================================")

    elif choice == "2":
        profileToChange = int(input("\t Enter CNIC to change your profile : "))

        if profileToChange in All_profiles.keys():
            for ids in All_profiles:
                if ids == profileToChange:
                    x = changeProfile()
                    All_profiles[profileToChange] = x
                    print("==================================================================================================")

        else:
            print("\t Profile not found")
            print("==================================================================================================")
                    
    elif choice == "3":
        print("\t", All_profiles)
        print("==================================================================================================")
    
    elif choice == "4":
        idSearch = int(input("\t Please enter CNIC to search your profile: "))
        if idSearch in All_profiles.keys():
            print("\t ", All_profiles[idSearch])
            print("==================================================================================================")

        else:
            print("\t No profile registered under this CNIC : ")
            print("==================================================================================================")
    
    elif choice == "5":
        print("\t ****Good Bye****")
        print("==================================================================================================")
        break
    
    else:
        print("\t Invalid Selection")
        print("==================================================================================================")
    
