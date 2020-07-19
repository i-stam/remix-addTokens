#!/usr/bin/python
import sys
import os
import json


filepath = sys.argv[1]

if not os.path.isfile(filepath):
       print("File path {} does not exist. Exiting...".format(filepath))
       sys.exit()

tokens_len = len("Tokens:")
symbols_len = len("Symbols:")
magnitude_len = len("Magnitude:")
loadable_len = len("Loadable:")
redeemable_len = len("Redeemable:")

tokens = []
symbols = []
magnitudes = []
loadable = []
redeemable = []

with open(filepath) as fp:
    line = fp.readline()
    while line:
        if line[:tokens_len] == "Tokens:":
            tokens = [x.strip() for x in fp.readline().split(',')]
        elif line[:symbols_len] == "Symbols:":
            symbols_ascii = [x.strip() for x in fp.readline().split(',')]
            for sym in symbols_ascii:
                symbol_hex = "0x" + sym.encode('hex')
                symbol_hex = symbol_hex + (32-len(sym))*"00"
                symbols.append(symbol_hex)
        elif line[:magnitude_len] == "Magnitude:":
            magnitudes_packed = [x.strip() for x in fp.readline().split(',')]
            for mag in magnitudes_packed:
                magnitudes.append(str(10 ** int(mag)))
        elif line[:loadable_len] == "Loadable:":
            loadable = [x.strip() for x in fp.readline().split(',')]
        elif line[:redeemable_len] == "Redeemable:":
            redeemable = [x.strip() for x in fp.readline().split(',')]
        line = fp.readline()

assert len(tokens) == len(symbols)
assert len(magnitudes) == len(symbols)
assert len(magnitudes) == len(loadable)
assert len(redeemable) == len(loadable)
print "Token addresses:"
print json.dumps(tokens); print
print "Symbols:"
print json.dumps(symbols); print
print "Magnitudes:"
print json.dumps(magnitudes); print
print "Loadable:"
print json.dumps(loadable); print
print "Redeemable:"
print json.dumps(redeemable)