"""Weather API client for OpenWeatherMap."""

import json
import time
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, Optional
from urllib import request, parse, error


class WeatherClient:
    """Client for fetching weather data from OpenWeatherMap API."""
    
    BASE_URL = "https://api.openweathermap.org/data/2.5"
    CACHE_DIR = Path.home() / ".weather_app_cache"
    CACHE_DURATION = 600  # 10 minutes
    
    def __init__(self, api_key: str, units: str = 'metric'):
        """
        Initialize the weather client.
        
        Args:
            api_key: OpenWeatherMap API key
            units: Temperature units ('metric', 'imperial', 'kelvin')
        """
        self.api_key = api_key
        self.units = units
        self.CACHE_DIR.mkdir(exist_ok=True)
    
    def _make_request(self, endpoint: str, params: Dict) -> Dict:
        """
        Make an API request to OpenWeatherMap.
        
        Args:
            endpoint: API endpoint (e.g., 'weather', 'forecast')
            params: Query parameters
            
        Returns:
            Parsed JSON response
            
        Raises:
            Exception: If the API request fails
        """
        params['appid'] = self.api_key
        params['units'] = self.units
        
        query_string = parse.urlencode(params)
        url = f"{self.BASE_URL}/{endpoint}?{query_string}"
        
        try:
            with request.urlopen(url, timeout=10) as response:
                data = json.loads(response.read().decode())
                return data
        except error.HTTPError as e:
            if e.code == 401:
                raise Exception("Invalid API key. Please check your configuration.")
            elif e.code == 404:
                raise Exception(f"Location not found: {params.get('q', 'Unknown')}")
            else:
                raise Exception(f"API error: {e.code} - {e.reason}")
        except error.URLError as e:
            raise Exception(f"Network error: {e.reason}")
        except Exception as e:
            raise Exception(f"Request failed: {str(e)}")
    
    def _get_cache_path(self, cache_key: str) -> Path:
        """Get the cache file path for a given key."""
        return self.CACHE_DIR / f"{cache_key}.json"
    
    def _read_cache(self, cache_key: str) -> Optional[Dict]:
        """
        Read data from cache if it exists and is still valid.
        
        Args:
            cache_key: Unique identifier for the cached data
            
        Returns:
            Cached data if valid, None otherwise
        """
        cache_path = self._get_cache_path(cache_key)
        
        if not cache_path.exists():
            return None
        
        try:
            with open(cache_path, 'r') as f:
                cached = json.load(f)
            
            # Check if cache is still valid
            cache_time = datetime.fromisoformat(cached['timestamp'])
            if datetime.now() - cache_time < timedelta(seconds=self.CACHE_DURATION):
                return cached['data']
        except (json.JSONDecodeError, KeyError, ValueError):
            pass
        
        return None
    
    def _write_cache(self, cache_key: str, data: Dict):
        """
        Write data to cache.
        
        Args:
            cache_key: Unique identifier for the cached data
            data: Data to cache
        """
        cache_path = self._get_cache_path(cache_key)
        
        cached = {
            'timestamp': datetime.now().isoformat(),
            'data': data
        }
        
        with open(cache_path, 'w') as f:
            json.dump(cached, f)
    
    def get_current_weather(self, location: str, use_cache: bool = True) -> Dict:
        """
        Get current weather for a location.
        
        Args:
            location: City name or "lat,lon" coordinates
            use_cache: Whether to use cached data if available
            
        Returns:
            Weather data dictionary
        """
        cache_key = f"current_{location}_{self.units}"
        
        if use_cache:
            cached_data = self._read_cache(cache_key)
            if cached_data:
                return cached_data
        
        # Parse location
        if ',' in location and all(part.replace('.', '').replace('-', '').isdigit() 
                                   for part in location.split(',')):
            lat, lon = location.split(',')
            params = {'lat': lat.strip(), 'lon': lon.strip()}
        else:
            params = {'q': location}
        
        data = self._make_request('weather', params)
        
        if use_cache:
            self._write_cache(cache_key, data)
        
        return data
    
    def get_forecast(self, location: str, use_cache: bool = True) -> Dict:
        """
        Get 5-day weather forecast for a location.
        
        Args:
            location: City name or "lat,lon" coordinates
            use_cache: Whether to use cached data if available
            
        Returns:
            Forecast data dictionary
        """
        cache_key = f"forecast_{location}_{self.units}"
        
        if use_cache:
            cached_data = self._read_cache(cache_key)
            if cached_data:
                return cached_data
        
        # Parse location
        if ',' in location and all(part.replace('.', '').replace('-', '').isdigit() 
                                   for part in location.split(',')):
            lat, lon = location.split(',')
            params = {'lat': lat.strip(), 'lon': lon.strip()}
        else:
            params = {'q': location}
        
        data = self._make_request('forecast', params)
        
        if use_cache:
            self._write_cache(cache_key, data)
        
        return data
