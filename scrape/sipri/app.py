
import requests, pandas, io
def getCSV(country_code='SWE'):
    payload = {'import_or_export': 'export',
    'country_code': country_code,
    'low_year': 2018,
    'high_year': 2019,
    'summarize': 'country',
    'filetype': 'csv',
    'Action': 'Download'}
    return requests.post(url='https://armstrade.sipri.org/armstrade/html/export_values.php' , data=payload).content
    

if __name__ == '__main__':
    csv = getCSV()
    dataframe = pandas.read_csv(io.BytesIO(csv))
    print(len(dataframe))
    print(dataframe)