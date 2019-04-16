#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import json
from Source_DB import *

with open('JSON_Phone.json', 'w', encoding='utf-8') as f:
    json.dump(phone_dict,f,ensure_ascii=False,indent=4)