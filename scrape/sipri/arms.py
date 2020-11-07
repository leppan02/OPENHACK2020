import requests
from weapon_code import  *
from urllib.parse import quote
from country_code import get_country
URL = 'https://armstrade.sipri.org/armstrade/html/export_trade_register.php'
def urlencode_withoutplus(query):
    if hasattr(query, 'items'):
        query = query.items()
    l = []
    for k, v in query:
        k = quote(str(k), safe=' /+')
        v = quote(str(v), safe=' /+')
        l.append(k + '=' + v)
    return '&'.join(l)

def get_rtf(country_code='SWE', year=2019, id=1): 
    url = URL

    headers = {
        "Host": "armstrade.sipri.org",
        "Connection": "close",
        "Content-Length": "225",
        "Cache-Control": "max-age=0",
        "Upgrade-Insecure-Requests": "1",
        "Origin": "https://armstrade.sipri.org",
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "navigate", 
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "document",
        "Referer": "https://armstrade.sipri.org/armstrade/page/trade_register.php",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.9,sv;q=0.8",
    }

    data = {
        "include_open_deals": "on",
        "selFromseller_country_code": country_code,
        "seller_country_code": "+"+country_code,
        "buyer_country_code": "",
        "low_year": year,
        "high_year": year,
        "armament_category_id": str(id),
        "buyers_or_sellers": "sellers",
        "filetype": "rtf",
        "sum_deliveries": "on", 
        "Submit4": "Download"
    }

    r = requests.post(url, data=urlencode_withoutplus(data), headers=headers)
    if b'<!DOCTYPE html' in r.content: 
        return False
    else:
        return r.content


def parse(data, country, key, weapon_type,year):
    lines = data.split('{\\b     }')

    suppliers = []
    last = ''
    for line in lines: 
        data = line.replace('\\par{', '').replace('\\b', '').replace('R:}', '').replace('{ '+country+'}', '').split('\\tab')
        cur = {'country_from':country,'country_to':data[0].replace(' ', ''), 'source': URL, 'api_key':key, 'weapon_name': get_weapon(weapon_type),'trade_start':"{}-01-01".format(year), 'trade_end': "{}-01-01".format(year+1)}
        if cur['country_to'] == '':
            cur['country_to'] = last
        else: 
            last = cur['country_to']
        if 'ignore' not in cur:
            suppliers.append(cur)
    return suppliers



if __name__ == "__main__":
    country_code = "USA"
    year = 2019
    id = 4

    country = get_country(country_code)
    key = requests.post('http://l-h.nu/api/generate', json={"email": "admin", "full_name":"leopold"}).content.decode('utf8')
    text = get_rtf(country_code=country_code, year=year, id=id)
    if text != False: 
        data = text.decode('utf8').split('\n')
        ret = []
        for line in data:
            if country in line:
                ret = parse(line, country,key ,id, year)
        for i in ret:
            print(i)
    else: 
        print ("Can't get data")