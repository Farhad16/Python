from abc import ABC, abstractmethod


class InvalidOperationError(Exception):
    pass


class Stream(ABC):
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

    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("Stream reads from FileStream")


class NetworkStream(Stream):
    def read(self):
        print("Stream reads from NetworkStream")


class MemoryStream(Stream):
    def read(self):
        print("Stream reads from Memory Stream")


m = MemoryStream()
m.read()
