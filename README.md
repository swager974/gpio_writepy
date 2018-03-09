# gpio_writepy

Fonctionnel au 09/03/2018

Utlisation du GPIO du raspberry avec Gladys et Python

## Getting Started

### Prerequisites
- Raspberry
- Gladys >= 3.8.0

https://gladysproject.com/

Ce module pour gladys permet d'activer les sorties du GPIO du raspberry

Installation du module directement par gladys/modules/Avancé et y mettre ce lien git.(https://github.com/swager974/gpio_writepy.git)


## Deployment

Exemple pour une lumiere par detecteur infrarouge PIR

La detection est faite par le fichier motion_sensor.py totalement indépendant de gladys, ce dernier est lancé au démarrage du raspberry et s'occupe de la lecture des PINs du GPIO.
Lorsqu'il y a une detection PIR le fichier python appel un HTTP token sur gladys avec une event :
http://IP_GLADYS/event/create?token=TOKEN_GLADYS&code=motion-pir&user=1&house=1


Pour creer un event, sur gladys->scripts et executer :
```
type = {
"code": "motion-pir",
"name": "Detection PIR",
"description": "Un utilisateur est detecté",
"service": 0,
"category": "user",
"faIcon": "fa fa-briefcase",
"iconColor": "bg-light-blue",
};

gladys.eventType.create(type);
```

Scripts pour un scénario lumière automatique :
```
gladys.modules.gpio_write.exec(PIN_GPIO,1); // Remplacer PIN_GPIO par le PIN, [PIN,ETAT(0:False;1:True)]

//120 secondes temporisation
setTimeout(function(){
    gladys.modules.gpio_write.exec(PIN_GPIO,'0');
}, 120000);
``````

Pour information voici les codes event d'origine avec gladys :

``````
back-at-home
left-home
wake-up
going-to-sleep
gladys-installed
gladys-updated
sunrise
sunset
enter-area
devicetype-new-value
house-mode-changed
user-seen-at-home
```
