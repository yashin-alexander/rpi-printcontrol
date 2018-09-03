protobuf:
	python3 -m grpc_tools.protoc --proto_path=. --python_out=. --grpc_python_out=. printcontrol/printcontrol.proto
	protoc -I=printcontrol printcontrol.proto --js_out=import_style=commonjs:printcontrol/app
	protoc -I=printcontrol printcontrol.proto  --grpc-web_out=import_style=commonjs,mode=grpcwebtext:printcontrol/app
