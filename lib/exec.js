var Promise = require('bluebird');
var request = require('./request.js');
var createNotification = require('./createNotification.js');

module.exports = function(code,etat) {//code = PIN GPIO
	return request(code, etat) 
		.then(value => {
			sails.log.info(`[GPIO_RPI_CHANGE] On change le statut du PIN`);
			return createNotification(code, etat);
		})
		.catch(error => {
			sails.log.error(`[GPIO_ERROR] Erreur pour le PIN ${code} : ${error}`);
			return Promise.reject(error);
		});
};