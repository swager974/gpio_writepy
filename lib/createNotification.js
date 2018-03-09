var Promise = require('bluebird');
var queries = require('./queries.js');
var config = require('./config.js').config;

module.exports = function(code, data) {
	var text = `Le statut du PIN ${code} a changé : ${data}`;
	
	return gladys.utils.sqlUnique(queries.getNotificationCount, [code, text])
		.then(notificationCount => {
			if (notificationCount.nb === 0) {
				var notification = {
					user: 1,
					title: 'Pin ${code} change pour etat ${data}',
					text: text,
					link: config.nom,
					icon: 'fa fa-home',
					iconColor: 'bg-light-blue',
					priority: 0
				};
				
				return gladys.notification.create(notification);
			}
			
			return Promise.resolve();
		});
};