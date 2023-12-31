from lib.album import *

class AlbumRepository():
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM albums')
        albums = []

        for row in rows:
            item = Album(row["id"], row["title"], row["release_year"], row["artist_id"])
            albums.append(item)

        return albums
    
    def find(self, album_id):
        rows = self._connection.execute('SELECT * FROM albums WHERE id = %s', [album_id])

        for row in rows:
            album = Album(row["id"], row["title"], row["release_year"], row["artist_id"])
        
        return album
        # row = rows[0]
        # return Album(row["id"], row["title"], row["release_year"], row["artist_id"])
