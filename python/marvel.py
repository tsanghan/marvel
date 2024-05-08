#!/use/bin/env python
from hashlib import md5
import os
import requests
import time
import urllib3
import ssl

baseurl="https://gateway.marvel.com/v1/public"
pub_key = os.environ["PUB_KEY"]
pri_key = os.environ["PRI_KEY"]

paths = ['characters', 'comics', 'creators', 'events', 'series', 'stories']
sub_paths = ['comics', 'events', 'series', 'stories']

class SslOldHttpAdapter(requests.adapters.HTTPAdapter):
    def init_poolmanager(self, connections, maxsize, block=False):
        ctx = ssl.create_default_context()
        ctx.set_ciphers('DEFAULT@SECLEVEL=1')

        self.poolmanager = urllib3.poolmanager.PoolManager(
            ssl_version=ssl.PROTOCOL_TLS,
            ssl_context=ctx)


def fn_hash(ts: int, pub_key: str, pri_key: str) -> str:
    return md5(f'{ts}{pri_key}{pub_key}'.encode()).hexdigest()


def main() -> None:
    ts = int(time.time())
    query_str = {"ts": ts, "apikey": pub_key, "hash": fn_hash(ts, pub_key, pri_key), "name":"Hulk"}
    session = requests.Session()
    # qsession.mount(baseurl, SslOldHttpAdapter())
    response = session.get(f"{baseurl}/characters", params=query_str)
    print(response.status_code)
    print(response.json())


if __name__ == "__main__":
    main()


