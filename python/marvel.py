#!/use/bin/env python
from hashlib import md5
import os
import requests
import time

baseurl="https://gateway.marvel.com/v1/public"
pub_key = os.environ["PUB_KEY"]
pri_key = os.environ["PRI_KEY"]

paths = ['characters', 'comics', 'creators', 'events', 'series', 'stories']
sub_paths = ['comics', 'events', 'series', 'stories']

def myhash(pub_key, pri_key):
    return md5(f'{int(time.time())}{pri_key}{pub_key}'.encode()).hexdigest()





