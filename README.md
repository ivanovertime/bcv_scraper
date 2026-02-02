# BCV Exchange Scraper 

## Table of Contents
- [BCV Exchange Scraper](#bcv-exchange-scraper)
  - [Table of Contents](#table-of-contents)
  - [About ](#about-)
  - [Getting Started ](#getting-started-)
  - [Requirements](#requirements)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Docker](#docker)
  - [Deployment ](#deployment-)
  - [Contributing](#contributing)


## About <a name = "about"></a>

This is a simple web scraper built in Python with FastAPI. It scrapes data from the oficial website [Banco Central de Venezuela](https://bcv.org.ve/) and returns it in JSON format.

## Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

## Requirements

- Python 3.12 or higher
- FastAPI
- Requests
- BeautifulSoup4
- Docker

## Installation

1. Clone the repository.
2. Install the required packages using `pip install -r requirements.txt`.
3. Run the application using `python run.py`.

## Usage

1. Send a GET request to `http://localhost:8000/get-data`.
2. The response will be in JSON format.

## Docker

To run the application in a Docker container, follow these steps:

1. Build the Docker image using `docker build -t bcv-scraper .`.
2. Run the Docker container using `docker run -p 8000:8000 bcv-scraper`.

## Deployment <a name = "deployment"></a>
Keep in mind that every call to the endpoint executes a scraping to the website. You need to consider storage solutions to avoid problems with the institution and yourself. 

If you have the means, I recommend [crawlab](https://github.com/crawlab-team/crawlab). You can create a scrapy spider with the selectors in `scraper.py`, set the cron task and forget about it (Well, mostly). 

## Contributing

Contributions are welcome! Please feel free to submit a pull request.
I hope this helps! Let me know if you have any questions.
