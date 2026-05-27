  # Compte Rendu R2.04

- [Installation-astersik](#installation-asterisk)
- [Creation-de-compte](#creation-des-comptes-sur-asterisk)
- [configuration-des-telephones](#configuration-des-telephones)
- [Deploiement-de-la-messagerie-vocale](#deploiement-de-la-messagerie-vocale)
- [Enregistrement-dun-message-vocal](#enregeistrer-un-message-vocal)
- [Deploiement-IVR](#deploiement-IVR)


## Informations 
- les VM utilisent ETH1
- les 2 premiers chiffres du numero du tel sont ceux du poste (EX: poste 14 : 1401 et 1402)
- Serveur asterisk **(asterisk-alpine)** et serveur tftp **(alpine-std)**

## Installation-asterisk
- Login et mdp : **root, progtr00**
- Ajouter au terminal nano et ssh : **apk add nano openssh**
- On utilise ces commandes pour gerer asterisk :
- > `service asterisk (start,reload,restart)`
- Ouvrir la CLI de asterisk
- > `asterisk -r` 

## Creation des comptes sur asterisk
- On travaille dans le repertoire **/etc/asterisk**
- Pour eviter de perdre les conf de base d'asterisk, on copie les fichiers de configurations dans des fichiers avec l'extension **.conf.src**
- On cree les comptes dans **pjsip.conf**
- Config basique 
- ```
    ;=====Transport====  (ligne de commentaire)
    [transport-udp]
    Type=transport
    Protocol=udp
    Bind=0.0.0.0:5060

    ;=====Telephone==== (declarer le telephone)
    [nom_tel]
    Type=endpoint
    Context=internal
    Transport=transport-udp
    Aors=nom_tel
    Auth=authnom_tel
    Disallow=all
    Allow=ulaw

    ;=====Authentification==== (authentification du tel)
    [authnom_tel]
    Type=auth
    Auth_type=userpass
    Username=nom_tel
    Password=mdp
    

    ;====connect==== (connecter le  tel)
    [nom_tel]
    Type=aor
    Max_contacts=1 

- Pour creer les lignes de contact on utilise le fichier **extensions.conf**

- config basique du fichier :
- ```
    ;====conxtext(nom_tel)=====
    [internal]
    exten=> num_tel,priorité(1..n),Dial(PJSIP/nom_tel)
    exten=> num_tel,priorité(n..n+1),operation(Dial, hangup, answer...)

- Extensions particulières
    - S : start, tous les appels peut importe le numero
    - T : timeout, délai d’attente
    - I : si extension invalide on execute cette extension
    - _ : précède tous les filtres 
    - _20XX : tous les numéros  commençant par 20 et à 4 chiffres
    - X : chiffre entre 0 et 9
    - Z : chiffre entre 1 et 9 
    - N : chiffre entre 2 et 9 
    - . : joker (suite de chiffres)
    -  VoiceMail()        Laisse un message vocal
    - VoiceMailMain()    Accède à la messagerie vocale
    - Wait()             Attend un délai
    - WaitExten()        Attend une saisie d’extension
    - ResponseTimeout()  Définit un délai d’attente
    - SayAlpha()         Annonce vocale de caractères
    - SayDigits()        Annonce vocale de chiffres
    - SayNumber()        Annonce vocale de nombres
    - SayUnixTime()      Annonce vocale de l’heure
    - System()           Exécute une commande système
    - GotoIf()        Branchement conditionnel
    - GotoIfTime()    Branchement conditionnel selon condition temporelle
    - HangUp()        Termine une communication
    - Playback()      Lit un message audio (bloquant)
    - Read()          Lit une variable saisie par l’utilisateur
    - Record()        Enregistre une communication
    - Answer()        Répond à un appel entrant
    - Background()    Lit un message audio de manière non bloquante
    - Dial()          Met en relation deux entités
    - Echo()          Retour audio (test de ligne)
    - Goto()          Branchement inconditionnel

## Configuration des telephones
 ### Fanvil
 - Déconnecter la fiche RJ45 du téléphone
 - Maintenir la touche # et connecter la fiche RJ45 sur le port du téléphone
 - Attendre l'apparition du message Post Mode
 - Appuyer successivement sur les touches *#168
 - Attendre l'apparition du message Phone reset
 - Déconnecter et reconnecter la fiche RJ45 sur le port du téléphone
 - Lancer le navigateur avec l’ip du fanvil et entrez les id : admin admin dans le site 
 - Configurer les paramètres du tel

 ### Cisco
 - Il faut d’abord démarrer un serveur tftp (13, alpine-std sur eth 1)
 - Login root mdp progtr00
 - Ouvrir le terminal et installer le service tftp :
 - > apk add tftp-hpa 
 - > service in.tftpd start
 - > apk add openssh
 - > service sshd start
 - > apk add nano
 - Se placer dans le repertoire /var/tftpboot puis télécharger un fichier zip
 - wget http://iut-rt.univ-artois.fr/tph/Archive.zip
 - commande “unzip nom_fichier”
 - la configuration du téléphone Cisco se fait grâce au fichier SEP_MAC_CISCO_.cnf.xml
- On doit remplacer SEP_MAC_CISCO_ par l’adresse MAC du téléphone Cisco 
- On modifie ces paramètres dans le fichier SEP_MAC_CISCO_.cnf.xml :
- ```
    - <processNodeName>@IP_serveur_asterisk</processNodeName> 
    - <phoneLabel>nom_tel</phoneLabel>
    - <featureLabel>nom_tel</featureLabel>
    - <authName>nom_tel</authName>
    - <contact>nom_tel</contact>
    - Remplasser les noms Cisco par Ciscoxx correspondant au téléphone utilisé
    - service in.tftpd restart

- Configuration du cisco :
    - Paramètres
    - admin settings 
    - network setup 
    - IPV4 
    - Alternate TFTP (yes) 
    - TFTP serveur (ip du serv tftp) 
    - debrancher cable RJ45 et rebrancher

## Deploiement de la messagerie vocale
- La configuration se fait le module voicemail.conf
- Config basique :
- ```voicemail.conf
   [default]
    Num_tel => mdp_boite_vocale,nom-tel(pour les deux téléphones)
    1401 => 1234,Fanvil14(exemple)

- Il faut ensuite configurer le fichier extensions.conf pour que les appels soient redirigés vers la messagerie vocale
- ```
    exten => num_tel,priorité(1..n),Dial(PJSIP/nom_tel,20)
    exten => num_tel,priorité(n+1),Voicemail(${EXTEN}@default) 
    
    ;pour acceder a la messagerie vocale on configure une extension :
    exten => num_x,priorité(1),VoicemailMain(default)

    ;Pour accéder aux boites vocales
	exten=>888,1,VoiceMailMain($CALLERID(num)@default)
	;$CALLERID(num) est une liste contenant les informations de l'appelant
	; Ici on récupère le numéro d'extension

## Enregeistrer un message vocal
- Dans le fichier **extensions.conf** on configure une extension pour accéder à la messagerie vocale
- ``` 
    ; Exemple avec une extension variable
    exten=>_20XX,1,Wait(2)
    exten=>_20XX,n,Record(/tmp/message-${EXTEN}.gsm,1,7)
    ; les options 1 et 7 sont respectivement le temps d’attente avant le début de l’enregistrement et la durée maximale de l’enregistrement
    exten=>_20XX,n,Wait(2)
    exten=>_20XX,n,Playback(/tmp/message-${EXTEN})
    exten=>_20XX,n,Wait(2)
    exten=>_20XX,n,HangUp()

## Deploiement IVR
- Pour que les messages puissent etre lus par asterisk ils doivent etre dans le repertoire **/var/lib/asterisk/sounds**
- Apres avoir record un message vocal, on le deplace dans ce repertoire
- > mv /tmp/message-20XX.gsm /var/lib/asterisk/sounds
- Exemple de configuration d'un IVR dans le fichier **extensions.conf** :
- ```
   exten=>1000,1,goto(AccueilAnnonce,s,1)
    [AccueilAnnonce]
    exten=>s,1,Background(MsgAccueil)
    exten=>s,2,ResponseTimeOut(5)
    exten=>s,3,WaitExten()
    exten=>#,1,Goto(Service1,s,1)
    exten=>*,1,Goto(MenuPrincipal,s,1)
    exten=>i,1,Goto(s,1)
    exten=>t,1,PlayBack(MsgAuRevoir)
    exten=>t,2,HangUp()
    [Service1]
    exten=>s,1, ...
    [MenuPrincipal]
    exten=>s,1, ...



AU CAS où
extensions.conf
    [internal]
; --- Gestion des appels directs ---
; On fait sonner 12s, si pas de réponse -> Messagerie
exten => 1401,1,Dial(PJSIP/1401,12)
same => n,VoiceMail(1401@default)
same => n,Hangup()

exten => 1402,1,Dial(PJSIP/1402,12)
same => n,VoiceMail(1402@default)
same => n,Hangup()

; --- Accès messagerie (Consultation) ---
exten => 888,1,VoiceMailMain(${CALLERID(num)}@default)

; --- IVR avec Restriction Horaire (Question 4) ---
exten => 0800,1,NoOp(Verification horaires IVR)
; Si ouvert (8h-18h, Lun-Ven) -> va vers l'IVR
same => n,GotoIfTime(08:00-18:00,mon-fri,*,*?AccueilAnnonce,s,1)
; Sinon -> Message de fermeture
same => n,Playback(vm-from-outside-as-closed)
same => n,Hangup()

[AccueilAnnonce]
exten => s,1,Answer()
same => n,Playback(accueil)         ; Message bloquant
same => n(menu),Background(menuIVR) ; Message interactif
same => n,WaitExten(5)              ; Attend 5s la saisie

; Choix du menu
exten => 1,1,Goto(internal,1401,1)  ; Vers Fanvil
exten => 2,1,Goto(internal,1402,1)  ; Vers Cisco
exten => 3,1,SayUnixTime(,CET,kM)   ; Donne l'heure
exten => 4,1,Hangup()               ; Raccroche

; Gestion erreurs
exten => i,1,Goto(s,menu)           ; Mauvaise touche -> rejoue le menu
exten => t,1,Hangup()               ; Timeout -> raccroche

## Questions
Ces questions marquent la transition entre la configuration d'Asterisk et l'analyse réelle des protocoles de communication.
 Voici les éléments clés pour répondre à cette nouvelle partie de ton TP.1. 
 Diagramme de flux du protocole SIPLe protocole SIP (Session Initiation Protocol) gère uniquement la signalisation (l'établissement, la modification et la fin de l'appel).Ports d'échange : Généralement UDP 5060 (par défaut pour SIP).Adresses IP : L'adresse IP source du téléphone (ex: Fanvil) et l'adresse IP destination du serveur (Asterisk).Requêtes et réponses essentielles :INVITE : Demande d'établissement de session.100 Trying : Le serveur a reçu l'invite et traite la demande.180 Ringing : Le téléphone de destination sonne.200 OK : L'appel est accepté.ACK : Confirmation finale de l'établissement.BYE : Demande de fin d'appel.2. Diagramme de flux du protocole RTPLe RTP (Real-time Transport Protocol) transporte la voix réelle. Contrairement au SIP, il utilise des flux bidirectionnels continus.Payload Type : Indique le CODEC utilisé. Par exemple, 0 pour le PCMU (G.711u) ou 8 pour le PCMA (G.711a).Jitter (Gigue) : C'est la variation du délai de transmission entre les paquets reçus. Une gigue élevée peut hacher la voix.Taille du Payload : Pour le G.711, elle est souvent de 160 octets pour une durée de 20 ms de voix.Bande passante moyenne : Pour le CODEC G.711, elle est d'environ 80 kb/s (64 kb/s de données voix + en-têtes IP/UDP/RTP).3. Analyse avec Audacity (Spectre audio)En sauvegardant ton échange au format .wav (souvent via Wireshark : Telephony > RTP Streams > Analyze > Play Streams), tu peux l'ouvrir dans Audacity.Analyse de spectre : Analyse > Tracer le spectre.Bande passante audio : Pour un CODEC de téléphonie standard (G.711) :Fmin : environ 300 Hz.Fmax : environ 3400 Hz.C'est ce qu'on appelle la "bande passante téléphonique" classique.4. Relation Fréquence d'échantillonnage et Fréquence maximaleC'est le point théorique crucial de ton TP (Théorème de Nyquist-Shannon).Relation : La fréquence maximale d'un signal pouvant être correctement numérisée est égale à la moitié de la fréquence d'échantillonnage du CODEC ($F_{max} = F_e / 2$).Application concrète : Les CODECs standards comme G.711 utilisent une fréquence d'échantillonnage de 8000 Hz (8 kHz). C'est pourquoi la fréquence maximale relevée dans Audacity ne pourra jamais dépasser 4000 Hz (4 kHz).


2. Analyse Wireshark et Diagramme de fluxPour cette partie, tu dois lancer une capture Wireshark sur l'interface réseau de ton serveur (ETH1) pendant que tu effectues l'appel.Ce que tu vas observer dans Wireshark :Signalisation SIP (Établissement) : Tu verras les requêtes INVITE et 180 Ringing.Délai (Timeout) : Après 12 secondes sans 200 OK (décroché), Asterisk envoie un message SIP vers l'appelant pour confirmer le basculement audio.Audio RTP (Dépôt du message) : Une fois que la boîte vocale "décroche" pour enregistrer, le flux RTP commence. C'est ici que tu enregistres la phrase : "Je souhaite te parler, rappelle-moi, merci."Signalisation SIP (Fin) : En raccrochant, tu verras une requête BYE.Éléments du diagramme de flux :Pour établir ton diagramme, utilise l'outil intégré de Wireshark : Telephony > VoIP Calls > Flow Sequence.ÉtapeProtocoleDescriptionAppelSIPINVITE de l'appelant vers Asterisk.SonnerieSIP180 Ringing renvoyé par Asterisk.BasculementSIPAprès 12s, Asterisk prend la main pour la boîte vocale.MessageRTPFlux audio transportant ta voix vers le serveur.FinSIPBYE lors du raccrochage.Analyse des protocoles utilisés :SIP (UDP 5060) : Utilisé pour la gestion de l'appel (négociation des ports et codecs).RTP (UDP ports dynamiques) : Utilisé pour le transport de la voix numérisée.RTCP : Souvent présent pour surveiller la qualité du flux (statistiques sur la gigue et les paquets perdus).

