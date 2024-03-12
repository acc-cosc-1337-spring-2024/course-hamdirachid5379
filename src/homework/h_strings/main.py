#Create a Menu

from homework.h_strings.strings import get_hamming_distance, get_dna_complement


while True:
        print("1-Hamming Distance")
        print("2-DNA Complement")
        print("3-Exit")

        choice = int(input("Enter your choice: "))

        if choice == '1':
            dna1 = str(input("Enter dna1: "))
            dna2 = str(input("Enter dna2: "))
            distance = get_hamming_distance(dna1, dna2)
            print("Hamming Distance:", distance)

        elif choice == '2':
            dna = str(input("Enter dna string: "))
            complement = get_dna_complement(dna)
            print("DNA Complement:", complement)

        elif choice == '3':
            print("Exiting program...")
            

        else:
            print("Invalid choice. Please enter a valid option.")
