from typing import List, Callable
from collections import defaultdict
from z3 import *
from classes.components.enums import Quarter

class Caller:
    def __init__(self, max_quarter_units = 20):
        self._max_quarter_units = max_quarter_units
        self._observers = []
    
    @property
    def max_quarter_units(self):
        return self._max_quarter_units
    
    @max_quarter_units.setter
    def max_quarter_units(self, value):
        self._max_quarter_units = value
        self.notify_observers("max_quarter_units")

    def add_observer(self, observer: Callable[[], None]): 
        self._observers.append(observer)

    def remove_observer(self, observer: Callable[[], None]):
        self._observers.remove(observer)

    def notify_observers(self, change_type: str):
        for observer in self._observers:
            observer(change_type)


class Listener:
    def __init__(self, caller):
        self._caller = caller
        self._constraints = defaultdict(list)
        self._solver = Solver()
        self._caller.add_observer(self.update)
        self._modifiers = {
            "max_quarter_units": self._max_quarter_units,
        }
        
    def update(self, key: str):
        constraints = self._constraints[key]
        self._modifiers[key](constraints)
    
    def _max_quarter_units(self, constraints):
        constraints = []
        for quarter in range(4):
            load = sum([quarter for course in range(5)])
            constraints.append(self._caller.max_quarter_units)
            self._solver.add(load <= self._caller.max_quarter_units)

    def get_constraints(self):
        return self._solver.assertions()


def main():
    caller = Caller()
    listener = Listener(caller)
    caller.max_quarter_units = 20
    
    print(listener.get_constraints())
    print(listener._constraints)


if __name__ == "__main__":
    main()