from __future__ import print_function

import grpc
import io

from . import printcontrol_pb2
from . import printcontrol_pb2_grpc


def main():
    channel = grpc.insecure_channel('192.168.1.228:5000')
    stub = printcontrol_pb2_grpc.PrintControlStub(channel)
    # response = stub.print_test_page(printcontrol_pb2.PrintTestPageRequest())

    response = stub.print_file(printcontrol_pb2.PrintFileRequest(filename='23.pdf'))
    print("respose status: {}, response error: {}".format(response.status, response.error))

    # response = stub.get_uploaded_files(printcontrol_pb2.GetUploadedFilesRequest())
    # print("files: {}, respose error: {}".format(response.files, response.error))

    # response = stub.remove_file(printcontrol_pb2.RemoveFileRequest(filename='1'))
    # print("respose status: {}, response error: {}".format(response.status, response.error))

    # response = stub.remove_all_files(printcontrol_pb2.RemoveAllFilesRequest())
    # print("respose status: {}, response error: {}".format(response.status, response.error))

    # response = stub.get_uploaded_files(printcontrol_pb2.GetUploadedFilesRequest())
    # print("files: {}, respose error: {}".format(response.files, response.error))

    # fileio = io.FileIO('/home/alexander/Downloads/download.pdf', mode='rb')
    # file_content = fileio.read()
    # fileio.close()
    # response = stub.upload_file(printcontrol_pb2.UploadUnit(filename='23.pdf', content=file_content))
    # print("respose status: {}, response error: {}".format(response.status, response.error))
