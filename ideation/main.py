from classes.Course import Course
from classes.Program import Program
from z3 import *

def main():
    
    # Quarters assigned integer values
    FRESH_FALL = 0
    FRESH_WINTER = 1
    FRESH_SPRING = 2
    FRESH_SUMMER = 3
    
    C1 = Int('C1')
    C2 = Int('C2')
    C3 = Int('C3')
    C4 = Int('C4')
    C5 = Int('C5')
    C6 = Int('C6')
    C7 = Int('C7')
    C8 = Int('C8')
    
    s = Solver()
    
    s.add(Or(C1 == FRESH_FALL))
    s.add(Or(C2 == FRESH_FALL))
    s.add(Or(C3 == FRESH_SPRING))
    s.add(Or(C4 == FRESH_SUMMER))
    s.add(Or(C5 == FRESH_FALL))
    s.add(Or(C6 == FRESH_WINTER))
    s.add(Or(C7 == FRESH_SPRING))
    s.add(Or(C8 == FRESH_SUMMER))
    
    course_load = [If(C1 == q, 1, 0) + If(C2 == q, 1, 0) + If(C3 == q, 1, 0) + If(C4 == q, 1, 0) 
                   + If(C4 == q, 1, 0)  + If(C5 == q, 1, 0)  + If(C6 == q, 1, 0)  + If(C7 == q, 1, 0) for q in range(4)]
    for load in course_load:
        s.add(load <= 2)
    
    print(s.check())
    
    if s.check() == sat:
        print(s.model())
    
if __name__ == "__main__":
    main()

