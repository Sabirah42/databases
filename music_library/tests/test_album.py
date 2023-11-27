from lib.album import *

"""
Album constrcts with an id, title, release year and artist id
"""

def test_album_constructs():
    artist = Album(1, "Test Album", 2000, 1)
    assert artist.id == 1
    assert artist.title == "Test Album"
    assert artist.release_year == 2000
    assert artist.artist_id == 1