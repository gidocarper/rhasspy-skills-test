# 3 Rhasspy Skills 


<h2><a id="user-content-installation" class="anchor" aria-hidden="true" href="#installation"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Installation</h2>
<ol>
<li>Install Rhasspy</li>

<li>install with<pre>
pip install -r requirements.txt</pre>

<li>install each single skill (check the README.md in each skill directory)
<li> and then it is the question.... how to start all 3 skills at the same time

I have tried to start read all directories, search for each action-*.py file and start up all python files at the same time but you can only do this once.
If you want to change anything and stop the script with ctrl + C the script dont stop

use
<pre>ps aux | grep python</pre>

to see which script is still running and then kill each of them with 

<pre>kill -9 [ID you find in the list]</pre>