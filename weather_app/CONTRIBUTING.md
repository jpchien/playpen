# Contributing to Weather Checker 🌤️

First off, thank you for considering contributing to Weather Checker! It's people like you that make this tool better for everyone.

## 🎯 Ways to Contribute

### 1. Report Bugs 🐛

Found a bug? Please create an issue with:
- **Clear title**: Describe the bug in a few words
- **Steps to reproduce**: How can we trigger the bug?
- **Expected behavior**: What should happen?
- **Actual behavior**: What actually happens?
- **Environment**: Python version, OS, etc.
- **Screenshots**: If applicable

### 2. Suggest Features 💡

Have an idea? Create an issue with:
- **Feature description**: What would you like to see?
- **Use case**: Why is this useful?
- **Possible implementation**: How might it work?

### 3. Submit Code 🚀

#### Getting Started

1. **Fork the repository**
   ```bash
   # Click the "Fork" button on GitHub
   ```

2. **Clone your fork**
   ```bash
   git clone https://github.com/YOUR_USERNAME/playpen.git
   cd playpen/weather_app
   ```

3. **Create a branch**
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/bug-description
   ```

#### Development Guidelines

**Code Style**
- Follow PEP 8 guidelines
- Use type hints where appropriate
- Write docstrings for functions and classes
- Keep functions focused and small

**Example:**
```python
def get_weather(location: str) -> Dict:
    """
    Get current weather for a location.
    
    Args:
        location: City name or coordinates
        
    Returns:
        Weather data dictionary
    """
    # Implementation
```

**Testing Your Changes**
```bash
# Test the main functionality
python3 weather.py --setup
python3 weather.py London
python3 weather.py Tokyo --forecast
python3 weather.py --favorites

# Test error handling
python3 weather.py "InvalidCityName123"
python3 weather.py --no-cache "New York"
```

**Commit Messages**
Write clear, concise commit messages:
```bash
# Good ✅
git commit -m "Add support for wind gust in detailed view"
git commit -m "Fix cache expiration bug"
git commit -m "Update README with new examples"

# Bad ❌
git commit -m "fixed stuff"
git commit -m "updates"
```

#### Submitting Your Changes

1. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

2. **Open a Pull Request**
   - Go to the original repository
   - Click "New Pull Request"
   - Select your fork and branch
   - Fill out the PR template

3. **PR Checklist**
   - [ ] Code follows project style guidelines
   - [ ] All functions have docstrings
   - [ ] Changes are tested locally
   - [ ] README updated if needed
   - [ ] No sensitive data (API keys) in code

### 4. Improve Documentation 📝

Documentation improvements are always welcome:
- Fix typos or unclear instructions
- Add examples
- Improve code comments
- Translate documentation

## 🎨 Feature Ideas

Here are some features we'd love to see:

### Easy
- [ ] Add colored output with ANSI codes
- [ ] Support for more temperature units (Rankine?)
- [ ] Add weather condition icons in terminal
- [ ] Export weather data to JSON/CSV
- [ ] Add quiet mode (minimal output)

### Medium
- [ ] Desktop notifications for severe weather
- [ ] Weather comparison between multiple cities
- [ ] Historical weather data
- [ ] Customizable output format templates
- [ ] Interactive mode (TUI)

### Advanced
- [ ] Unit tests with pytest
- [ ] Support for multiple weather APIs (Dark Sky, WeatherAPI, etc.)
- [ ] Weather maps and visualizations
- [ ] Air quality index integration
- [ ] Machine learning weather predictions

## 🐍 Python Guidelines

- **Minimum version**: Python 3.6+
- **Use standard library** when possible
- **No external dependencies** unless absolutely necessary
- **Type hints** for better code clarity
- **Error handling** with informative messages

## 📜 Code of Conduct

### Our Standards

- **Be respectful** and considerate
- **Be collaborative** and constructive
- **Accept constructive criticism** gracefully
- **Focus on what's best** for the community

### Unacceptable Behavior

- Harassment, discrimination, or trolling
- Publishing others' private information
- Inappropriate or unwelcome attention
- Any conduct inappropriate in a professional setting

## ❓ Questions?

Feel free to:
- Open an issue with the "question" label
- Reach out to maintainers
- Join discussions in existing issues

## 🎉 Thank You!

Every contribution, no matter how small, makes a difference. Thank you for taking the time to contribute!

---

**Happy Coding!** 🌈
