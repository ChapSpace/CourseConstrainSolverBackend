from typing import Union, List
from classes.components.course import Course

class Pool: 
    """
    Represents a degree program requirement whereby a certain number of requirements of a certain type must be fulfilled
    
    Attributes:
        type (str): The type of objects in the collection. Can be of type Course or another Pool
        objects (List[Union[Course, 'Pool']]): The actual requirements in the collection
        num_required (int): The number of object requirements that must be fulfilled (Ex: Fulfill at least two courses from the collection)
    """
    def __init__(self, type: str, objects: List[Union[Course, 'Pool']], num_required: int):
        self._type = type
        self._objects = objects
        self._num_required = num_required
    
    @property
    def type(self) -> str:
        return self._type
    @property
    def objects(self) -> List[Union[Course, 'Pool']]:
        return self._objects
    @property
    def num_required(self) -> int:
        return self._num_required