from flask import Flask,render_template,request
from weather import getcurrentweather
from waitress import serve
import os

app=Flask(__name__)
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
@app.route('/weather')
def get_weather():
    city=request.args.get('city')
    if not bool(city.strip()):
        city="Bangalore"
    weather_data=getcurrentweather(city)
    if not weather_data['cod']==200:
        return render_template('citynf.html')
   
    return render_template(
    "weather.html",
    title=weather_data["name"],
    description=weather_data["weather"][0]["description"],
    temp=f"{weather_data['main']['temp']:.1f}",
    feels_like=f"{weather_data['main']['feels_like']:.1f}",
    humidity=weather_data["main"]["humidity"],
    wind_speed=weather_data["wind"]["speed"],
    icon=weather_data["weather"][0]["icon"]
)


if __name__=="__main__":
    port = int(os.environ.get("PORT", 8000))
    serve(app, host="0.0.0.0", port=port)

   
