
import requests
def getCSV(country_code='USA'):
    payload = {'import_or_export': 'export',
    'country_code': country_code,
    'low_year': 2000,
    'high_year': 2019,
    'summarize': 'country',
    'filetype': 'csv',
    'Action': 'Download'}
    return requests.post(url='https://armstrade.sipri.org/armstrade/html/export_values.php' , data=payload).content.decode('utf8')
    

if __name__ == '__main__':
    csv = getCSV()
    dataframe = [i.split(',') for i in csv.split('\n')[11:-3]]
    for i in dataframe:
        country = i[0]
        data = i[1:]
        year = 2000
        for j in data:
            if len(j):
                package = {'country_from':'USA','country_to':country, 'amount': j, 'trade_start':"{}-01-01".format(year), 'trade_end': "{}-01-01".format(year+1)}
                print(package)
            year+=1