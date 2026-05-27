# Weather Checker 🌤️

![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Code Style](https://img.shields.io/badge/code%20style-black-black)
![Maintenance](https://img.shields.io/badge/maintained-yes-brightgreen)

A feature-rich command-line weather application built with Python.

## 📋 Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Command Reference](#command-reference)
- [Configuration](#configuration)
- [Cache](#cache)
- [Examples](#examples)
- [Demo](#demo)
- [Requirements](#requirements)
- [API Information](#api-information)
- [Contributing](#contributing)
- [License](#license)

## Features

- ☀️ **Current Weather** - Get real-time weather for any location
- 📅 **5-Day Forecast** - View detailed weather forecasts
- ⭐ **Favorites** - Save and quickly check your favorite locations
- 🌡️ **Multiple Units** - Choose between Celsius, Fahrenheit, or Kelvin
- 📊 **Detailed Info** - Humidity, wind speed, pressure, visibility, and more
- 💾 **Smart Caching** - Reduces API calls and improves performance
- 🎨 **Beautiful Display** - Colorful CLI with weather emojis

## Installation

1. **Get an API Key** (free):
   - Visit [OpenWeatherMap](https://openweathermap.org/api)
   - Sign up for a free account
   - Generate an API key

2. **Run Setup**:
   ```bash
   python3 weather.py --setup
   ```
   
   Enter your API key and preferences when prompted.

## Usage

### Current Weather
```bash
# Basic weather check
python3 weather.py London

# Detailed information
python3 weather.py "New York" --detailed

# Use different units
python3 weather.py Tokyo --units imperial
```

### Forecast
```bash
# 5-day forecast
python3 weather.py Paris --forecast

# Forecast with specific units
python3 weather.py Berlin --forecast --units metric
```

### Favorites
```bash
# Add favorite locations
python3 weather.py --add-favorite "San Francisco"
python3 weather.py --add-favorite Tokyo

# List all favorites
python3 weather.py --list-favorites

# Check weather for all favorites
python3 weather.py --favorites

# Remove a favorite
python3 weather.py --remove-favorite Tokyo
```

### Coordinates
```bash
# Use latitude,longitude
python3 weather.py "51.5074,-0.1278"  # London coordinates
```

### Other Options
```bash
# Bypass cache for fresh data
python3 weather.py London --no-cache

# Update configuration
python3 weather.py --setup
```

## Command Reference

```
positional arguments:
  location              City name or "latitude,longitude" coordinates

optional arguments:
  -h, --help            Show help message
  -f, --forecast        Show 5-day weather forecast
  -d, --detailed        Show detailed weather information
  -u, --units {metric,imperial,kelvin}
                        Temperature units
  --add-favorite LOCATION
                        Add a location to favorites
  --remove-favorite LOCATION
                        Remove a location from favorites
  --list-favorites      List all favorite locations
  --favorites           Show weather for all favorite locations
  --setup               Setup or update API key and preferences
  --no-cache            Bypass cache and fetch fresh data
```

## Configuration

Configuration is stored in `~/.weather_app/config.json`:

```json
{
  "api_key": "your_api_key_here",
  "units": "metric",
  "favorites": [
    "London",
    "New York",
    "Tokyo"
  ]
}
```

## Cache

Weather data is cached for 10 minutes in `~/.weather_app_cache/` to:
- Reduce API calls
- Improve response time
- Respect API rate limits

Use `--no-cache` to fetch fresh data.

## Examples

```bash
# Morning weather routine - check all favorites
python3 weather.py --favorites

# Planning a trip - get detailed forecast
python3 weather.py "Los Angeles" --forecast --detailed

# Quick temperature check
python3 weather.py Seattle

# Check weather at specific coordinates
python3 weather.py "35.6762,139.6503"  # Tokyo coordinates
```

## 🎬 Demo

### Current Weather
```
============================================================
📍 London, GB
============================================================

☁️  Overcast Clouds
🌡️  Temperature: 59.7°F
🤚  Feels like: 58.3°F
💧  Humidity: 76%
💨  Wind Speed: 8.05 mph
===🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Make your changes** and test thoroughly
4. **Commit your changes**: `git commit -m 'Add amazing feature'`
5. **Push to the branch**: `git push origin feature/amazing-feature`
6. **Open a Pull Request**

### Ideas for Contributions

- 🎨 Add color output with ANSI codes
- 📊 Add weather graphs and charts
- 🌍 Support for more weather APIs
- 🔔 Add weather alerts and notifications
- 📱 Add desktop notifications
- 🌙 Add moon phase information
- 🏙️ Add air quality index
- 🧪 Add unit tests

See [CONTRIBUTING.md](CONTRIBUTING.md) for more details.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Weather data provided by [OpenWeatherMap](https://openweathermap.org/)
- Built with ❤️ using Python's standard library
- Inspired by the need for a simple, fast weather CLI tool

---

**⭐ If you find this useful, please star the repository!**
### 5-Day Forecast
```
============================================================
📅 5-Day Forecast for Tokyo, JP
============================================================

☀️  Monday, May 27
   Clear
   Low: 64.4°F  |  High: 75.2°F

🌧️  Tuesday, May 28
   Rain
   Low: 61.5°F  |  High: 68.9°F
...
```

> 💡 **Tip**: Add a screenshot or animated GIF here showing the actual output!

## Requirements

- Python 3.6+
- Internet connection
- OpenWeatherMap API key (free tier available)

## API Information

This app uses the [OpenWeatherMap API](https://openweathermap.org/api):
- **Free tier**: 60 calls/minute, 1,000,000 calls/month
- **Current Weather**: Real-time weather data
- **5-Day Forecast**: Weather predictions with 3-hour intervals

## License

MIT License - feel free to use and modify!
