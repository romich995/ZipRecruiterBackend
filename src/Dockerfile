FROM python:3.12-alpine
WORKDIR app
COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app
COPY ./src ./src
EXPOSE 8000
CMD [ "uvicorn", "src.main:app", "--host=0.0.0.0", "--reload" ]