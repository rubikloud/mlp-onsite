FROM python:3.7.1

RUN apt-get update -y

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /wf/requirements.txt
EXPOSE 4000
WORKDIR /wf
RUN pip install -r requirements.txt

COPY . /wf

