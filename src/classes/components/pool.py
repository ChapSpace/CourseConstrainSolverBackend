from typing import Union, List, Dict, Any
from classes.components.course import Course

class Pool: 
    """
    Represents a degree program requirement whereby a certain number of requirements of a certain type must be fulfilled
    
    Attributes:
        type (str): The type of objects in the collection. Can be either "Course" or "Pool"
        objects (List[Union[Course, 'Pool']]): The actual requirements in the collection
        num_required (int): The number of object requirements that must be fulfilled (Ex: Fulfill at least two courses from the collection)
    """
    def __init__(self, type: str, objects: List[Union[Course, 'Pool']], num_required: int):
        self._type = type
        self._objects = objects
        self._num_required = num_required
        
    def to_dict(self) -> Dict[str, Any]:
        return {
            "type": self._type,
            "objects": [obj.to_dict() for obj in self._objects],
            "num_required": self._num_required
        }
    
    def from_dict(cls, dict) -> 'Pool':
        
        obj_dicts = dict.get("objects")
        objs = None
        
        if dict.get("type") == "Course":
            objs = [Course.from_dict(course_dict) for course_dict in obj_dicts]
        elif dict.get("type") == "Pool":
            objs = [Pool.from_dict(pool_dict) for pool_dict in obj_dicts]
            
        return cls(
            type=dict.get("type"),
            objects=objs,
            num_required=dict.get("num_required")
        )
        
    
    @property
    def type(self) -> str:
        return self._type
    @property
    def objects(self) -> List[Union[Course, 'Pool']]:
        return self._objects
    @property
    def num_required(self) -> int:
        return self._num_required