""" Example: 

from typing import Protocol
from typing import List
from domain.music import Music

class Repository(Protocol):
    #Repository for music operations

    def get(self) -> Music:
        # Get a specific music
        raise NotImplementedError("Get not implemented")

    def get_all(self) ->List[Music]:
        #Get all music
        raise NotImplementedError("Get_All not implemented")
    
    def get_paginated(self, page: str) ->List[Music]:
        # Get a paginated list of music
        raise NotImplementedError("get_paginated not implemented")
    
    def get_pages(self) -> int:
        #Get total pages of list music
        raise NotImplementedError("get_pages not implemented")

    def save(self, song: Music) -> None:
        #Insert a song 
        raise NotImplementedError("save not implemented")"""