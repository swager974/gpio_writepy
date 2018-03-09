var queries = require('./queries.js');
var config = require('./config.js').config;

module.exports = function() {
	return gladys.utils.sql(queries.deleteAction, [config.nom])
		.then(() => gladys.utils.sql(queries.deleteLauncher, [config.nom]))
		.then(() => gladys.utils.sql(queries.deleteAlarm, [config.nom]))
		.then(() => gladys.utils.sql(queries.deleteScript, [config.nom]))
		.then(() => gladys.utils.sql(queries.deleteAllNotifications, [config.nom]));
};