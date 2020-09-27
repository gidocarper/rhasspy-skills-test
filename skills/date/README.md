# Date Skill

<h2><a id="user-content-installation" class="anchor" aria-hidden="true" href="#installation"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Installation</h2>
<ol>
<li>Install Rhasspy</li>
<li>
<p>Add to the sentences in German the following sentences:</p>
<pre>[whenIsChristmas]
Wie viel tage ist es noch (zum|zu|zur)  (Weihnachten|Weihnacht|Weihnachte)
Wann ist (Weihnachten|Weihnacht|Weihnachte)
Tage bis  (Weihnachten|Weihnacht|Weihnachte)</pre>
<pre>
[GetTime]
wie spät ist es [jetzt]
was ist die Uhrzeit
erzähle mir die Uhrzeit
die Uhrzeit</pre>
<pre>
[GetDate]
(welcher|welche|welchen) Tag ist [es]  [jetzt|heute]
erzähle mir (der|die|dem) Tag</pre>
</li>
<li>
<p>Or Add to the sentences in english the following sentences:</p>
<pre>[whenIsChristmas]
How many days (till|until) (Xmass|Christmas)
When is [it] (Xmass|Christmas)
Days (till|until) (Xmass|Christmas)</pre>
<pre>
[GetTime]
what time is it [now]
what is the time
what time is it
tell me the time
time</pre>
<pre>[GetDate]
which day is [it]  [today]
tell me the day
what date do we have today
what's todays date
</pre></li>
<li>if you are using the english version replace in the config.ini language=<i><b>de</b></i> with <i><b>en</b></i>
<li>Save and train Rhasspy
<li>Now Save and train Rhasspy
<li>install the requirements with
<pre>chmod +x action-date.py
pip install -r requirements.txt</pre>
<li>Then start the script with 
<pre>python3 action-date.py</pre> 

<li>install the skill as service:
<pre>
chmod +x setup.sh
chmod +x action-date.py
sudo ./setup.sh
</pre></li>
