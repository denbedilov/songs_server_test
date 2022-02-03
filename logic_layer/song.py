# class describes song
class Song:
    def __init__(self, song_title='song_title', song_performer='song_performer', song_genre='song_genre', song_year='0'):
        self.song = {
            'title': song_title,
            'performer': song_performer,
            'genre': song_genre,
            'year': song_year,
            'rating': 0
        }

    def get_song(self):
        return self.song

    # return song in add_song schema
    def get_add_song_schema(self):
        return {
            'song_title': self.song['title'],
            'song_performer': self.song['performer'],
            'song_genre': self.song['genre'],
            'song_year': self.song['year']
        }

    # return song in add_song schema
    def get_get_song_schema(self):
        return {
            'song_title': self.song['title']
        }