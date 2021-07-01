from django.shortcuts import render
import requests
import json

def home(request):
    if request.method == "POST":
        if request.POST.get("zipcode").isdigit():
            zipcode = request.POST.get("zipcode")
        else:
            pass
    else:
        zipcode = 10001 #defult NY city 
    try:
        data = requests.get(f"https://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode={zipcode}&date=2021-07-01&distance=25&API_KEY=78AEA765-0785-4F86-83C5-BB4BA9BEBDDA")
        weather_data = json.loads(data.content.decode())[0]
        if weather_data["Category"]["Name"] == "Good":
            category_description = "Air quality is satisfactory, and air pollution poses little or no risk."
            category_color = "good"
            
        elif weather_data["Category"]["Name"] == "Moderate":
            category_description = "Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution."
            category_color = "moderate"
            
        elif weather_data["Category"]["Name"] == "Unhealthy for Sensitive Groups":
            category_description = "Members of sensitive groups may experience health effects. The general public is less likely to be affected."
            category_color = "usg"
            
        elif weather_data["Category"]["Name"] == "Unhealthy":
            category_description = "Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects."
            category_color = "unhealthy"
            
        elif weather_data["Category"]["Name"] == "Very Unhealthy":
            category_description = "Health alert: The risk of health effects is increased for everyone."
            category_color = "veryunhealthy"
            
        elif weather_data["Category"]["Name"] == "Hazardous":
            category_description = "Health warning of emergency conditions: everyone is more likely to be affected."
            category_color = "hazardous"
            
        context = {"data":weather_data,"category_color": category_color,"category_description" : category_description}
    except Exception as e:
        context = {"error" : "Unable to connect to API"}
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html',{})