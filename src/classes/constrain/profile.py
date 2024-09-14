from typing import Dict, Any

class Profile:
    """User-set constraints for the solver"""
    def __init__(
        self, 
        max_quarter_units: int = 20,
        min_quarter_units: int = 12,
    ):
        self._max_quarter_units = max_quarter_units
        self._min_quarter_units = min_quarter_units
        
    def to_dict(self) -> Dict[str, Any]:
        return {
            "max_quarter_units": self._max_quarter_units,
            "min_quarter_units": self._min_quarter_units
        }
        
    @property
    def max_quarter_units(self) -> int:
        return self._max_quarter_units
    
    @property
    def min_quarter_units(self) -> int:
        return self._min_quarter_units
    
    @max_quarter_units.setter
    def max_quarter_units(self, value: int):
        self._max_quarter_units = value
    
    @min_quarter_units.setter
    def min_quarter_units(self, value: int):
        self._min_quarter_units = value