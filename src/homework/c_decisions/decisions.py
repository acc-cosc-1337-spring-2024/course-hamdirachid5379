#create function get_options_ratio

def get_options_ratio(options, total):
    result= options/total
    return result

def get_faculty_rating(ratio):
    faculty_rating = ""

    if(ratio > .9 and ratio < 1):
        faculty_rating = "Excellent"
        return  faculty_rating

    elif(ratio > .8):
        faculty_rating = "Very Good"
        return faculty_rating

    elif(ratio > .7):
        faculty_rating = "Good"
        return faculty_rating

    elif(ratio > .6):
        faculty_rating = "Needs Improvements"
        return faculty_rating

    elif(0 < ratio < .59 ):
        faculty_rating = "Unacceptable"
        return faculty_rating

    else:
        faculty_rating = "No Grading available"
        return faculty_rating
    
    def sum_of_odd_numbers(num): 
        counter = 0
        sum = 0
        
        while (counter < num):
            counter = counter +1
            if counter % 2 == 1:
                sum = sum + counter 
                print(counter)
                print('sum of odd numbers is: ' + sum )

    
    while(odd):
        print("the sum is odd : " + sum)
    else:
        print("the sum is not odd :" + sum)
        



