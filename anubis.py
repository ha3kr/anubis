
import requests
import json
from argparse import ArgumentParser


parser = ArgumentParser()
parser.add_argument("-domain")
opt = parser.parse_args()

res = requests.get(f"https://jldc.me/anubis/subdomains/{opt.domain}")

loads = json.loads(res.text)

for i in loads:
    print(i)