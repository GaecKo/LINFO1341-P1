## Acces File:
### Statistics 
1) protocol hierarchy
* IPv6: 29
    * TCP: 14
    * UDP: 12
        * MDNS: 12
* IPv4: 152
    * TCP: 110
        * TLS: 52
    * UDP: 41
        * MDNS: 10
        * DNS: 24

2) Conversations
* IPv4:
    * 46.105.132.156: OVH server à Paris, FR. Gérer par ShadowDrive **68 packets: 21kB**
    * 35.186.227.140: Google server, à MontainView, US. **15 packets: 3kB**
    * // 185.199.108.153: GitHub server à San Francisco, US. **12 packets: 1kB** 

* IPv6:
    * 2600:1901:0:38d7:: : Google server, à MontainView, US. **8 packets: 704B**
    * 2606:4700:4400::6812:26e9 : Cloudflare, à San Francisco, US. **4 packets: 352 bytes**

* TCP:
    * 46.105.132.156 (same as in IPv4): port 443
    * 13.225.239.60 (Amazon US): port 443
    * 185.199.108.153 (same as in IPv4): port 443
    * 34.107.221.82 (Google): port 80, 4 packets
    * 2600:1901:0:38d7:: (Google): port 80
    * 2606:4700:4400::6812:26e9 (same as in IPv6): port 80
    * 192.229.221.95 (EdgeCast, US): port 80, 2 packets
    * 2a02:a000:1:213::51f3:161 (Belgacom-Proximus): port 80, 2 packets

* UDP:
    > port 53: DNS from TCP/UDP -> to verify
    > port 5353: Multicast DNS (mDNS) enables DNS-like operations within local networks without needing a traditional DNS server. It operates on UDP port 5353 and allows devices to discover each other and their services, commonly seen in various IoT devices.
    > port 1900: Microsoft for SSDP



#### DNS
    — Combien de noms de domaines sont résolus et quand ?
        * Il y a 9 requêtes DNS. Cependant, celles-ci sont toutes éffectuées depuis le localhost ou autour du réseau local. Cela est du au simple fait que la capture de traces a débuté après le chargement de la page. Cependant, nous retiendrons que le nom de domaine demandé est drive.shadow.tech
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
