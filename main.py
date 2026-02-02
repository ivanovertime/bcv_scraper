from fastapi import FastAPI
from scraper import scrapeData

app = FastAPI()


@app.get("/")
async def index():
    """ index route """

    return {
        "get-data": "visit /get-data to get scraped data",
    }

@app.get("/get-data")
async def get_data():
    """ Get all scraped data as in json by visiting /get-data """
    return scrapeData()
