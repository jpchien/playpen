"""Display module for formatting and printing weather data."""

from datetime import datetime
from typing import Dict, List


class WeatherDisplay:
    """Handles formatting and display of weather data."""
    
    # Weather emoji mapping
    WEATHER_EMOJI = {
        'Clear': '☀️',
        'Clouds': '☁️',
        'Rain': '🌧️',
        'Drizzle': '🌦️',
        'Thunderstorm': '⛈️',
        'Snow': '❄️',
        'Mist': '🌫️',
        'Fog': '🌫️',
        'Haze': '🌫️',
        'Smoke': '🌫️',
        'Dust': '🌫️',
        'Sand': '🌫️',
        'Ash': '🌋',
        'Squall': '💨',
        'Tornado': '🌪️',
    }
    
    def __init__(self, units: str = 'metric'):
        """
        Initialize the display handler.
        
        Args:
            units: Temperature units ('metric', 'imperial', 'kelvin')
        """
        self.units = units
        self.temp_symbol = self._get_temp_symbol()
    
    def _get_temp_symbol(self) -> str:
        """Get the temperature symbol based on units."""
        return {
            'metric': '°C',
            'imperial': '°F',
            'kelvin': 'K'
        }.get(self.units, '°C')
    
    def _get_weather_emoji(self, condition: str) -> str:
        """Get emoji for weather condition."""
        return self.WEATHER_EMOJI.get(condition, '🌍')
    
    def _format_timestamp(self, timestamp: int) -> str:
        """Format Unix timestamp to readable string."""
        return datetime.fromtimestamp(timestamp).strftime('%I:%M %p')
    
    def _format_date(self, timestamp: int) -> str:
        """Format Unix timestamp to readable date."""
        return datetime.fromtimestamp(timestamp).strftime('%A, %B %d')
    
    def show_current_weather(self, data: Dict, detailed: bool = False):
        """
        Display current weather information.
        
        Args:
            data: Weather data from API
            detailed: Whether to show detailed information
        """
        # Extract data
        location = data['name']
        country = data['sys']['country']
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        condition = data['weather'][0]['main']
        description = data['weather'][0]['description'].title()
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        
        emoji = self._get_weather_emoji(condition)
        
        # Header
        print("=" * 60)
        print(f"📍 {location}, {country}")
        print("=" * 60)
        
        # Main weather info
        print(f"\n{emoji}  {description}")
        print(f"🌡️  Temperature: {temp:.1f}{self.temp_symbol}")
        print(f"🤚  Feels like: {feels_like:.1f}{self.temp_symbol}")
        print(f"💧  Humidity: {humidity}%")
        print(f"💨  Wind Speed: {wind_speed} {'m/s' if self.units == 'metric' else 'mph'}")
        
        if detailed:
            # Additional details
            print("\n" + "-" * 60)
            print("DETAILED INFORMATION")
            print("-" * 60)
            
            temp_min = data['main']['temp_min']
            temp_max = data['main']['temp_max']
            pressure = data['main']['pressure']
            visibility = data.get('visibility', 0) / 1000  # Convert to km
            clouds = data['clouds']['all']
            
            print(f"🔽  Min Temperature: {temp_min:.1f}{self.temp_symbol}")
            print(f"🔼  Max Temperature: {temp_max:.1f}{self.temp_symbol}")
            print(f"🎚️  Pressure: {pressure} hPa")
            print(f"👁️  Visibility: {visibility:.1f} km")
            print(f"☁️  Cloudiness: {clouds}%")
            
            if 'wind' in data:
                if 'deg' in data['wind']:
                    wind_deg = data['wind']['deg']
                    wind_dir = self._get_wind_direction(wind_deg)
                    print(f"🧭  Wind Direction: {wind_dir} ({wind_deg}°)")
                
                if 'gust' in data['wind']:
                    print(f"💨  Wind Gust: {data['wind']['gust']} {'m/s' if self.units == 'metric' else 'mph'}")
            
            # Sunrise/Sunset
            sunrise = self._format_timestamp(data['sys']['sunrise'])
            sunset = self._format_timestamp(data['sys']['sunset'])
            print(f"🌅  Sunrise: {sunrise}")
            print(f"🌇  Sunset: {sunset}")
        
        print("=" * 60)
    
    def show_forecast(self, data: Dict):
        """
        Display 5-day weather forecast.
        
        Args:
            data: Forecast data from API
        """
        location = data['city']['name']
        country = data['city']['country']
        
        # Header
        print("=" * 60)
        print(f"📅 5-Day Forecast for {location}, {country}")
        print("=" * 60)
        
        # Group forecast by day
        forecast_by_day = {}
        for item in data['list']:
            date = datetime.fromtimestamp(item['dt']).date()
            if date not in forecast_by_day:
                forecast_by_day[date] = []
            forecast_by_day[date].append(item)
        
        # Display each day
        for date, forecasts in list(forecast_by_day.items())[:5]:
            day_name = date.strftime('%A, %B %d')
            
            # Calculate daily stats
            temps = [f['main']['temp'] for f in forecasts]
            conditions = [f['weather'][0]['main'] for f in forecasts]
            
            temp_min = min(temps)
            temp_max = max(temps)
            
            # Most common condition
            condition = max(set(conditions), key=conditions.count)
            emoji = self._get_weather_emoji(condition)
            
            print(f"\n{emoji}  {day_name}")
            print(f"   {condition}")
            print(f"   Low: {temp_min:.1f}{self.temp_symbol}  |  High: {temp_max:.1f}{self.temp_symbol}")
            
            # Show 3-hour intervals for today and tomorrow
            if len(forecast_by_day) <= 2:
                print("   Hourly:")
                for forecast in forecasts[:4]:  # Show first 4 intervals
                    time = datetime.fromtimestamp(forecast['dt']).strftime('%I:%M %p')
                    temp = forecast['main']['temp']
                    desc = forecast['weather'][0]['description']
                    print(f"      {time}: {temp:.1f}{self.temp_symbol} - {desc}")
        
        print("\n" + "=" * 60)
    
    def _get_wind_direction(self, degrees: float) -> str:
        """Convert wind degrees to cardinal direction."""
        directions = ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE',
                     'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW']
        idx = int((degrees + 11.25) / 22.5) % 16
        return directions[idx]
