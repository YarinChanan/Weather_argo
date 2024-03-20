import requests
from datetime import date, timedelta

def json_creation(city):
    key = "NG5SCKUHVM4Y9MKGKD8M37SPU"
    days = 7
    start_date = date.today()
    end_date = start_date + timedelta(days=7)
    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}/{start_date}/{end_date}?unitGroup=metric&key={key}"


    list_all_days=[]
    response = requests.get(url).json()

    for i in range(days): 
        dict_day = {}
        dict_day['address']=response['address']
        dict_day['resolvedAddress']=response['resolvedAddress']
        dict_day['date']=response['days'][i]['datetime']
        dict_day['temp']=response['days'][i]['temp']
        dict_day['day_temp']=response['days'][i]['tempmax']
        dict_day['night_temp']=response['days'][i]['tempmin']
        dict_day['humidity']=response['days'][i]['humidity']
        list_all_days.append(dict_day)
        
    return list_all_days

if __name__=="__main__":
    json_creation("Tel aviv")


