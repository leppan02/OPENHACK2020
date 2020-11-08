import requests
from weapon_code import  *
from urllib.parse import quote
from country_code import get_country
URL = 'https://armstrade.sipri.org/armstrade/html/export_trade_register.php'
import threading 
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
        cur = {'country_from':country,'country_to':data[0].lstrip(), 'source': URL, 'api_key':key, 'weapon_name': get_weapon(weapon_type),'trade_start':"{}-01-01".format(year), 'trade_end': "{}-01-01".format(year+1)}
        if cur['country_to'] == '':
            cur['country_to'] = last
            try:
                cur['amount'] = int(data[2].replace('(', '').replace(')', '').replace(' ', ''))
            except:
                continue
        else: 
            last = cur['country_to']
            try:
                cur['amount'] = int(data[1].replace('(', '').replace(')', '').replace(' ', ''))
            except:
                continue
        if 'ignore' not in cur:
            suppliers.append(cur)
    return suppliers

def send(packages):
    if len(packages):
        resp = requests.post('http://l-h.nu/api/add_trades',json=packages)
        print("worked")

def run(key, country_code):
    for year in range(2000, 2020):
        ids = [1,2,3,4,5,6,7,11,12,13,14]
        for id in ids:
            try:
                country = get_country(country_code)
                text = get_rtf(country_code=country_code, year=year, id=id)
                if text != False: 
                    data = text.decode('utf8').split('\n')
                    ret = []
                    for line in data:
                        if country in line:
                            ret = parse(line, country,key ,id, year)
                    send(ret)
            except KeyboardInterrupt:
                raise

if __name__ == "__main__":
    codes = ['AF', 'ALB', 'ALG', 'XLA', 'XSA', 'ANG', 'XCC', 'ARG', 'XGC', 'ARM', 'ARU', 'AUS', 'AST', 'AZB', 'BAS', 'BAH', 'BAN', 'BAR', 'BLR', 'BEL', 'BLZ', 'BEN', 'BHU', 'BIA', 'BOL', 'BOS', 'BOT', 'BRA', 'BRU', 'BUL', 'BF', 'BDI', 'CAP', 'CMB', 'CAM', 'CAN', 'CAR', 'CHA', 'CHE', 'CHI', 'COL', 'COM', 'CON', 'XNC', 'COS', 'IVO', 'CRO', 'CUB', 'CYP', 'CZR', 'CZE', 'XSD', 'DEN', 'DJI', 'DOM', 'DRC', 'GDR', 'ECU', 'EGY', 'XEE', 'SAL', 'XEP', 'EQU', 'ERI', 'EST', 'SWA', 'ETH', 'EU', 'EUR', 'XCF', 'FJI', 'FIN', 'XSF', 'XAF', 'FRA', 'XPR', 'GAB', 'GAM', 'GEO', 'FRG', 'GHA', 'GRE', 'GND', 'GUA', 'GUI', 'GBI', 'XCG', 'GUY', 'HAI', 'XHB', 'XPA', 'XLH', 'HON', 'XYH', 'HUN', 'ICE', 'IND', 'INS', 'XIR', 'IRA', 'IRQ', 'IRE', 'ISR', 'ITA', 'JAM', 'JAP', 'JOR', 'KAT', 'KAZ', 'KEN', 'XCR', 'KIR', 'KSV', 'KUW', 'KYR', 'LAO', 'LAT', 'LEB', 'XLP', 'LES', 'XLL', 'LIB', 'LYA', 'LYW', 'LYE', 'LIT', 'XUL', 'XSL', 'LUX', 'MAC', 'MAD', 'MWI', 'MAL', 'MLV', 'MLI', 'MTA', 'MAR', 'MRA', 'MAU', 'MEX', 'MIC', 'XPQ', 'MOL', 'MON', 'MTG', 'MOR', 'MOZ', 'XPM', 'XMX', 'XAM', 'MUL', 'MYA', 'NAM', 'NAT', 'NEP', 'NET', 'NZ', 'NIC', 'NIR', 'NIG', 'XMN', 'XAN', 'NCY', 'KON', 'YEN', 'NOR', 'XLB', 'OMA', 'OSC', 'XPP', 'PAK', 'PAL', 'PA', 'PAN', 'PAP', 'PAR', 'XLO', 'PER', 'PHI', 'XID', 'XTP', 'XIP', 'POL', 'POR', 'XPC', 'XUI', 'QAT', 'RSS', 'ROM', 'XRR', 'XSR', 'RUS', 'RWA', 'SKN', 'SVG', 'SAM', 'SAU', 'SEN', 'SER', 'SEY', 'SIE', 'SIN', 'XLS', 'SLK', 'SLO', 'XSY', 'SOL', 'SOM', 'SA', 'XYS', 'KOS', 'SSD', 'VNS', 'YES', 'USR', 'SPA', 'XSP', 'SRI', 'SUD', 'SUR', 'SWE', 'SWI', 'SYR', 'XSX', 'TAI', 'TAJ', 'TAN', 'THA', 'ET', 'TOG', 'TON', 'TRI', 'TUN', 'TUR', 'TRK', 'TUV', 'UAE', 'UGA', 'XSI', 'UKR', 'XUR', 'XAU', 'UK', 'UNO', 'USA', 'XMU', 'XXX', 'XXU', 'XXR', 'XXS', 'URU', 'UZB', 'VAN', 'VEN', 'XVC', 'XFV', 'VN', 'SAH', 'YEM', 'YAR', 'YUG', 'ZAM', 'XZZ', 'ZIM']
    key = requests.post('http://l-h.nu/api/generate', json={"email": "admin@admin", "full_name":"leopold"}).content.decode('utf8')
    ts = []
    for country_code in codes:
        ts.append(threading.Thread(target=run, args=(key, country_code,)) )
        ts[-1].start()
    for t in ts:
        t.join()
