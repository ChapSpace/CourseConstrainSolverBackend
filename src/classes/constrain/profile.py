from typing import Dict, Any

class Profile:
    """User-set constraints for the solver"""
    def __init__(
        self, 
        id: str,
        max_quarter_units: int = 20,
        min_quarter_units: int = 12,
    ):
        self._id = id
        self._max_quarter_units = max_quarter_units
        self._min_quarter_units = min_quarter_units
        
    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self._id,
            "max_quarter_units": self._max_quarter_units,
            "min_quarter_units": self._min_quarter_units
        }
        
    @classmethod
    def from_dict(cls, dict) -> 'Profile':
        return cls(
            id=dict.get("id"),
            max_quarter_units=dict.get("max_quarter_units"),
            min_quarter_units=dict.get("min_quarter_units")
        )
        
    @property
    def id(self) -> str:
        return self._id
    
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