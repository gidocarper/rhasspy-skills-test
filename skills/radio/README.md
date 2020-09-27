# Radio Skill


<h2><a id="user-content-installation" class="anchor" aria-hidden="true" href="#installation"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Installation</h2>
<ol>
<li>Install Rhasspy</li>

<li>Add a new slot with the name 
<pre>radio_station</pre>
and add to this new slot the following values: <pre>
rtl
world hits
raggea
70er Hits
Rock songs
charts
80er Hits
sunshine lounge
italia
Love
ndr 2
2000-er Hits
party mix
ndr welle nord kiel
n joy
Hits für kids
Deutsch Rap
Trending
Westdeutscher Rundfunk
Sunshine house
r b b
f f h
Deutschlandfunk Kultur
Energy
Radio Bremen
Deutschland Funk
Hessischer Rundfunk
Partyschlager
80er Radio
Fitness Hits
Saarländischer Rundfunk
Weihnacht
Deutsch House
Rock classics
Neuheiten
60er 70er
ndr 2 Hamburg
Deutsch Hits
hamburg 2
sunshine trance
Prince
90er Hits
mix
mdr
delta
Südwestrundfunk
sunshine drum and bass
Bayern 1
ndr
</pre>

<li>
<p>Add to the sentences in German the following sentences:</p>
<pre>[PlayInternetRadio]
radio_station= [$radio_station]{radio_station}
Internet Radio <radio_station> 
Spiele [der|die|das] (Sender|Radio sender|Internet Radio|Radio) <radio_station> 
Spiele <radio_station> (Sender|Radio sender|Internet Radio|Radio) 
Ich möchte  [der|die|das] (Sender|Radio sender|Internet Radio|Radio) <radio_station> hören
</pre>
<pre>
[Stop]
stop
stoppe
vergiss es 
stop (die|der|das) (musik|video|song|playlist|internet radio|radio|radio sender)
</pre>
</li>
<li>if you are using the english version replace in the config.ini language=<i><b>de</b></i> with <i><b>en</b></i>
<li>There is no english translation yet.
<li>Save and train Rhasspy
</li>
<li>Now Save and train Rhasspy
<li>install the skill as service:
<pre>
chmod +x setup.sh
chmod +x action-radio.py
sudo ./setup.sh
</pre>
After the script reboot the service should work. If it is not working check out
<pre>systemctl list-units --type=service</pre>
to see if the service started or check out any bugs with

<pre>journalctl -xe</pre>


if it doesn't work install the vlc python player in this direcoty with:<pre>pip install python-vlc</pre>



