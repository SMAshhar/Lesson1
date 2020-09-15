class Student():
    def __init__(self, ID, F_name, L_name, Father_name, course):
        self.ID = ID
        self.F_name = F_name
        self.L_name = L_name
        self.Father_name = Father_name
        self.course = course
    def statment(self):
        print(f"You will be able to take classes for '{self.course}'")

