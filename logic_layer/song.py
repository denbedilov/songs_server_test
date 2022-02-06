# class describes song
class Song:
    db_schema = {
        'title': 'title',
        'performer': 'performer',
        'genre': 'genre',
        'year': 'year',
        'rating': 'rating'
    }

    api_schema = {
        'title': 'song_title',
        'performer': 'song_performer',
        'genre': 'song_genre',
        'year': 'song_year',
        'rating': 'rating'
    }

    def __init__(self, song_title='song_title', song_performer='song_performer', song_genre='song_genre', song_year='0'):
        self.song = {
            self.db_schema['title']: song_title,
            self.db_schema['performer']: song_performer,
            self.db_schema['genre']: song_genre,
            self.db_schema['year']: song_year,
            self.db_schema['rating']: 0
        }

    def get_song(self):
        return self.song

    # return song in add_song schema
    def get_add_song_schema(self):
        return {
            self.api_schema['title']: self.song['title'],
            self.api_schema['performer']: self.song['performer'],
            self.api_schema['genre']: self.song['genre'],
            self.api_schema['year']: self.song['year']
        }

    # return song in add_song schema
    def get_get_song_schema(self):
        return {
            self.api_schema['title']: self.song['title']
        }

    # return upvote schema with user and song
    def get_upvote_schema(self, user, playlist):
        self.song['rating'] += 1
        schema = user.get_user()
        schema[self.api_schema['title']] = self.song['title']
        schema['playlist_name'] = playlist
        return schema

    # return song rating
    def get_rating(self):
        return {
            self.api_schema['title']: self.song['title'],
            self.api_schema['rating']: self.song['rating']
        }

    # return upvote schema with user and song
    def get_down_vote_schema(self, user, playlist):
        self.song['rating'] -= 1
        schema = user.get_user()
        schema[self.api_schema['title']] = self.song['title']
        schema['playlist_name'] = playlist
        return schema

    # return sons title
    def get_title(self):
        return self.song['title']
