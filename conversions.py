import math
import struct


def int_to_bytes(dec, bytes, reverse):
    arr = bytearray(8)
    if dec == 0:
        return arr[:bytes]

    if bytes < 8:
        dec = dec % (1 << (bytes * 8))

    for i in range(7, -1, -1):
        power = int(math.pow(256, i))
        arr[i] = dec // power
        if arr[i] > 0:
            dec -= arr[i] * power

    if reverse:
        return arr[:bytes]

    return reverse_bytes(arr)[8 - bytes : 8]


def bytes_to_int(arr, reverse):
    total = 0
    _arr = bytearray(arr)

    if reverse:
        _arr = reverse_bytes(_arr)

    for i in range(len(_arr)):
        power = int(math.pow(256, len(_arr) - (i + 1)))
        total += _arr[i] * power

    return total


def bytes_to_float(arr, reverse):
    return struct.unpack(">f" if reverse else "<f", arr)[0]


def float_to_bytes(dec, bytes, reverse):
    return int_to_bytes(
        struct.unpack(">I" if reverse else "<I", struct.pack(">f", dec))[0],
        bytes,
        reverse,
    )


def reverse_bytes(input):
    if len(input) == 0:
        return input

    return input[::-1]
