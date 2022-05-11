#!/usr/bin/python3
import os
import json
print("Alright")
f = os.environ.get('MDCAP_ELEMENT_CONF_PATH')
print(f)
with open(f,'r') as fh:
    data = fh.read()
    data1 = json.loads(data)
    print(data1)
