# PostgreSQL für django aufsetzen - django in Produktion (Teil 2)
## Vorwort

Im letzten Teil haben wir den Server bereit gemacht. In diesem Teil wird es um die Datenbank gehen. Ich habe mich für PostgreSQL entschieden, da es eine lange bewährte, viel genutzte Open - Source Datenbank ist. Ebenso ist Postgres natürlich skalierbar, d.h. wenn einmal mehr Nutzeranfragen kommen sollten kann man den Server anpassen, sodass eine große Anzahl von gleichzeitigen Anfragen verarbeitet werden kann.

### PostgreSQL installieren

Zuerst müssen wir das ganze via apt installieren:
```
sudo apt install postgresql postgresql-contrib
```

Jetzt können wir auf die PostgreSQL Datenbank zugreifen:
```
sudo -u postgres psql

# Nun sollte das Prompt so ausschauen:
psql (15.6 (Debian 15.6-0+deb12u1))
Type "help" for help.

postgres=#
```

### Datenbank & Nutzer erstellen

Jetzt erstellst du deinen eigenen Datenbank Nutzer.

```
# Verbinde dich mit postgres
sudo -u postgres psql

# Erstelle deine Datenbank - benutze Natürlich deinen eigenen Namen ;)
CREATE DATABASE meine_datenbank_xyz;

# Nun kannst du dich mit deiner Datenbank Verbinden
\connect meine_datenbank_xyz

# Jetzt kannst du deinen eigenen Nutzer für die Datenbank mit Passwort erstellen.
CREATE USER mein_nutzer WITH PASSWORD 'password';
```

### Datenbank Schema und PSQL 15

Seit PostgreSQL 15 gibt es bei der Sicherheit von Postgres ein Update.
`Remove PUBLIC creation permission on the public schema (Noah Misch) The new default is one of the secure schema usage patterns that Section 5.9.6 has recommended...`
Das hat Auswirkungen auf das Aufsetzen der Datenbank mit django. [Hier kannst du mehr darüber lesen](https://gist.github.com/axelbdt/74898d80ceee51b69a16b575345e8457)

Wenn du also jetzt `python manage.py migrate` ausprobieren würdest, hättest du folgende Fehlermeldung: `permission denied for schema public`

Deswegen müssen wir jetzt das Schema Autorisieren und deinen Nutzer etwas anpassen:
```
CREATE SCHEMA mein_schema AUTHORIZATION mein_nutzer;
ALTER ROLE mein_nutzer SET client_encoding TO 'utf8';
ALTER ROLE mein_nutzer SET default_transaction_isolation TO 'read committed';
ALTER ROLE mein_nutzer SET timezone TO 'CET';
```

Nun sollte `python manage.py migrate` funktionieren. Das werden wir uns im nächsten Teil anschauen!
