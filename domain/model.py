"""Example: class Music:
    def __init__(
            self,
            music_id: int,
            url: str,
            name: str,
            created_at: str
    ):
        self._music_id = music_id
        self._url = url
        self._name = name
        self._created_at = created_at

    @property
    def music_id(self):
        return self._music_id
    
    @property
    def url(self):
        return self._url
    
    @url.setter
    def url(self, value:str):
        self._url = value
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value:str):
        self._name = value

    @property
    def created_at(self):
        return self._created_at
    
    @created_at.setter
    def created_at(self, value:str):
        self._created_at = value"""