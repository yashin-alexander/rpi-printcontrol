from concurrent import futures
import time
import grpc
import cups
import os
import io

from . import printcontrol_pb2
from . import printcontrol_pb2_grpc


_ONE_DAY_IN_SECONDS = 60 * 60 * 24
FILES_PATH = '/home/pi/files/'


class PrintControl(printcontrol_pb2_grpc.PrintControlServicer):
    def __init__(self):
        super(PrintControl, self)
        self.cups_connection = cups.Connection()

    @property
    def printer(self):
        printers_dict = self.cups_connection.getPrinters()
        printer_list = list(printers_dict.keys())
        try:
            return printer_list.pop(0)
        except IndexError:
            return ''

    def print_test_page(self, request, context):
        try:
            self.cups_connection.printTestPage(self.printer)
        except cups.IPPError as err:
            return printcontrol_pb2.DefaultResponse(status=False, error=str(err))
        return printcontrol_pb2.DefaultResponse(status=True)

    def print_file(self, request, context):
        filepath = FILES_PATH + request.filename
        try:
            self.cups_connection.printFile(self.printer, filepath, '', {})
        except cups.IPPError as err:
            return printcontrol_pb2.DefaultResponse(status=False, error=str(err))
        return printcontrol_pb2.DefaultResponse(status=True)

    def get_uploaded_files(self, request, context):
        try:
            files_list = os.listdir(FILES_PATH)
        except OSError as err:
            return printcontrol_pb2.UploadedFilesInfo(error=str(err))
        return printcontrol_pb2.UploadedFilesInfo(files=files_list)

    def remove_file(self, request, context):
        filepath = FILES_PATH + request.filename
        if os.path.isfile(filepath):
            os.remove(filepath)
            return printcontrol_pb2.DefaultResponse(status=True)
        return printcontrol_pb2.DefaultResponse(status=False, error="No such file")

    def remove_all_files(self, request, context):
        try:
            files_list = os.listdir(FILES_PATH)
        except OSError as err:
            return printcontrol_pb2.DefaultResponse(status=False, error=str(err))
        for unit in files_list:
            os.remove(FILES_PATH + unit)
        return printcontrol_pb2.DefaultResponse(status=False)

    def upload_file(self, request, context):
        file_content = request.content
        filename = request.filename
        with open(FILES_PATH + filename, "wb") as unit:
            unit.write(file_content)

        return printcontrol_pb2.DefaultResponse(status=True)


def main():
    server = grpc.server(futures.ThreadPoolExecutor())
    printcontrol_pb2_grpc.add_PrintControlServicer_to_server(PrintControl(), server)
    server.add_insecure_port('[::]:5000')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)
