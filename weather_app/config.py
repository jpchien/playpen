"""Configuration management for the weather application."""

import json
from pathlib import Path
from typing import Any, List, Optional


class Config:
    """Manages application configuration and favorites."""
    
    CONFIG_DIR = Path.home() / ".weather_app"
    CONFIG_FILE = CONFIG_DIR / "config.json"
    
    DEFAULT_CONFIG = {
        'api_key': '',
        'units': 'metric',
        'favorites': []
    }
    
    def __init__(self):
        """Initialize configuration manager."""
        self.CONFIG_DIR.mkdir(exist_ok=True)
        self.config = self._load_config()
    
    def _load_config(self) -> dict:
        """Load configuration from file."""
        if self.CONFIG_FILE.exists():
            try:
                with open(self.CONFIG_FILE, 'r') as f:
                    config = json.load(f)
                    # Merge with defaults to ensure all keys exist
                    return {**self.DEFAULT_CONFIG, **config}
            except (json.JSONDecodeError, IOError):
                return self.DEFAULT_CONFIG.copy()
        return self.DEFAULT_CONFIG.copy()
    
    def _save_config(self):
        """Save configuration to file."""
        with open(self.CONFIG_FILE, 'w') as f:
            json.dump(self.config, f, indent=2)
    
    def get(self, key: str, default: Any = None) -> Any:
        """
        Get a configuration value.
        
        Args:
            key: Configuration key
            default: Default value if key doesn't exist
            
        Returns:
            Configuration value
        """
        return self.config.get(key, default)
    
    def set(self, key: str, value: Any):
        """
        Set a configuration value.
        
        Args:
            key: Configuration key
            value: Configuration value
        """
        self.config[key] = value
        self._save_config()
    
    def add_favorite(self, location: str):
        """
        Add a location to favorites.
        
        Args:
            location: Location name to add
        """
        favorites = self.config.get('favorites', [])
        if location not in favorites:
            favorites.append(location)
            self.set('favorites', favorites)
    
    def remove_favorite(self, location: str) -> bool:
        """
        Remove a location from favorites.
        
        Args:
            location: Location name to remove
            
        Returns:
            True if removed, False if not found
        """
        favorites = self.config.get('favorites', [])
        if location in favorites:
            favorites.remove(location)
            self.set('favorites', favorites)
            return True
        return False
    
    def interactive_setup(self):
        """Run interactive setup to configure the application."""
        print("=" * 60)
        print("Weather App Setup")
        print("=" * 60)
        print("\nGet your free API key from:")
        print("https://openweathermap.org/api")
        print("")
        
        # API Key
        current_key = self.get('api_key', '')
        if current_key:
            print(f"Current API key: {current_key[:8]}...{current_key[-4:]}")
            print("(Press Enter to keep current key)")
        
        api_key = input("Enter your OpenWeatherMap API key: ").strip()
        if api_key:
            self.set('api_key', api_key)
            print("✅ API key saved!")
        elif current_key:
            print("✅ Keeping existing API key")
        else:
            print("⚠️  No API key configured!")
        
        # Units
        print("\nTemperature units:")
        print("  1. Metric (Celsius)")
        print("  2. Imperial (Fahrenheit)")
        print("  3. Kelvin")
        
        current_units = self.get('units', 'metric')
        print(f"Current: {current_units} (Press Enter to keep)")
        
        units_choice = input("Choose (1/2/3): ").strip()
        units_map = {'1': 'metric', '2': 'imperial', '3': 'kelvin'}
        if units_choice in units_map:
            self.set('units', units_map[units_choice])
            print(f"✅ Units set to: {units_map[units_choice]}")
        else:
            print(f"✅ Keeping {current_units}")
        
        # Favorites
        print("\nWould you like to add favorite locations?")
        while True:
            location = input("Enter location (or press Enter to finish): ").strip()
            if not location:
                break
            self.add_favorite(location)
            print(f"✅ Added '{location}' to favorites")
        
        print("\n" + "=" * 60)
        print("Setup complete! 🎉")
        print("=" * 60)
        print("\nTry these commands:")
        print("  python3 weather.py London")
        print("  python3 weather.py --favorites")
        print("  python3 weather.py Tokyo --forecast")
