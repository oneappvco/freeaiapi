import requests
from random import randint,choice as che
import os
from requests import post
from urllib.parse import urlencode

def ipinfo(ip: str):
    return requests.get(f"http://api.api4dev.ir/ipinfo?ip={ip}").json()

def domain2ip(domain: str):
    return requests.get(f"http://api.api4dev.ir/domaintoip?domain={domain}").json()["ip"]

def youtube_downloader(link: str):
    return requests.get(f"http://api4dev.ir/yt/download?url={link}").json()["url"]

def dayornight(time: str):
    return requests.get(f"http://api.api4dev.ir/day?time={time}").json()
def sendsms(mobile: str, text: str):
    requests.get(f"http://api4dev.ir/me/sms.php?mobile={mobile}&txt={text}").text
    return "."
def timenow():
    return requests.get(f"http://api.api4dev.ir/day?time=00:00").json()["timenow"]
def fal():
    fals = requests.get("https://api.codebazan.ir/fal/?type=json").json()
    return {"fal":fals["Result1"],"tabir":fals["Result"]}
def tron_balance(address: str):
    return requests.get(f"http://api.api4dev.ir/tronapi?action=getbalance&address={address}").json()["balance"]
def tas():
    return randint(1,6)

def send_request(url: str):
    try:
        return requests.get(url).text
    except Exception as er:
        return "failed to send request"+str(er)

def sendsms(mobile: str, text: str):
    txt = urlencode({"text":text})
    res = requests.get(f"https://webdows.ir/new/sms.php?phone={mobile}&{txt}&password=78451200")
    return "ok"

def phonecall(mobile: str, text: str):
    print("called")
    txt = urlencode({"text":text})
    res = requests.get(f"https://webdows.ir/new/phone.php?phone={mobile}&{txt}&password=78451200")
    return "ok"

def sstp_config():
    return che(requests.get("http://api.api4dev.ir/sstp").json()["result"])
def romantic_phrase():
    return requests.get("http://api.api4dev.ir/love").text
def find_online_item(item: str):
    text = urlencode({"text":item})
    api = requests.get(f"http://api.api4dev.ir/searchapi/search?{text}").json()["result"]
    res = []
    for i in api:
        res.append(i["body"])
    return res


def execute_linux_command(cmd: str):
    text = urlencode({"cmd":cmd})
    api = requests.get(f"http://api.api4dev.ir/linux?{text}").text
    return api
    
    
def is_domain_registered(domain: str):
    api = requests.get(f"http://api.api4dev.ir/domain?domain={domain}").json()
    json_obj = {}
    try:
        if api["result"]["status"] == "unavailable":
            json_obj["registered"] = True
        else:
            json_obj["registered"] = False
        json_obj["price"] = api["result"]["price"]
        return json_obj
    except:
        return "domain not found"
    
    
    
def domain_price(domain: str):
    api = requests.get(f"http://api.api4dev.ir/domain?domain={domain}").json()
    json_obj = {}
    try:
        json_obj["price"] = str(api["result"]["price"])+" تومان"
        return json_obj
    except:
        return "domain not found"
    
def gold_or_coin_price():
    return requests.get("http://api.api4dev.ir/tala").json()
    
def generate_tron_wallet():
    return requests.get("http://api.api4dev.ir/tronapi?action=genaddress").json()
    
    
def weather(city: str):
    city = urlencode({"city":city})
    return requests.get(f"http://api4dev.ir/ba/weather.php?{city}").text
    
    
def generate_mnemonic(words: str = "12"):
    return requests.get(f"http://backupapi.s6.vipbotdomain.top/mnemonic/?words={words}").json()
    
    
    
