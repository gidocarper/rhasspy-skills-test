# Gasoline Prices

<p><strong>Important:</strong>
Before you can use this script you need an api key from this website: 
<a href="https://creativecommons.tankerkoenig.de/">https://creativecommons.tankerkoenig.de/</a> 

This didnt cost me  anything, just take the free api key.

<h2><a id="user-content-installation" class="anchor" aria-hidden="true" href="#installation"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Installation</h2>
<ol>
<li>Install Rhasspy</li>
<li>Insert the api key into the config.ini File
<pre>
tankerkoenig_api_key=HERE
</pre>
</li>
<li>Check the latitude and longitude values from the street you are living in and replace it in the config.ini file: 
<pre>
latitude=52.5166667
longitude=13.3999996
</pre>
The above coordinates are the coordinates of Berlin.
<li>Add a new slot with the name 
<pre>city</pre>
and add to this new slot the following values:
<pre>Moers
Rostock
Flensburg
Koblenz
Duisburg
Erlangen
Siegen
Velbert
Wolfsburg
Oldenburg
Neuss
Tubingen
Ulm
Solingen
Kiel
Wurzburg
Berlin
Furth
Iserlohn
Essen
Karlsruhe
Bremen
Ingolstadt
Heidelberg
Mannheim
Remscheid
Krefeld
Zwickau
Hannover
Dresden
Esslingen
Oberhausen
Wiesbaden
Marl
Hagen
Hanau am Main
Mainz
Magdeburg
Chemnitz
Herne
Stuttgart
Duren
Bonn
Leverkusen
Osnabruck
Heilbronn
Hamburg
Hildesheim
Lubeck
Ratingen
Halle-Neustadt
Augsburg
Aachen
Dortmund
Halle
Minden
Wilhelmshaven
Bochum
Witten
Regensburg
Nuernberg
Koeln
Monchengladbach
Cottbus
Mulheim an der Ruhr
Saarbrucken
Kaiserslautern
Bremerhaven
Bergisch Gladbach
Reutlingen
Recklinghausen
Schwerin
Bottrop
Gutersloh
Offenbach
Leipzig
Darmstadt
Dusseldorf
Erfurt
Gottingen
Munster
Jena
Kassel
Paderborn
Freiburg
Hamm
Gelsenkirchen-Alt
Potsdam
Frankfurt am Main
Pforzheim
Muenchen
Lunen
Neustadt
Ludwigsburg
Wuppertal
Gera
Trier
Ludwigshafen am Rhein
Braunschweig
Bielefeld
<li>
<p>Add to the sentences in German the following sentences:</p>
<pre>[FullPrices]
city = ($city){city}
Preise für (Diesel | Benzin){fullType} [bitte]
(Diesel | Benzin){fullType} (Preis|Preise) [bitte]
was kostet (Diesel | Benzin){fullType}
(Diesel | Benzin){fullType}
(Diesel | Benzin){fullType} Preise [in] <city> [bitte]
gib mir die (Diesel | Benzin){fullType} (Preis|Preise)
die (Diesel | Benzin){fullType} (Preis|Preise)
Wie ist der aktuelle Benzin{fullType} (Preis|Preise)
Ich möchte (Diesel | Benzin){fullType} tanken
Ich muss (Diesel | Benzin){fullType} tanken
(Nenne mir den|Wie ist der aktuelle|Gib mir den|Sag mir den|Gib mir den aktuellen) (Diesel | Benzin){fullType} (Preis|Preise)
(Wieviel kostet|Wie viel kostet|Was kostet der)  (Diesel | Benzin){fullType} [gerade|jetzt]</pre>

This service only works in Germany so there is no english version here.
</li>
<li>Now Save and train Rhasspy
<li>install the skill as service:
<pre>
chmod +x setup.py
chmod +x action-gasoline.py
sudo ./setup.py
</pre>

After the script reboot the service should work. If it is not working check out
<pre>systemctl list-units --type=service</pre>
to see if the service started or check out any bugs with

<pre>journalctl -xe</pre>
 



This script has it origines from this script:
https://github.com/hablijack/Snips-Spritpreise