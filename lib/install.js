var config = require('./config.js').config;

module.exports = function() {

	var script = {
		name : 'PIN en postion HIGH',
		user : 1,
		text :
`gladys.modules.gpio_write.exec({pin:"11", etat:"true"});`
	};
	
	return gladys.script.create(script);
};