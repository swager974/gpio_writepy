var Promise = require('bluebird');
var config = require('./config.js').config;
var pythonScriptPath = './api/hooks/gpio_write/lib/gpio_write.py';
var PythonShell = require('python-shell');

module.exports = function(code,etat) {
	console.log('Le module GPIO_WRITE demarre...');
	return new Promise((resolve, reject) => {
		var pyshell = new PythonShell(pythonScriptPath, {
			args: [code, etat]
		});
		pyshell.on('message', function (message) {
			return resolve(message);
		});
		pyshell.end(function (err) {
			if (err) throw err;
		});

	});
};
console.log('Module gpio_write ... fichier request.js OK .. Pret');