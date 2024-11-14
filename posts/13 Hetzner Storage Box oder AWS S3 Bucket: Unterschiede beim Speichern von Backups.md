# Hetzner Storage Box oder AWS S3 Bucket: Unterschiede beim Speichern von Backups

Die Hetzner Storage Box bietet ein sehr einfaches Preismodell an. So kostet beispielsweise die ein Terabyte Große Storage Box 3,20 € pro Monat (0,0032 € pro GB pro Monat). Bei AWS ist das Preismodell deutlich komplexer, aber auch flexibler. Hier wird direkt pro Gigabyte abgerechnet. AWS bietet mehrere Preisklassen an, in denen die Daten nicht sofort wiederhergestellt werden können, sondern erst nach einigen Stunden. Da wir größere Aussetzer vermeiden und immer sofort auf unsere Daten zugreifen möchten, passt AWS S3 nicht optimal zu unseren Anforderungen.

Außerdem wussten wir, dass wir das Terabyte sowieso füllen werden. Wenn man bei Hetzner mehr als ein Terabyte nutzt, z.B. 20 Terabyte, wird der Speicher, auf den wir ja immer sofortigen Zugriff haben, sehr günstig – nur 0,00203 € pro GB pro Monat. Zum Vergleich: AWS S3 kostet für sofort abrufbaren Speicher (Instant Retrieval) 0,004 $ pro Gigabyte pro Monat. Also fast doppelt so Teuer

Also war die Entscheidung leicht: Wir werden unsere Backup-Daten in einer Hetzner Storage Box speichern.

### Anleitung zur Nutzung der Hetzner Storage Box

Nun die Storage Box kaufen und ab zu [Hetzner Robot](https://robot.hetzner.com/storage). Dort solltest du deine Storage Box jetzt sehen. Wenn du sie anklickst, steht neben "Server" dein Servername und etwas weiter unten dein Benutzername. Du kannst dich nun über SSH mit deiner Storage Box verbinden.

Drücke noch eben den Passwort-Reset-Button, um dir dein neues Passwort anzeigen zu lassen, und dann los:

```bash
# Nutze Port 23
ssh -p 23 mein_user@mein_user.your-storagebox.de
```

Jetzt solltest du mit deinem Passwort in einer Shell landen:

```plaintext
Last login: Wed Jul 10 13:14:02 2024 from ***
+------------------------------------------------------------------+
| Welcome to your Storage Box.                                     |
|                                                                  |
| Please note that this is only a restricted shell environment and |
| therefore some shell features like pipes and redirects are not   |
| supported.                                                       |
+------------------------------------------------------------------+
mein_user /home >  
```

Du kannst jetzt in einem neuen Shell-Tab etwas auf deine Storage Box kopieren:

```bash
scp file.txt mein_user@mein_user.your-storagebox.de:file.txt
```

Jetzt zurück zu deiner Box gehen und den Inhalt auflisten:

```bash
mein_user /home > ls
file.txt
```