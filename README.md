![Python](https://img.shields.io/badge/python-3.13-blue)
![CI](https://github.com/faith-akiror/calculator-app/actions/workflows/python-app.yml/badge.svg)
![Docker Publish](https://github.com/faith-akiror/calculator-app/actions/workflows/docker-publish.yml/badge.svg)
![Docker Pulls](https://img.shields.io/docker/pulls/faithakiror/calculator-app)
![Docker Image Size](https://img.shields.io/docker/image-size/faithakiror/calculator-app/latest)
![Last Commit](https://img.shields.io/github/last-commit/faith-akiror/calculator-app)

# Calculator App

A simple Python calculator application built with **Test-Driven Development (TDD)**, **Behavior-Driven Development (BDD)**, **GitHub Actions CI/CD**, **flake8 linting**, and **Docker containerization**.


## Features
- Add numbers
- Subtract numbers
- Multiply numbers
- Divide numbers
- Unit tested with **pytest**
- Behavior tested with **behave**
- Code style checked with **flake8**
- Dockerized for easy deployment
- Auto-published to Docker Hub using GitHub Actions


## Project Structure
```bash
calculator-app/
│
├── app/
│   └── calculator.py
│
├── tests/
│   └── test_calculator.py
│
├── features/
│   ├── calculator.feature
│   └── steps/
│       └── calculator_steps.py
│
├── .github/
│   └── workflows/
│       ├── python-app.yml
│       └── docker-publish.yml
│
├── Dockerfile
├── requirements.txt
└── README.md
```

## Installation
Clone the repository:

```bash
git clone https://github.com/faith-akiror/calculator-app.git
cd calculator-app
```

Create virtual environment:

```bash
python -m venv .venv
source .venv/Scripts/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run Tests
### TDD (pytest)
```bash
pytest
```

### BDD (behave)
```bash
behave
```

### Linting
```bash
flake8 .
```

---

## Docker
Build image:

```bash
docker build -t calculator-app .
```

Run container:

```bash
docker run --rm calculator-app
```

## Docker Hub
Image available at:

```bash
docker pull faithakiror/calculator-app:latest
```

## CI/CD
GitHub Actions automatically:

- Runs flake8
- Runs pytest
- Runs behave
- Builds Docker image
- Pushes Docker image to Docker Hub

on every push to `main`.

## Author
Built by **FAITH AKIROR**