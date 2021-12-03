# Backend for Music app

## APIs

### Add 1 song (login required)
```
POST    https://music-app-dd.herokuapp.com/music/song/
```
```json
{
    "title": "song 1",
    "artists": "J, K",
    "artwork": "1",
    "url": "url",
    "duration": 1,
    "genres": "a, b",
    "description": "N/A"
}
```

### Get all songs
```
GET    https://music-app-dd.herokuapp.com/music/song/all
```

### Edit 1 song with id (login required)
edit song (id=1)
```
PUT    https://music-app-dd.herokuapp.com/music/song/1
```
```json
{
    "title": "song 1",
    "artists": "J, K",
    "artwork": "1",
    "url": "url",
    "duration": 1,
    "genres": "a, b",
    "description": "N/A"
}
```

### Delete 1 song with id (login required)
delete song (id=1)
```
DELETE    https://music-app-dd.herokuapp.com/music/song/1
```

### Song +1 view with id (login required)
song (id=1) +1 view
```
PUT    https://music-app-dd.herokuapp.com/music/song/views/1
```

### Get 1 song with id
get song (id=1)
```
GET    https://music-app-dd.herokuapp.com/music/song/detail/1
```

### Search songs with title
get songs contain input (title contain "song")
```
GET    https://music-app-dd.herokuapp.com/music/song/search/title/song
```

### Update data from mock-server (login required)
```
POST    https://music-app-dd.herokuapp.com/music/song/mock/
```

### Add 1 artist (login required)
```
POST    https://music-app-dd.herokuapp.com/music/artist/
```
```json
{
    "name": "A",
    "information": "abc"
}
```

### Get all artists (login required)
```
GET    https://music-app-dd.herokuapp.com/music/artist/
```

### Edit 1 artist with id (login required)
edit artist (id=1)
```
PUT    https://music-app-dd.herokuapp.com/music/artist/1
```
```json
{
    "name": "B",
    "information": "abc"
}
```

### Delete 1 artist with id (login required)
delete artist (id=1)
```
DELETE    https://music-app-dd.herokuapp.com/music/artist/1
```

### Register 1 user
```
POST    https://music-app-dd.herokuapp.com/music/register
```
```json
{
    "username": "ce",
    "password": "123456",
    "password2": "123456"
}
```

### Login
```
POST    https://music-app-dd.herokuapp.com/music/login
```
```json
{
    "username": "ce",
    "password": "123456"
}
```

### Add 1 song to favorite list of user (login required)
```
POST    https://music-app-dd.herokuapp.com/music/favorite-list/
```
```json
{
    "songId": 1,
    "username": "chun"
}
```

### Delete 1 song from favorite list of user (login required)
```
DELETE    https://music-app-dd.herokuapp.com/music/favorite-list/
```
```json
{
    "songId": 1,
    "username": "chun"
}
```

### Get all song from favorite list of user (login required)
Get all song from favorite list of user with username "chun"
```
GET    https://music-app-dd.herokuapp.com/music/favorite-list/chun
```

### Get all genres
```
GET    https://music-app-dd.herokuapp.com/music/genre/all
```

### Search songs with genre
get songs with input (genre "Pop")
```
GET    https://music-app-dd.herokuapp.com/music/genre-song/Pop
```

### Add 1 genre (login required)
```
POST    https://music-app-dd.herokuapp.com/music/genre/
```
```json
{
    "title": "Hot",
    "artwork": "No"
}
```

### Edit 1 genre with id (login required)
edit genre (id=1)
```
PUT    https://music-app-dd.herokuapp.com/music/genre/1
```
```json
{
    "title": "Hot",
    "artwork": "No"
}
```

### Delete 1 genre with id (login required)
delete genre (id=1)
```
DELETE    https://music-app-dd.herokuapp.com/music/genre/1
```

### Get all playlist
```
GET    https://music-app-dd.herokuapp.com/music/playlist/all
```

### Search songs with playlist
get songs with input (playlist "Hot")
```
GET    https://music-app-dd.herokuapp.com/music/playlist-song/Hot
```

### Add 1 playlist (login required)
```
POST    https://music-app-dd.herokuapp.com/music/playlist/
```
```json
{
    "title": "Hot",
    "artwork": "No"
}
```

### Edit 1 playlist with id (login required)
edit playlist (id=1)
```
PUT    https://music-app-dd.herokuapp.com/music/playlist/1
```
```json
{
    "title": "Hot",
    "artwork": "No"
}
```

### Delete 1 playlist with id (login required)
delete playlist (id=1)
```
DELETE    https://music-app-dd.herokuapp.com/music/playlist/1
```

### Add 1 song to playlist(login required)
```
POST    https://music-app-dd.herokuapp.com/music/playlist-song/
```
```json
{
    "songId": 1,
    "playlist": "Hot"
}
```

### Delete 1 song from playlist (login required)
```
DELETE    https://music-app-dd.herokuapp.com/music/playlist-song/
```
```json
{
    "songId": 1,
    "playlist": "Hot"
}
```