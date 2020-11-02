FROM python:3.7.9

RUN apt-get update -y

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt
COPY . /app
EXPOSE 4000
WORKDIR /app
ENV FLASK_APP=api_app.py
RUN pip install -r requirements.txt

# ENTRYPOINT [ "python" ]
CMD ["flask","run","--host", "0.0.0.0","--port","4000"]
