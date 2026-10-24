#!/usr/bin/env python3

import hashlib
import sys

if len(sys.argv) < 2:
    print("""=bletsch's secret sauce=
    usage: test_hasher.py <filename>""")
    exit(1) 

m = hashlib.md5()
MAC_KEY = b'[Wow! This string is our MAC key!]'

with open(sys.argv[1], "rb") as bin:
    # m.update(MAC_KEY)
    m.update(bin.read())
    m.update(MAC_KEY)
    print(m.hexdigest())
