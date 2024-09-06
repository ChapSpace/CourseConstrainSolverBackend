from classes.Course import Course
from classes.Program import Program
from classes.Quarters import Quarters
from z3 import *

def main():
    
    degreeProgram = Program([Course('C1', [Quarters['FRESH_FALL'].value]),
                            Course('C2', [Quarters['FRESH_FALL'].value, Quarters['FRESH_WINTER'].value]),
                            Course('C3', [Quarters['FRESH_WINTER'].value, Quarters['FRESH_SPRING'].value]),
                            Course('C4', [Quarters['FRESH_SPRING'].value])])
    
    s = Solver()
    
    for course in degreeProgram.get_required_courses():
        s.add(Or([Int(course.get_name()) == quarter for quarter in course.get_quarters()]))
    
    print(s.check())
    print(s.model())
   
    
if __name__ == "__main__":
    main()

