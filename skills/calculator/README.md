# Simple Calculator Skill

<h2>Installation</h2>
<ol>
<li>Install Rhasspy</li>
<li>
<p>Add to the sentences in German the following sentences:</p>
<pre>

[CalculatorAddition]
(wie viel|was) ist  (1..10){$number}{first} (mit|plus|und)  (1..10){$number}{second}
addiere  (1..10){$number}{first} (mit|plus|und)  (1..10){$number}{second}
/(1..10){$number}{first} (mit|plus|und)  (1..10){$number}{second} [ist]

[CalculatorSubstract]
(wie viel|was) ist  (1..10){$number}{first} minus  (1..10){$number}{second}
substrahiere  (1..10){$number}{first} (minus|und)  (1..10){$number}{second}
/(1..10){$number}{first} minus  (1..10){$number}{second} [ist]

[CalculatorMultiply]
(wie viel|was) ist (1..10){$number}{first} mal   (1..10){$number}{second}
multipliziere  (1..10){$number}{first} (mit|und)  (1..10){$number}{second}
/(1..10){$number}{first} mal  (1..10){$number}{second} [ist]

[CalculatorDivision]
(wie viel|was) ist (1..10){$number}{first} geteilt [durch]  (1..10){$number}{second}
dividiere  (1..10){$number}{first} (mit|und)   (1..10){$number}{second}
/(1..10){$number}{first} geteilt [durch]  (1..10){$number}{second} [ist]

[CalculatorRoot]
was ist die Wurzel von  (1..10){$number}{first}
Wurzel   (1..10){$number}{first}
/(1..10){$number}{first} Wurzel [ist]
</pre>
</li>

<li>
<p>Or add to the sentences in english the following sentences:</p>
<pre>
[CalculatorAddition]
(how much|what) is  (1..10){$number}{first} (with|plus|and)  (1..10){$number}{second}
add (1..10){$number}{first} (with|plus|and) (1..10){$number}{second}
/(1..10){$number}{first} (with|plus|and)  (1..10){$number}{second} [ist]

[CalculatorSubstract]
(how much|what) is (1..10){$number}{first} minus  (1..10){$number}{second}
subtract  (1..10){$number}{first} (minus|und)  (1..10){$number}{second}
/(1..10){$number}{first} minus  (1..10){$number}{second} [ist]

[CalculatorMultiply]
(how much|what) is (1..10){$number}{first} multiplied with (1..10){$number}{second}
multiply  (1..10){$number}{first} (with|and)  (1..10){$number}{second}
/(1..10){$number}{first} multiplied with  (1..10){$number}{second} [ist]

[CalculatorDivision]
(how much|what) is (1..10){$number}{first} divided [by]  (1..10){$number}{second}
divide  (1..10){$number}{first} (with|and)   (1..10){$number}{second}
/(1..10){$number}{first} divide [by]  (1..10){$number}{second} [ist]

[CalculatorRoot]
what is the root of (1..10){$number}{first}
root of (1..10){$number}{first}
/(1..10){$number}{first} root [ist]
</pre>
</li>

<li>if you are using the english version replace in the config.ini language=<i><b>de</b></i> with <i><b>en</b></i></li>
<li>Save and train Rhasspy</li>
<li>Test the skill with:
<pre>
python3 action-calculator.py
</pre>
<li>install the skill as service:
<pre>
chmod +x setup.sh
chmod +x action-calculator.py
sudo ./setup.sh
</pre></li>

After the script reboot the service should work. If it is not working check out
<pre>systemctl list-units --type=service</pre>
to see if the service started or check out any bugs with

<pre>journalctl -xe</pre>


THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.