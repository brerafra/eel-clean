"""from typing import List
from domain.music import Music
from repository.music_mysql import MusicRepository


class MusicService:
    def __init__(self, repository:MusicRepository):
        self._repository = repository

    def get_song(self, song_id:int) -> Music:
        return self._repository.get(song_id)
    
    def get_pages(self) -> int:
        return self._repository.get_pages()
    
    def get_all_songs(self) -> List[Music]:

        return self._repository.get_all()
    
    def get_paginated_songs(self, page: str) -> List[Music]:

        return self._repository.get_paginated(page)
    
    def insert_song(self, song: Music) -> None:
        return self._repository.save(song)"""