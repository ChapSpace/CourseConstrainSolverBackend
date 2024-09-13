class Profile:
    """User-set constraints for the solver"""
    def __init__(
        self, 
        max_quarter_units: int = 20,
        min_quarter_units: int = 12,
    ):
        self._max_quarter_units = max_quarter_units
        self._min_quarter_units = min_quarter_units

        self._observers = []

    @property
    def max_quarter_units(self) -> int:
        return self._max_quarter_units
    
    @property
    def min_quarter_units(self) -> int:
        return self._min_quarter_units
    
    @max_quarter_units.setter
    def max_quarter_units(self, value: int):
        self._max_quarter_units = value
        self._notify_observers()
    
    @min_quarter_units.setter
    def min_quarter_units(self, value: int):
        self._min_quarter_units = value
        self._notify_observers()

    def add_observer(self, observer):
        self._observers.append(observer)
    
    def remove_observer(self, observer):
        self._observers.remove(observer)

    def _notify_observers(self):
        for observer in self._observers:
            observer()