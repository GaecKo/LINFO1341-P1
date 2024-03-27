## Acces File:
**Scénario**: On accède au drive (en étant DEJA connecté avec uclouvain), puis on clique sur "Ajouter" puis "Téléverse" puis j'ai ajouté un fichier (temp.py), attendu qu'il soit uploaded et arrêté l'analyse
### Statistics 
1) protocol hierarchy
* IPv6: 
    * TCP: 
    * UDP: 
        * MDNS: 
* IPv4: 
    * TCP: 
        * TLS: 
    * UDP: 
        * MDNS: 
        * DNS: 

2) Conversations
* IPv4:
    * 

* IPv6:
    * 

* TCP:
    * 

* UDP:
    > port 53: DNS from TCP/UDP -> to verify
    > port 5353: Multicast DNS (mDNS) enables DNS-like operations within local networks without needing a traditional DNS server. It operates on UDP port 5353 and allows devices to discover each other and their services, commonly seen in various IoT devices.
    > port 1900: Microsoft for SSDP

`traceroute -n -U -p 443 --sport=4000 drive.shadow.tech`:
```bash
traceroute to drive.shadow.tech (46.105.132.157), 30 hops max, 60 byte packets
 1  192.168.1.1  5.813 ms  174.144 ms  45.879 ms
 2  10.24.145.8  11.340 ms  13.012 ms  284.127 ms
 3  * * *
 4  91.183.242.132  13.027 ms  29.869 ms  407.397 ms
 5  * * *
 6  * * *
 7  * * *
 8  * * *
 9  * * *
10  91.121.131.149  118.636 ms  19.464 ms  19.510 ms
11  * * *
12  * * *
13  * * *
14  * * *
15  * * *
16  * * *
17  * * *
18  * * *
19  * * *
20  * * *
21  * * *
22  * * *
23  * * *
24  * * *
25  * * *
26  * * *
27  * * *
28  * * *
29  * * *
30  * * *
```


#### DNS
    — Combien de noms de domaines sont résolus et quand ?
        * 
    — Quels sont les serveurs autoritatifs pour ces noms de domaines ? Sont-ils gérés par des entreprises différentes ?
    — À quelles entreprises appartiennent les noms de domaines résolus ? Il y en a-t-il d’autres que celle qui détient l’application ?
    — Quels sont les types de requête DNS effectuées ?
    — Lorsqu’une requête DNS souhaite obtenir une adresse IP, quelle est sa famille ? Il y a-t-il une version IP préférée par l’application ?
    — Les requêtes contiennent elles des records additionnels ? Le cas échéant, à quoi servent-ils ?
    — Observez-vous des comportements DNS inattendus ?


#### Couche réseau
    — Lorsque IPv4 est utilisé, l’application utilise-t-elle des techniques pour traverser les NAT 3 .
    — Quels sont les adresses vers lesquels des paquets sont envoyés ? Retrouvez à quels noms
    de domaine elles correspondent, observez-vous une tendance particulière dans la famille d’adresse ? Pouvez-vous l’expliquer ?

#### Couche transport 
    — Quels sont les protocoles de transports utilisés pour chaque fonctionnalité ?
    — Il y a-t-il plusieurs connexions vers un même nom de domaine ? Si oui, pouvez-vous l’expliquer ?
    — Si vous observez du trafic QUIC, quels sont les versions utilisées ? Pouvez-vous identifier des extensions négociées dans le handshake ?
    — Lorsque vous observez du trafic UDP, identifiez-vous d’autres protocoles que QUIC et DNS ? Expliquez comment ils sont utilisés par l’application.

#### Chiffrement / sécurité
    — L’utilisation du DNS est-elle sécurisée ? Comment ?
    — Quelles versions de TLS sont utilisées ? Précisez les protocoles de transport sécurisés par ces versions.
    — Quel est la durée de vie des certificats utilisés ? Par qui sont-ils certifiés ?
    — Lorsque vous pouvez observer l’établissement du chiffrement, quels sont les algorithmes de chiffrement utilisés ?
    — Si vous observez du trafic UDP, semble-t-il chiffré ? Comment est-il sécurisé ?

#### Application
— Quels comportements observer-vous lors du transfert de nouveaux fichiers comparé à la modification de fichiers existant ? Quel impact a la modification par plusieurs utilisateurs par rapport à un seul ?
— Quel est le volume de données échangées par l’application pour chacune de ces fonctionnalités ? Utilisez une base appropriée permettant la comparaison (par ex. par minute).
— Il y a-t-il des serveurs relais utilisés pour interagir avec un utilisateur ou les applications communiquent-elles directement ? Observez-vous autre chose lorsque deux utilisateurs sont sur le même réseau Wi-Fi 4 ?
— Est-ce qu’interagir avec un utilisateur se trouvant dans le même réseau Wi-Fi ou Ethernet a un impact sur la façon dont le trafic applicatif est transporté ? Il y a-t-il des serveurs relais ?

