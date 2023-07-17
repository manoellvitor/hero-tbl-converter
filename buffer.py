import logging
from const import type_sizes, ColType
from conversions import bytes_to_float, bytes_to_int, float_to_bytes, int_to_bytes


class Buffer:
    def __init__(self, data):
        self.data = bytearray(data)
        self.offset = 0

    def read(self, t):
        data = self.read_n(type_sizes[t])
        if t == ColType.BYTE:
            return data[0]
        elif t == ColType.INT16:
            return bytes_to_int(data, True)
        elif t == ColType.UINT16:
            return bytes_to_int(data, True)
        elif t == ColType.INT32:
            return bytes_to_int(data, True)
        elif t == ColType.UINT32:
            return bytes_to_int(data, True)
        elif t == ColType.FLOAT:
            return bytes_to_float(data, True)
        else:
            return None

    def read_n(self, n):
        if self.offset == len(self.data):
            return bytearray()

        if len(self.data) >= self.offset + n:
            self.offset += n
            return self.data[self.offset - n : self.offset]

        data = self.data[self.offset :]
        self.offset = len(self.data)
        return data

    def write(self, value, t):
        if t == ColType.STRING:
            data = value.encode()
            length = len(data)
            self.data.extend(int_to_bytes(length, 4, True))
            self.offset += 4
            self.data.extend(data)
            self.offset += length
            return

        try:
            val = float(value)
        except ValueError as e:
            logging.FATAL(e)

        if t == ColType.BYTE:
            self.data.append(int(val))
            self.offset += 1
        elif t == ColType.INT16:
            data = int_to_bytes(int(val), 2, True)
            self.data.extend(data)
            self.offset += 2
        elif t == ColType.UINT16:
            data = int_to_bytes(int(val), 2, True)
            self.data.extend(data)
            self.offset += 2
        elif t == ColType.INT32:
            data = int_to_bytes(int(val), 4, True)
            self.data.extend(data)
            self.offset += 4
        elif t == ColType.UINT32:
            data = int_to_bytes(int(val), 4, True)
            self.data.extend(data)
            self.offset += 4
        elif t == ColType.FLOAT:
            data = float_to_bytes(float(val), 4, True)
            self.data.extend(data)
            self.offset += 4

    def overwrite(self, data, i):
        _data = bytearray(data)
        self.data[i : i + len(data)] = _data

    def get_bytes(self):
        return self.data

    def get_offset(self):
        return self.offset
    
    def write_bytes(self, data):
        self.data.extend(data)
        self.offset += len(data)
