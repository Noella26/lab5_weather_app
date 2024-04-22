from .models import weatherData
from django.shortcuts import render
import json
import urllib.request
def index(request):
    if request.method=='POST':
        city = request.POST['city']
        
    #     try:
    #     source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=1c40c5f593f9f1a303f617caf1da992a').read()
    #     list_of_data = json.loads(source)

    #     data = {
    #         "city": city,
    #         "country_code": str(list_of_data['sys']['country']),
    #         "coordinate": str(list_of_data['coord']['lon']) + ' ' + str(list_of_data['coord']['lat']),
    #         "temp": str(list_of_data['main']['temp']) + 'k',
    #         "pressure": str(list_of_data['main']['pressure']),
    #         "humidity": str(list_of_data['main']['humidity']),
    #     }

    # except HTTPError:
    #     print("No information available")
    #     data = None

    # print(data)

        source = urllib.request.urlopen( 
            'http://api.openweathermap.org/data/2.5/weather?q='+city+ '&appid=1c40c5f593f9f1a303f617caf1da992a').read()
        
        
        list_of_data = json.loads(source)
        #converting json to dictionary

        #data for variable list_of_data
        # print(list_of_data)

        data={
            'bdata': weatherData.objects.all().order_by('-Timestamp'),
            "city":city,
            "country_code": str(list_of_data['sys']['country']), 
            "coordinate": str(list_of_data['coord']['lon']) + ' '
                        + str(list_of_data['coord']['lat']), 
            "temp": str(list_of_data['main']['temp']) + 'K', 
            "pressure": str(list_of_data['main']['pressure']), 
            "humidity": str(list_of_data['main']['humidity']), 
        }
        wdata = weatherData()
        wdata.City= city
        wdata.Country = str(list_of_data['sys']['country'])
        wdata.Coordinate = str(list_of_data['coord']['lon']) + ' ' + str(list_of_data['coord']['lat'])
        wdata.Temperature = str(list_of_data['main']['temp']) + 'K'
        wdata.Pressure = str(list_of_data['main']['pressure'])
        wdata.Humidity = str(list_of_data['main']['humidity'])
        wdata.save() 

        
        print(data)

    else:
        data=None
    return render(request, "index.html", data)