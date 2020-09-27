# Volume Skill


<h2>Installation</h2>
<ol>

<li>Install Rhasspy</li>
<li>Before installing this skill check if it works with
<pre>
python3 action-volume.py
</pre>
</li>
<li>If it doesnt work check these lines in volume.py
<pre>
    #for some this can be Master instead of PCM if you get errors try Master
    try:
        self.alsaaudioMixer = alsaaudio.Mixer('PCM')
    except Exception as ex:
        self.alsaaudioMixer = alsaaudio.Mixer('Master')
</pre>
</li>


<li>install the skill as service:
<pre>
chmod +x setup.sh
chmod +x action-volume.py
sudo ./setup.sh
</pre>
After the script reboot the service should work. If it is not working check out
<pre>systemctl list-units --type=service</pre>
to see if the service started or check out any bugs with

<pre>journalctl -xe</pre>


THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
