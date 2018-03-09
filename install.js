var config = require('./config.js').config;

module.exports = function() {

	var script = {
		name : 'Pin 11 => True',
		user : 1,
		text :
`gladys.modules.gpio_write.exec({pin:"11", etat:"true"});`
	};
	
	return gladys.script.create(script);
};