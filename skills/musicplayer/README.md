this is still work in progress, the installation of the music player works the same as with the other skills..
here the intends for german...
if you let the musicplayer scan your music it write several files in 

/root/.config/rhasspy/profiles/de/slots/

this location can differ.
The skill was installed on a rhasspy locally without docker.


<pre>

[PlayMusic]

[MusicPlayer]
music_artists = ($music_artists){music_artists}
music_titles = ($music_titles){music_titles}
music_genres = ($music_genres){music_genres}
music_albums  = ($music_albums){music_albums}
spiele (musik|lied|lieder|song|songs) [von] (&lt;music_artists&gt;|&lt;music_albums&gt;)
spiele  [(das Lied|der Song|Lied|Song)]&lt;music_titles&gt; von &lt;music_artists&gt;
spiele &lt;music_artists&gt;
spiele &lt;music_genres&gt; [musik|lied|lieder|song|songs]
musik [von] &lt;music_artists&gt;
spiele &lt;music_titles&gt; [von] &lt;music_artists&gt;

[MusicPlayerAddStars]
gebe [(dieses|dies|diese|das|der|dem|den)] [(Lied|Song)] (1..10){stars} (Sterne|Sternen|Stern)

[MusicPlayerPlayStarMusic]
spiele (musik|lied|lieder|song|songs) mit (1..10){stars} (Sterne|Sternen|Stern)

[MusicPlayerDeleteStars]
/[Lösche|entferne|entfern|Lösch] (von) [(dieses|dies|diese|das|der|dem|den)]  [(Lied|Song)] [(dieses|dies|diese|das|der|dem|den)] (Sterne|Sternen|Stern|bewertung)

[MusicPlayerPlayFavouriteMusic]
spiele mein (Lieblings|beste|hochst bewertete|liebing|best|super) (musik|lied|lieder|song|songs)
spiele [(Lieder|Songs|Song|Lieder|musik)] [mit] (1..10){stars} (Sterne|Sternen|Stern)

[MusicPlayerWhatIsPlaying]
Was spielt gerade?
Welche Musik spielt gerade?
Was für Musik wird gerade gespielt?
Was spielst du gerade?

[MusicPlayerAddToFavourites]
/[Füge] (dieses|die|das|dies|der) (Lied|Song) zu (meine|mein|meinem) (Favouriten|Favourite)

[MusicPlayerAddStarsToSong]
(Füge|gebe) (dieses|die|das|dies|der) (Lied|Song) (1..10) Sternen

[MusicPlayerAddToPlaylist]
music_playlist_name = ($music_playlist_name){music_playlist_name}
füge dieses Lied zu um meine Playlist &lt;music_playlist_name&gt;
Lied zu Playlist &lt;music_playlist_name&gt; hinzufügen
fügen (das) Lied zu meine Playlist &lt;music_playlist_name&gt;

[MusicPlayerRemoveFromPlaylist]
music_playlist_name = ($music_playlist_name){music_playlist_name}
lösche dieses Lied von meiner Playlist &lt;music_playlist_name&gt;
[dieses|der|das|diese] Lied [von meiner|von|von mein] Playlist löschen

[MusicPlayerPlayPlaylist]
music_playlist_name = ($music_playlist_name){music_playlist_name}
spiele meine Playlist &lt;music_playlist_name&gt;

[MusicPlayerScanMusic]
ich hab [neue] (Songs|Musik|Videos|Lieder|liedchen|Song)
(scan|scanne|scannen) [alle|die|allen|den] (Musik|Songs|Artisten)

[Training]
Trainiere
Lerne was neues
Trainiere dein Slots


</pre>