# Backend for Music app

## APIs

### Add 1 song
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
    "album": "1"
}
```

### Get all songs
```
GET    https://music-app-dd.herokuapp.com/music/song/
```

### Edit 1 song with id
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
    "album": "1"
}
```

### Delete 1 song with id
delete song (id=1)
```
DELETE    https://music-app-dd.herokuapp.com/music/song/1
```

### Song +1 view with id
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

### Get all albums
```
GET    https://music-app-dd.herokuapp.com/music/song/album/
```

### Search songs with album
get songs with input (album "1")
```
GET    https://music-app-dd.herokuapp.com/music/song/search/album/1
```

### Update data from mock-server
```
POST    https://music-app-dd.herokuapp.com/music/song/mock/
```

### Add 1 artist
```
POST    https://music-app-dd.herokuapp.com/music/artist/
```
```json
{
    "name": "A",
    "information": "abc"
}
```

### Get all artists
```
GET    https://music-app-dd.herokuapp.com/music/artist/
```

### Edit 1 artist with id
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

### Delete 1 artist with id
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
