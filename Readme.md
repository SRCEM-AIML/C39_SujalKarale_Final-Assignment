# 🛠️ Web Applications: Flask + Django with Docker Compose

This project contains two web applications:
- A **Flask** app with form input and validation
- A **Django** app with a product list, admin panel, and CRUD operations

Both applications are containerized using **Docker** and managed via **Docker Compose**.

---

## 🚀 How to Run This Project on Localhost

### ✅ Prerequisites

Before you begin, make sure you have:

- [Docker](https://www.docker.com/products/docker-desktop) installed
- [Docker Compose](https://docs.docker.com/compose/install/) installed

---

### 🛆 Step 1: Clone the Repository

```bash
git clone https://github.com/SRCEM-AIML/C39_SujalKarale_Final-Assignment.git
cd C39_SujalKarale_Final-Assignment
```

> Or copy the project files into a folder on your machine.

---

### 🐳 Step 2: Build and Run Containers

Navigate to the root `project/` directory and run:

```bash
docker-compose up --build
```

This will:
- Build Docker images for both Flask and Django apps
- Run the containers and expose them to your localhost

---

### 🌐 Step 3: Open the Applications in Browser

- **Flask App**: [http://localhost:5000](http://localhost:5000)
- **Django App**: [http://localhost:8000](http://localhost:8000)

---

### ⚙️ Step 4: Setup Django Admin (First Time Only)

In a separate terminal:

```bash
docker-compose exec django-app python manage.py migrate
docker-compose exec django-app python manage.py createsuperuser
```

Then access the Django admin panel at:

- [http://localhost:8000/admin](http://localhost:8000/admin)

Login using the superuser credentials you just created.

---

### 🔝 To Stop the Apps

Press `CTRL+C` in the terminal running Docker Compose, or run:

```bash
docker-compose down
```

---

## 📁 Directory Overview

```
project/
├── flask_app/
│   ├── app.py
│   ├── templates/
│   ├── Dockerfile
│   └── requirements.txt
├── django_app/
│   ├── manage.py
│   ├── ecommerce/
│   ├── store/
│   ├── Dockerfile
│   └── requirements.txt
├── docker-compose.yml
└── README.md
```

---

## ❓Troubleshooting

- If you see `ERR_EMPTY_RESPONSE` or a blank page, ensure:
  - No other service is using ports 5000 or 8000.
  - Docker is running.
  - Containers are up: `docker-compose ps`

- Restart containers:
  ```bash
  docker-compose down
  docker-compose up --build
  ```

---

Happy coding! ✨

