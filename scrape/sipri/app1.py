
import requests
import json
URL = 'https://armstrade.sipri.org/armstrade/html/export_values.php' 
def getCSV(country_code='USA'):
    payload = {'import_or_export': 'export',
    'country_code': country_code,
    'low_year': 2000,
    'high_year': 2019,
    'summarize': 'country',
    'filetype': 'csv',
    'Action': 'Download'}
    return requests.post(url=URL , data=payload).content.decode('utf8')
    

def parse(country_code, key):
    ret = []
    csv = getCSV(country_code)
    if csv[:9] == '<!DOCTYPE':
        return []
    country = csv.split('\n')[0][26:-34]
    dataframe = [i.split(',') for i in csv.split('\n')[11:-3]]
    for i in dataframe:
        countryto = i[0]
        data = i[1:]
        year = 2000
        for j in data:
            try:
                if len(j):
                    package = {'country_from':country,'country_to':countryto, 'source': URL, 'trade_start':"{}-01-01".format(year), 'trade_end': "{}-01-01".format(year+1), 'api_key':key}
                    j = int(j)
                    if j != '0':
                        package[ 'amount'] = j
                    ret.append(package)
            except:
                print('failed',{'country_from':country,'country_to':countryto, 'amount': j, 'trade_start':"{}-01-01".format(year), 'trade_end': "{}-01-01".format(year+1)})
            year+=1
    return ret

def send(packages):
    if len(packages):
        resp = requests.post('http://l-h.nu/api/add_trades',json=packages)
        print("worked")
    
if __name__ == "__main__":
    key = requests.post('http://l-h.nu/api/generate', data={"email": "admin", "full_name":"leopold"})
    codes = ['AF', 'ALB', 'ALG', 'XLA', 'XSA', 'ANG', 'XCC', 'ARG', 'XGC', 'ARM', 'ARU', 'AUS', 'AST', 'AZB', 'BAS', 'BAH', 'BAN', 'BAR', 'BLR', 'BEL', 'BLZ', 'BEN', 'BHU', 'BIA', 'BOL', 'BOS', 'BOT', 'BRA', 'BRU', 'BUL', 'BF', 'BDI', 'CAP', 'CMB', 'CAM', 'CAN', 'CAR', 'CHA', 'CHE', 'CHI', 'COL', 'COM', 'CON', 'XNC', 'COS', 'IVO', 'CRO', 'CUB', 'CYP', 'CZR', 'CZE', 'XSD', 'DEN', 'DJI', 'DOM', 'DRC', 'GDR', 'ECU', 'EGY', 'XEE', 'SAL', 'XEP', 'EQU', 'ERI', 'EST', 'SWA', 'ETH', 'EU', 'EUR', 'XCF', 'FJI', 'FIN', 'XSF', 'XAF', 'FRA', 'XPR', 'GAB', 'GAM', 'GEO', 'FRG', 'GHA', 'GRE', 'GND', 'GUA', 'GUI', 'GBI', 'XCG', 'GUY', 'HAI', 'XHB', 'XPA', 'XLH', 'HON', 'XYH', 'HUN', 'ICE', 'IND', 'INS', 'XIR', 'IRA', 'IRQ', 'IRE', 'ISR', 'ITA', 'JAM', 'JAP', 'JOR', 'KAT', 'KAZ', 'KEN', 'XCR', 'KIR', 'KSV', 'KUW', 'KYR', 'LAO', 'LAT', 'LEB', 'XLP', 'LES', 'XLL', 'LIB', 'LYA', 'LYW', 'LYE', 'LIT', 'XUL', 'XSL', 'LUX', 'MAC', 'MAD', 'MWI', 'MAL', 'MLV', 'MLI', 'MTA', 'MAR', 'MRA', 'MAU', 'MEX', 'MIC', 'XPQ', 'MOL', 'MON', 'MTG', 'MOR', 'MOZ', 'XPM', 'XMX', 'XAM', 'MUL', 'MYA', 'NAM', 'NAT', 'NEP', 'NET', 'NZ', 'NIC', 'NIR', 'NIG', 'XMN', 'XAN', 'NCY', 'KON', 'YEN', 'NOR', 'XLB', 'OMA', 'OSC', 'XPP', 'PAK', 'PAL', 'PA', 'PAN', 'PAP', 'PAR', 'XLO', 'PER', 'PHI', 'XID', 'XTP', 'XIP', 'POL', 'POR', 'XPC', 'XUI', 'QAT', 'RSS', 'ROM', 'XRR', 'XSR', 'RUS', 'RWA', 'SKN', 'SVG', 'SAM', 'SAU', 'SEN', 'SER', 'SEY', 'SIE', 'SIN', 'XLS', 'SLK', 'SLO', 'XSY', 'SOL', 'SOM', 'SA', 'XYS', 'KOS', 'SSD', 'VNS', 'YES', 'USR', 'SPA', 'XSP', 'SRI', 'SUD', 'SUR', 'SWE', 'SWI', 'SYR', 'XSX', 'TAI', 'TAJ', 'TAN', 'THA', 'ET', 'TOG', 'TON', 'TRI', 'TUN', 'TUR', 'TRK', 'TUV', 'UAE', 'UGA', 'XSI', 'UKR', 'XUR', 'XAU', 'UK', 'UNO', 'USA', 'XMU', 'XXX', 'XXU', 'XXR', 'XXS', 'URU', 'UZB', 'VAN', 'VEN', 'XVC', 'XFV', 'VN', 'SAH', 'YEM', 'YAR', 'YUG', 'ZAM', 'XZZ', 'ZIM']
    for i in codes:
        print(i)
        send(parse(i, key))
