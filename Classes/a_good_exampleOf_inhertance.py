class InvalidOperationError(Exception):
    pass


class Stream:
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already open")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is alreay closed")
        self.opened = False


class FileStream(Stream):
    def read(self):
        print("Stream is read from FileStream")


class NetworkStream(Stream):
    def read(self):
        print("Stream is read from NetworkStream")
