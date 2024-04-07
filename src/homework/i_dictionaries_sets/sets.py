#define a set


def get_students_who_took_prog1_and_prog2(prog1, prog2):
    
    print(prog1.union(prog2))

def get_students_who_took_prog2_only(prog1, prog2):
    
    print(prog1.difference(prog1))

def get_students_who_took_prog1_not_prog2(prog1, prog2):
    
    #print('students who took prog1 not prog2') 
    print(prog1.difference(prog2))

def get_students_who_took_prog2_not_prog1(prog1, prog2):
    

    #print('students who took prog2 not prog1')
    print(prog2.difference(prog1))

