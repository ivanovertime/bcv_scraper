FROM python:3.12.1-alpine 
ADD * .
RUN pip install -r requirements.txt
CMD ["sh", "-c", "gunicorn -k uvicorn.workers.UvicornWorker -w ${WORKERS:-4} -b 0.0.0.0:${PORT:-8000} main:app"]
