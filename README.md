# Django-Weather-app-

## Features

- Real-time weather data for major Pakistani cities
- Clean and responsive user interface
- Displays temperature, humidity, wind speed, and weather conditions
- Uses OpenWeatherMap API for accurate weather data
- Mobile-friendly design

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd weatherapp
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory with your OpenWeatherMap API key:
```
OPENWEATHER_API_KEY=your_api_key_here
DJANGO_SECRET_KEY=your_secret_key_here
```

5. Run migrations:
```bash
python manage.py migrate
```

6. Start the development server:
```bash
python manage.py runserver
```

## Technologies Used

- Python 3.x
- Django 4.2.7
- OpenWeatherMap API
- HTML/CSS
- SQLite3

## Project Structure

```
weatherapp/
├── weather/                # Main app directory
│   ├── templates/         # HTML templates
│   ├── static/           # Static files (CSS, images)
│   ├── urls.py           # URL configurations
│   └── views.py          # View functions
├── weatherapp/           # Project settings
├── static/              # Global static files
├── manage.py
└── requirements.txt
```

## Contributing

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## License

This project is open-sourced under the MIT license.

## Acknowledgments

- Weather data provided by [OpenWeatherMap](https://openweathermap.org/)
- Built with [Django](https://www.djangoproject.com/)
