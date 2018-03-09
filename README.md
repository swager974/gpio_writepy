# gpio_writepy

Fonctionnel au 09/03/2018

Ecrire sur le GPIO du raspberry avec Gladys et Python

Module pour Gladys 3.8.0
https://gladysproject.com/

Permet d'activer les sorties du GPIO du raspberry

Installation du module directement par gladys/modules/Avancé et y mettre ce lien git.(https://github.com/swager974/gpio_writepy.git)



Exemple pour une lumiere par detecteur infrarouge PIR

La detection est faite par le fichier python totalement indépendant de gladys, ce dernier est lancé au démarrage du raspberry, lorsqu'il y a une detection le fichier python appel un HTTP token sur gladys avec un event exemple "motion-pir"
http://192.168.0.101/event/create?token=TOKEN_GLADYS&code=motion-pir&user=1&house=1

Pour creer un event, sur gladys aller dans scripts et executer :

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

Scripts pour un scénario lumieres automatique :

gladys.modules.gpio_write.exec(PIN_GPIO,ETAT); // Remplacer PIN_GPIO par le PIN et ETAT par 0 ou 1

//120 secondes temporisation
setTimeout(function(){
    gladys.modules.gpio_write.exec('11','0');
}, 120000);