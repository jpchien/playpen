#!/usr/bin/env python3
"""Weather Checker - A feature-rich CLI weather application."""

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path

from api_client import WeatherClient
from config import Config
from display import WeatherDisplay


def main():
    """Main entry point for the weather application."""
    parser = argparse.ArgumentParser(
        description="Weather Checker - Get current weather and forecasts",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s London                    # Current weather for London
  %(prog)s "New York" --forecast     # 5-day forecast for New York
  %(prog)s Tokyo --units metric      # Weather in Celsius
  %(prog)s --add-favorite Paris      # Add Paris to favorites
  %(prog)s --list-favorites          # Show all favorite locations
        """
    )
    
    # Location arguments
    parser.add_argument(
        'location',
        nargs='?',
        help='City name or "latitude,longitude" coordinates'
    )
    
    # Weather options
    parser.add_argument(
        '-f', '--forecast',
        action='store_true',
        help='Show 5-day weather forecast'
    )
    parser.add_argument(
        '-d', '--detailed',
        action='store_true',
        help='Show detailed weather information'
    )
    parser.add_argument(
        '-u', '--units',
        choices=['metric', 'imperial', 'kelvin'],
        help='Temperature units (default: from config or metric)'
    )
    
    # Favorites management
    parser.add_argument(
        '--add-favorite',
        metavar='LOCATION',
        help='Add a location to favorites'
    )
    parser.add_argument(
        '--remove-favorite',
        metavar='LOCATION',
        help='Remove a location from favorites'
    )
    parser.add_argument(
        '--list-favorites',
        action='store_true',
        help='List all favorite locations'
    )
    parser.add_argument(
        '--favorites',
        action='store_true',
        help='Show weather for all favorite locations'
    )
    
    # Configuration
    parser.add_argument(
        '--setup',
        action='store_true',
        help='Setup or update API key and preferences'
    )
    parser.add_argument(
        '--no-cache',
        action='store_true',
        help='Bypass cache and fetch fresh data'
    )
    
    args = parser.parse_args()
    
    # Load configuration
    config = Config()
    
    # Handle setup
    if args.setup:
        config.interactive_setup()
        return 0
    
    # Check if API key is configured
    if not config.get('api_key'):
        print("❌ API key not configured!")
        print("\nPlease run: python3 weather.py --setup")
        print("\nYou can get a free API key from: https://openweathermap.org/api")
        return 1
    
    # Initialize clients
    units = args.units or config.get('units', 'metric')
    client = WeatherClient(config.get('api_key'), units=units)
    display = WeatherDisplay(units=units)
    
    # Handle favorites management
    if args.add_favorite:
        config.add_favorite(args.add_favorite)
        print(f"✅ Added '{args.add_favorite}' to favorites")
        return 0
    
    if args.remove_favorite:
        if config.remove_favorite(args.remove_favorite):
            print(f"✅ Removed '{args.remove_favorite}' from favorites")
        else:
            print(f"❌ '{args.remove_favorite}' not found in favorites")
        return 0
    
    if args.list_favorites:
        favorites = config.get('favorites', [])
        if favorites:
            print("⭐ Favorite Locations:")
            for i, fav in enumerate(favorites, 1):
                print(f"  {i}. {fav}")
        else:
            print("No favorite locations saved.")
            print("Add one with: python3 weather.py --add-favorite LOCATION")
        return 0
    
    # Handle weather for all favorites
    if args.favorites:
        favorites = config.get('favorites', [])
        if not favorites:
            print("No favorite locations saved.")
            return 0
        
        for location in favorites:
            try:
                weather_data = client.get_current_weather(location, use_cache=not args.no_cache)
                display.show_current_weather(weather_data, detailed=args.detailed)
                print()  # Blank line between locations
            except Exception as e:
                print(f"❌ Error fetching weather for {location}: {e}")
                print()
        return 0
    
    # Require location for weather queries
    if not args.location:
        parser.print_help()
        return 1
    
    try:
        # Fetch and display weather
        if args.forecast:
            forecast_data = client.get_forecast(args.location, use_cache=not args.no_cache)
            display.show_forecast(forecast_data)
        else:
            weather_data = client.get_current_weather(args.location, use_cache=not args.no_cache)
            display.show_current_weather(weather_data, detailed=args.detailed)
        
        return 0
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return 1


if __name__ == '__main__':
    sys.exit(main())
