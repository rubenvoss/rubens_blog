# Python und venv installieren - django in Produktion Teil 3
## Vorwort
Im letzten Teil haben wir uns um das Aufsetzen der Datenbank gekümmert. Nun werden wir unsere Repository auf den Produktionsserver bringen. Ebenso kümmern wir uns um das Aufsetzen der Python-Pakete. 

## Python Installation
Um unseren Webserver zum laufen zu bringen brauchen wir die richtigen Python-Pakete & für die Datenbankverbindung libpq-dev und gcc. Diese können wir nun mit apt installieren.
```
sudo apt install git python3.11 python3.11-venv python3-dev libpq-dev gcc
```

## Repository aufsetzen
Als nächstes brauchen wir einen Ort, an dem unser Repository liegen wird. Dazu nutze Ich hier `/srv/www`
```
sudo mkdir -p /srv/www/
sudo cd /srv/www
sudo git clone git@github.com:mein_name/meine_repository.git
sudo cd meine_repository
```
PS: Falls du nicht vor alle Befehle ein `sudo` setzen willst, kannst du dich mit `sudo su -` zum root Nutzer machen. Aber dann vorsichtig sein ;)

## requirements.txt
Für dein Projekt brauchst du eine requirements.txt Datei. Falls du diese noch nicht mit deinen Python Paketversionen gefüllt hast, kannst du das jetzt machen.
In deinem Lokalen Repository ausführen:
```
pip freeze > requirements.txt
```
Zu deinem requirements.txt solltest du folgende Pakete hinzufügen:
```
# Webserver in Produktion
gunicorn

# postgresql database adapter
psycopg2
psycopg2-binary
```
Diese kannst du nun bei dir Lokal installieren:
```
pip install -r requirements.txt
```

## Venv installieren
Jetzt kannst du, wieder zurück auf deinem Produktiven Server alle Pakete im requirements.txt installieren. Dazu erstellen wir ein venv, damit du mehrere Python Umgebungen auf dem gleichen Server laufen lassen kannst.
Vorher solltest du am besten bei dir lokal das venv - Verzeichnis in dein .gitignore hinzufügen.
Bei dir Lokal:
```
echo "venv/" >> .gitignore
```
Auf dem Produktivserver:
```
# Mache dich zum root Nutzer & Gehe in dein Codeverzeichnis
sudo su -
cd /srv/www/meine_repository

# hole dir die Neuesten Updates aus deiner Repository
git pull

# Installiere deine Virtuelle Python-Umgebung
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt 
```

## PostgreSQL migrieren
Nun sollte der python manage.py migrate Befehl funktionieren! Aber halt, hast du deine Datenbank schon in deiner settings.py Datei hinzugefügt? Das schauen wir uns im nächsten Post an ;)

Viel Spaß beim Coden,
Dein Ruben

[Mein Blog](rubenvoss.de)