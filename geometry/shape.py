from abc import ABC
# python 3.10: 
#   Union => |
#   Optional[str] => str|None
#from typing  import Union, Optional

class Shape(ABC):
    
    def __init__(self, name: str|None=None):
    # def __init__(self, name: Optional[str]=None):
        self.name = name