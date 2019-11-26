# Streamer

A python tool used to stream movies and series torrent directly in VLC media player

## Installation

```
$ pip install streamer
```

### Usage
Streamer can be used to query in 3 different ways
- To stream movies

```python
streamer movie "Batman Begins"
```
```
streamer movie "Batman Begins" --quality 720p
```
- To stream series 

```
streamer series "The big bang theory" --episode s02e02
```
```
streamer series "The big bang theory" --episode s02e02 --quality 720p
```

- To stream magnet links

```
 streamer link {magnet_link}
```

# Dependencies

Please ensure that VLC media player and NPM are installed.
Other dependencies are-
- BeautifulSoup
- Request
- Peerflix

