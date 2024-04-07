# Run the menu
from sets import (get_students_who_took_prog1_and_prog2,
                  get_students_who_took_prog2_only,
                  get_students_who_took_prog1_not_prog2,
                  get_students_who_took_prog2_not_prog1)

def main():
    prog1 = {'Student1', 'Student2', 'Student3'}
    prog2 = {'Student3', 'Student4', 'Student5'}
    
    while True:
        
        print("\nInventory Menu")
        print("1- Students who took prog1 and prog2")
        print("2- Students who took prog2 only")
        print("3- Students who took prog1 not prog2")
        print("4- Students who took prog2 not prog1")
        print("5- Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print('students_who_took_prog1_and_prog2') 
            get_students_who_took_prog1_and_prog2(prog1, prog2)
               
        elif choice == '2':
            print('students_who_took_prog2_only')
            get_students_who_took_prog2_only(prog1, prog2)
            
                
        elif choice == '3':
            print('students_who_took_prog1_not_prog2')
            get_students_who_took_prog1_not_prog2(prog1, prog2)
            

        elif choice == '4':
            print('students_who_took_prog2_not_prog1')
            get_students_who_took_prog2_not_prog1(prog1, prog2)
            
                
        elif choice == '5':
            print("Exiting...")
            
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
main()