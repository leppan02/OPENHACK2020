
import requests, pandas, io
def getCSV(country_code='USA'):
    payload = {'import_or_export': 'export',
    'country_code': country_code,
    'low_year': 2016,
    'high_year': 2019,
    'summarize': 'country',
    'filetype': 'csv',
    'Action': 'Download'}
    return requests.post(url='https://armstrade.sipri.org/armstrade/html/export_values.php' , data=payload).content
    

if __name__ == '__main__':
    csv = getCSV()
    dataframe = pandas.read_csv(io.BytesIO(csv), names=['name', '2016', '2017', '2018', '2019', 'tot', 'nothing'])
    dataframe = dataframe.drop(columns=['tot', 'nothing']).fillna(0).drop([len(dataframe)-1,len(dataframe)-2, len(dataframe)-3]).drop(dataframe.index[:11]).reset_index(drop=True)
    print(dataframe)