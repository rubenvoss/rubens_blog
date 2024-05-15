# Wie man eine django Webapp in Produktion aufsetzt (Teil 1)
## Vorwort

In dieser Post-Reihe geht es darum, eine django webapp Produktionsbereit zu machen.
Es gibt viele verschiedene Möglichkeiten das zu tun, aber hier werden wir uns einfach einen VPS mit Debian schnappen und alle Programme darauf laufen lassen.
Das ganze ist gut für Applikationen, die keine großen Skalierungsprobleme haben.

Außerdem werden wir dem ganzen über GitHub und webhooks kontinuierliche updates zukommen lassen - Continuous Deployment.

## Unser Stack

```
- Debian 12
- Django 5.0.6
- postgresql 15.6
- gunicorn 21.2.0
- nginx 1.22.1
- webhook 2.8.0
- ufw 0.36.2
```

## Wieso machen wir das so?

Wieso sollte Ich meine App nicht einfach auf einer Cloud-Service Platform hosten?
Du bist dann auch von dieser Platform abhängig. Sie verlangen einen Preis und den musst du dann bezahlen. Sobald deine Versionen etwas älter sind, geht deine Rechnung dann nochmal hoch. Um wirklich die Vorteile der Cloud zu nutzen, musst du sogar dann die Cloud-Services Nutzen, die es speziell nur bei einem Anbieter gibt.
So wie wir das ganze hier aufsetzen, kann man es einfach lassen und vergessen.
Außerdem wirst du viel darüber lernen, wie django und Webapplikationen generell sich in Produktion verhalten. In Produktion ist nämlich nochmal einiges anders als in der Entwicklung.

Mit dieser Art und Weise kannst du deine App sehr günstig auf irgend einem Hoster Hosten, kannst hoster wechseln und solange deine Nutzerzahlen nicht explodieren alles einfach in Ruhe lassen. Sobald deine Nutzerzahlen dann ansteigen, lohnt es sich erste Änderungen in Skalierungsrichtung zu unternehmen. Denn Kubernetes & Containerisierte Infrastruktur brauchen viel Zeit um gut aufgesetzt zu werden.

## Server Aufsetzen

## VPS kaufen

Ich habe meinen VPS auf hetzner gekauft, aber jeder andere Hosting-Anbieter geht an sich auch. 
[Hetzner Cloud Link](https://www.hetzner.com/de/cloud/)

## Nutzer erstellen

Direkt nach kauf kommst du normalerweise als 'root' Nutzer auf den VPS. Der root Nutzer hat alle Rechte, ist deswegen nützlich aber auch gefährlich. Es ist eine gute Idee dir einen Nutzer anzulegen und diesem Nutzer sudo-rechte zu geben. Dadurch wird dein Server sicherer.
```
adduser mein_nutzername
adduser mein_nutzername sudo
```

## Sicherheit

Weil dein Server eine Produktive app hostet, sollte es am besten nicht möglich sein sich als root Nutzer über ssh einzuloggen. Vor allem wenn du das über das Passwort tun kannst **musst** du hier etwas für die Sicherheit des Servers tun. Es gibt ständig ssh log-in Versuche als root, das sind eben bots die versuchen auf deinen Server Zugriff zu bekommen. Um diesen den Eintritt zu verwehren musst du einfach das root-login ausschalten und nur das login über deinen personalisierten Nutzer erlauben.

Generiere dir auf deinem eigenen Computer einen ssh-key, falls du noch keinen hast. Du kannst die Standard Einstellungen bestätigen. Nach Erstellung sollte sich der key unter ~/.ssh/ befinden. Es sollten sich dort nun eine id_rsa und eine id_rsa.pub - Datei befinden.
Wenn du Windows nutzt, [hole dir WSL](https://learn.microsoft.com/en-us/windows/wsl/install)
```
ssh-keygen
ls -l ~/.ssh/id_rsa*
```

Jetzt kannst du deinen ssh-key bei deinem Server hinzufügen, um dich mit deinem Nutzer sicher einloggen zu können.
```
ssh-copy-id mein_nutzername@meine.server.ip
# teste das ganze
ssh mein_nutzername@meine.server.ip
```

Nun kannst du dem root user verbieten sich via ssh key / Passwort einzuloggen. Ebenso solltest du deine eigene Möglichkeit, dich via Passwort einzuloggen entfernen. Aber vorsicht! nachdem du die sshd_config verändert hast, kannst du dich nur noch mit deinem ssh-key einloggen! Verliere ihn nicht...
```
sudo vi /etc/ssh/sshd_config

# Folgende Einstellungen setzen / ändern
PasswordAuthentication no
PubkeyAuthentication yes
PermitRootLogin no

# Jetzt probieren ob das ganze geklappt hat!!
ssh my_username@my.server.ip
ssh root@my.server.ip
# Beim root login-versuch sollte folgende Nachricht erscheinen:
root@xxx.xxx.xxx.xx: Permission denied (publickey).
```

Vielen Dank fürs lesen!
Im nächsten Teil wird es um die Datenbank gehen...
