from math import factorial
import repetition

#decisions.while_validate_user_input()

#select Factorial = 1
#select Sum odd numbers = 2
#select Exit = 3


        
num =int(input("Enter  1 for Factorial or  2 for Sum of odd numbers or 3  to Exit : " )) 

if 1:
   factorial = 1 

   for i in range(num):
    
    factorial *=i+1
   print("the factorial of" ,num, "is" , factorial)

   if 2:
      num = int(input("Enter odd numbers: "))
      counter = 0
      sum = 0
      while(counter < num):
         counter =counter+1
         if counter % 2 == 1:
          sum +=1
      print(counter)
      print("Sum of odd numbers is " , sum)

   if 3:
      print(" Exiting...")
    

    