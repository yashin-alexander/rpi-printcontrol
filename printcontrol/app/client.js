const {PrintTestFileRequest, DefaultResponse} = require('./printcontrol_pb.js');
const {PrintControlClient} = require('./printcontrol_grpc_web_pb.js');

var PrintControlService = new PrintControlClient('http://localhost:8080');
var request = new PrintTestFileRequest();

PrintTestFileRequest(request, {}, function(err, response) {
  if (err){
    console.log('Print test file error');
  } else {
    console.log('Print file success');
  }
});