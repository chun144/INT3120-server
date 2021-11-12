# Backend for Music app

## APIs

### Add 1 song
```
POST    https://music-app-dd.herokuapp.com/music/song/
```
```json
{
    "title": "song 1",
    "artists": ["J", "K"],
    "artwork": "1",
    "url_player": "url",
    "duration": "1",
    "genres": ["a", "b"],
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
    "artists": ["J", "K"],
    "artwork": "1",
    "url_player": "url",
    "duration": "1",
    "genres": ["a", "b"],
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

### Search songs with album
get songs contain input (album contain "1")
```
GET    https://music-app-dd.herokuapp.com/music/song/search/album/1
```

### Update data from mock-server
```
POST    https://music-app-dd.herokuapp.com/music/song/mock/
```

### Get token
```
POST    https://music-app-dd.herokuapp.com/music/api/token/
```
```json
{
    "username": "admin",
    "password": "12345678"
}
```