Little Lemon Restaurant
=======================

This is a website for a restaurant using Django.
It has a landing page, an about page, a menu page, and a reservation page.
The website is responsive and can be viewed on mobile devices.

## Technologies

- Bootstrap
- CSS
- Django
- Docker
- HTML
- JavaScript
- Python
- SQLite

## Features

- Landing Page
- About
- Menu
- Reservation

## Installation

1. Clone the repository:
```bash
git clone https://github.com/DavidMiserak/Little-Lemon-BE.git
```

2. Change to the directory:
```bash
cd Little-Lemon-BE
```

3. Build the Docker image:
```bash
docker build -t little-lemon-restaurant .
```

4. Run the Docker container:
```bash
docker run -it --rm -p 8000:8000 little-lemon-restaurant
```

5. Open the browser and go to `http://localhost:8000`.

6. Enjoy!
