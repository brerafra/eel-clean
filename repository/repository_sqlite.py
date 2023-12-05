""" Example:

from typing import List
from domain.music import Music
import sqlite3
import datetime
from .interface import Repository

class MusicRepository(Repository):
    def __init__(self):
        self._db = "storage.db"

    def get(self, music_id: int) -> Music:
        #Get a specific music

        try:
            connect = sqlite3.connect(self._db)
            cursor = connect.cursor()
            cursor.execute("select * from downolads where id=?",(music_id,))
            p = cursor.fetchone()
            m = Music(music_id=p[0], url=p[1], name=p[2], created_at=p[3])

            connect.close()
            return m
        
        except Exception as Error:
            print(Error)
            return None
        
    def get_pages(self) -> int:
        #Get all pages of music list
        try:
            connect = sqlite3.connect(self._db)
            cursor = connect.cursor()
            cursor.execute("select COUNT(*) from downolads")
            song = cursor.fetchone()
            if song is None:
                print("No such user found")
                connect.close()
                return None

            connect.close()
            return int(song[0])
        except Exception as Error:
            print(Error)

    def get_all(self) -> Music:
        #Get all music
        try:
            connect = sqlite3.connect(self._db)
            cursor = connect.cursor()
            cursor.execute("select * from downolads")
            songs = cursor.fetchall()
            self._songs = []
            for p in songs:
                m = Music(music_id=p[0], url=p[1], name=p[2], created_at=p[3])
                self._songs.append(m)

            connect.close()
            return self._songs
        except Exception as Error:
            print(Error)

    def get_paginated(self,page=str) -> Music:
        #Get music page to page
        try:
            connect = sqlite3.connect(self._db)
            cursor = connect.cursor()
            offset = 9 * int(page) - 9
            cursor.execute("select * from downolads order by id desc limit 9 offset ?",(offset,))
            songs = cursor.fetchall()
            self._songs = []
            for p in songs:
                m = Music(music_id=p[0], url=p[1], name=p[2], created_at=p[3])
                self._songs.append(m)

            connect.close()
            return self._songs
        except Exception as Error:
            print(Error)

    def save(self,song: Music) -> Music:
        #insert a song
        try:
            connect = sqlite3.connect(self._db)
            cursor = connect.cursor()
            now = datetime.datetime.now()
            created_at = now.strftime("%Y-%m-%d %H:%M:%S")
            cursor.execute("insert into downolads values(?,?,?,?)",(None,song.url,song.name,created_at))
            connect.commit()
            connect.close()
        except Exception as Error:
            print(Error)

"""