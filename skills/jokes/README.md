# Jokes Skills

<p>this one doesnt really work great but that is because there are not a lot of jokes apis... 
I used api.jokes.one and api.chucknorris.io and official-joke-api.appspot.com the api.jokes.one only allows 1 joke a day if I am correctly

<h2><a id="user-content-installation" class="anchor" aria-hidden="true" href="#installation"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Installation</h2>
<ol>
<li>Install Rhasspy</li>
<li>Insert the api key into the config.ini File

<p>Add to the sentences in German the following sentences:</p>
<pre>[Joke]
erzähle [(mir|uns|ihr|ihm)] [ein|einen] Witz</pre>
</li>

<p>Add to the sentences in English the following sentences:</p>
<pre>[Joke]
tell [(me|us|them|her|him)] [a] joke</pre>
</li>

<li>Now Save and train Rhasspy
<li>install the skill as service:
<pre>
chmod +x setup.sh
chmod +x action-jokes.py
sudo ./setup.sh
</pre>

After the script reboot the service should work. If it is not working check out
<pre>systemctl list-units --type=service</pre>
to see if the service started or check out any bugs with

<pre>journalctl -xe</pre>
 
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.