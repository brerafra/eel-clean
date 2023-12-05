import eel
import pyautogui

# ---- Configuracion loading
from config import Config as devconf

# ---- Repository, service and domain layers loading

"""from repository.music_sqlite import MusicRepository
from service import MusicService
from domain.music import Music"""

# ---- Initializating the repository instance
#repo = MusicRepository(devconf)
#repo = MusicRepository()


# ---- Initializating the service instance

#music  = MusicService(repo)

eel.init("web")

# -------------- [General - functions]

# -------------- [eel - functions]

#Example
"""@eel.expose
def get_songs(page):
    songs = music.get_paginated_songs(page)
    c = []
    for p in songs:
        song = (p.music_id,p.url, p.name, p.created_at)
        c.append(song)
    return c"""

# -------------- [Multitasking - functions]


if __name__== "__main__":
    eel.start(
        "templates/index.html",
        port=devconf.APP_PORT,
        jinja_templates = 'templates',
        size= pyautogui.size()
    )