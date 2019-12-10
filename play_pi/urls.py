from django.conf.urls import include, url
from django.contrib import admin
from play_pi.models import *
from play_pi.views import *

admin.autodiscover()

urlpatterns = [
	url(r'^$', home, name='home'),
        url(r'^albums/$', albums, name='albums'),
	url(r'^artist/(?P<artist_id>\d+)/$', artist, name='artist'),
	url(r'^album/(?P<album_id>\d+)/$', album, name='album'),
	url(r'^playlists/$', playlists, name='playlists'),
	url(r'^playlist/(?P<playlist_id>\d+)/$', playlist, name='playlist'),
	url(r'^play/track/(?P<track_id>\d+)/$', play_track, name='play_track'),
	url(r'^play/album/(?P<album_id>\d+)/$', play_album, name='play_album'),
	url(r'^play/artist/(?P<artist_id>\d+)/$', play_artist, name='play_artist'),
	url(r'^play/playlist/(?P<playlist_id>\d+)/$', play_playlist, name='play_playlist'),
	url(r'^controls/random/$', random, name='random'),
	url(r'^controls/repeat/$', repeat, name='repeat'),
	url(r'^get_stream/(?P<track_id>\d+)/$', get_stream, name='get_stream'),
	url(r'^stop/$', stop, name='stop'),
	url(r'^ajax/(?P<method>\w+)/$', ajax, name='ajax'),
	url(r'^admin/', include(admin.site.urls)),
        ]

#Startup code here because there does not seem to be a better place
Track.objects.filter(mpd_id__gt=0).update(mpd_id=0) # we have to reset the MPD_ID because MPD reuses IDs when its restarted.
