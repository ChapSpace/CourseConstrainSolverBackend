class Profile:
    """User-set constraints for the solver"""
    def __init__(self, max_quarter_units: int):
        self._max_quarter_units = max_quarter_units
        
    @property
    def max_quarter_units(self) -> int:
        return self._max_quarter_units
        