# Changelog

All notable changes to the Weather Checker project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2026-05-27

### Added
- Initial release of Weather Checker
- Current weather data for any location
- 5-day weather forecast with 3-hour intervals
- Favorite locations management
- Multiple temperature units (Celsius, Fahrenheit, Kelvin)
- Detailed weather information (humidity, wind, pressure, visibility)
- Smart caching system (10-minute cache duration)
- Interactive setup wizard
- Beautiful CLI output with weather emojis
- Support for both city names and coordinates
- No external dependencies (pure Python standard library)
- Configuration stored in `~/.weather_app/`
- Cache stored in `~/.weather_app_cache/`
- Comprehensive README with examples
- MIT License
- Contributing guidelines

### Features in Detail
- **CLI Arguments**: 
  - Location-based queries
  - Forecast mode
  - Detailed view
  - Unit selection
  - Favorites management
  - Cache bypass option
- **Weather Data**:
  - Temperature (current, feels like, min, max)
  - Humidity
  - Wind speed and direction
  - Cloudiness
  - Visibility
  - Pressure
  - Sunrise/Sunset times
- **Error Handling**:
  - Invalid API key detection
  - Location not found handling
  - Network error handling
  - Graceful degradation

## [Unreleased]

### Planned Features
- Colored terminal output
- Desktop notifications
- Unit tests
- Support for additional weather APIs
- Weather alerts
- Air quality index
- Historical weather data
- Weather comparison tool

---

[0.1.0]: https://github.com/jpchien/playpen/releases/tag/v0.1.0
