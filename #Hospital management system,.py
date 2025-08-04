#hospital management system
patients=[]
def add_patients():
    name=input("Enter patient's full name: ")
    age=input("Enter patient's age: ")
    gender=input("Enter patient's gender(M/F): ").lower()
    problem=input("Enter patient's problem: ")
    patient={
        "Name": name,
        "Age": age,
        "Gender": gender,
        "Problem": problem
    }
    patients.append(patient)
    print("Patient added successfull!")
def view_patients():
    if not patients:
        print("No patients to view yet!")
    else:
        print("List of patients: ")
        for i,patient in enumerate(patients):
         print(f"{i+1}. {patient["Name"]}   Age : {patient["Age"]}   Gender: {patient["Gender"]}   Problem: {patient["Problem"]}")
         print()
def search_patients():
   name=input("Enter name to be searched: ")
   for patient in patients:
    found=False
    if patient["Name"].lower() == name.lower():
       print(" Patient found: ")
       print(f"Name = {patient["Name"]}")
       print(f"Age = {patient["Age"]}")
       print(f"Gender = {patient["Gender"]}")
       print(f"Problem = {patient["Problem"]}")
       found=True
       break
    if not found:
       print("Patient not found!")
while True:
        print("-------Hospital Management System-------")
        print("Our system can assist you with the following: ")
        print("1. Add patients")
        print("2. View patients")
        print("3. Search patients")
        print("4. Exit")
    
        choice=input("Enter choice between 1-4: ")

        if choice == "1":
         add_patients()
        elif choice == "2":
         view_patients()
        elif choice == "3":
         search_patients()
        elif choice == "4":
         print("Exiting the system!Bye!")
         break
        else:
         print("Enter a valid choice between 1-4: ")
             