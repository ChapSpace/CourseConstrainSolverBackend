from classes.Course import Course
from classes.Program import Program
from z3 import *

def main():
    FALL = 0
    WINTER = 1
    SPRING = 2
    SUMMER = 3
    
    C1 = Int('C1')
    C2 = Int('C2')
    C3 = Int('C3')
    C4 = Int('C4')
    
    s = Solver()
    
    s.add(Or(C1 == FALL))
    s.add(Or(C2 == WINTER))
    s.add(Or(C3 == SPRING))
    s.add(Or(C4 == SUMMER))
    
    course_load = [If(C1 == q, 1, 0) + If(C2 == q, 1, 0) + If(C3 == q, 1, 0) + If(C3 == q, 1, 0) for q in range(4)]
    for load in course_load:
        s.add(load <= 2)
    
    print(s.check())
    
    
    
    

if __name__ == "__main__":
    main()

