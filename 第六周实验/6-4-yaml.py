#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import yaml
from Source_DB import *

f = open('souce_db.yml',encoding='utf-8')
x = yaml.safe_load(f)
#x = yaml.dump(phone_dict,allow_unicode = True)
print (x)