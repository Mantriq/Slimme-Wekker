# Documentation : https://pyspotify.readthedocs.io/en/latest/api/sink/

import Muziek.spotify as spotify
session = spotify.Session()
audio = spotify.AlsaSink(session)
loop = spotify.EventLoop(session)
loop.start()
# Login, etc...
track = session.get_track('spotify:track:3N2UhXZI4Gf64Ku3cCjz2g')
track.load()
session.player.load(track)
session.player.play()
# Listen to music...