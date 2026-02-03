# BCV Exchange Scraper

## Table of Contents
- [About](#about)
- [Getting Started](#getting-started)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [API Reference](#api-reference)
- [Response Schema](#response-schema)
- [Running Locally](#running-locally)
- [Docker](#docker)
- [Deployment Notes](#deployment-notes)
- [Caveats & Operational Notes](#caveats--operational-notes)
- [Contributing](#contributing)
- [License](#license)

## About

This is a small FastAPI service that scrapes exchange rates from the official website of [Banco Central de Venezuela](https://bcv.org.ve/) and returns them as JSON.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [Deployment Notes](#deployment-notes) for live usage considerations.

## Requirements

- Python 3.12 or higher
- FastAPI
- Requests-HTML (uses lxml under the hood)
- Uvicorn
- Docker (optional)

## Installation

1. Clone the repository.
2. Install the required packages using `pip install -r requirements.txt`.
3. Run the application using `python run.py`.

## Usage

1. Start the server.
2. Send a GET request to `http://localhost:8000/get-data`.
3. The response will be in JSON format.

## API Reference

- `GET /`
	- Returns a short message with the main endpoint.
- `GET /get-data`
	- Scrapes BCV and returns exchange rates as JSON.

## Response Schema

The response is a JSON object with numeric exchange rates and metadata:

- `usd`: number
- `euro`: number
- `yuan`: number
- `lira`: number
- `rublo`: number
- `scrap_date`: string (local timestamp, hour precision)
- `valid_date`: array of strings (as provided by the site)

Example response:

```json
{
	"usd": 36.12,
	"euro": 39.38,
	"yuan": 5.01,
	"lira": 1.10,
	"rublo": 0.41,
	"scrap_date": "2026-02-02 15",
	"valid_date": ["Lunes", " 02 Febrero  2026"]
}
```

## Running Locally

The default entrypoint is:

```bash
python run.py
```

For local development with auto-reload, run Uvicorn directly:

```bash
uvicorn main:app --reload
```

You can also configure runtime settings with environment variables:

- `HOST` (default: `0.0.0.0`)
- `PORT` (default: `8000`)
- `RELOAD` (default: `false`)
- `WORKERS` (default: `2 * CPU + 1`)
- `LOG_LEVEL` (default: `info`)

## Docker

The repository uses a lowercase `dockerfile`. Build using:

```bash
docker build -f dockerfile -t bcv-scraper .
```

Run the container:

```bash
docker run -p 8000:8000 bcv-scraper
```

By default, the container starts with Gunicorn and Uvicorn workers. You can override worker and port settings via environment variables:

- `WORKERS` (default: `4`)
- `PORT` (default: `8000`)

## Production

For production, a common pattern is to use Gunicorn with Uvicorn workers, for example:

```bash
gunicorn -k uvicorn.workers.UvicornWorker -w 4 -b 0.0.0.0:8000 main:app
```

Adjust the worker count based on CPU and load. If you prefer `run.py`, set `WORKERS`, `LOG_LEVEL`, and `RELOAD` appropriately.

## Deployment Notes

Every call to `/get-data` triggers a fresh scrape. For production usage, consider caching, scheduled scraping, or a data store to reduce load on the source website.

If you have the means, [crawlab](https://github.com/crawlab-team/crawlab) can run a scheduled crawler and store results for your API to read.

## Caveats & Operational Notes

- TLS verification is disabled in the scraper; this is not recommended for production environments.
- The scraper relies on specific HTML/XPath selectors. If the BCV page structure changes, scraping may break.
- Rate limits and politeness policies should be respected when calling the endpoint frequently.

## Contributing

Contributions are welcome! Please feel free to submit a pull request.

## License

No license specified yet.
