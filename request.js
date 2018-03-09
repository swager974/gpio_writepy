var Promise = require('bluebird');
var config = require('./config.js').config;
var pythonScriptPath = './gpio_write.py';

var PythonShell = require('python-shell');

module.exports = function(code,etat) {
	return new Promise((resolve, reject) => {
		var pyshell = new PythonShell(pythonScriptPath, {
			args: [code, etat]
		});
		pyshell.on('message', function (message) {
			console.log(message);
			return resolve(message);
		});
		pyshell.end(function (err) {
			if (err){ throw reject(err); };
		});

	});
};