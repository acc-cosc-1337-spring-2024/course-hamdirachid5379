

import repetition




while True:
   print("Menu:")
   print("1.get factorial")
   print("2.get sum of odd numbers")
   print("3.Exit")
   choice =  input("Enter your choice")
   if choice =="1":
      num = int(input("Enter a number for factorial"))

      factorial = 1
      while num > 0 and num < 10:

         factorial *=num
         num -= 1
         result = factorial

         print(f"factorial of {num} is  {result}")

   elif choice =="2":
      num = int(input("Enter number for sum of odd numbers: "))
      
      sum = 0
      while(num > 0 and num < 100):
         #def get_sum_of_odd_numbers(num):
         if num % 2 == 1:
            sum += num
            num -=1
            result = sum
            print(f"Sum of odd numbers up to the {num} is:  {result}")

   elif choice == "3":
      print(" Exiting...")
    

    