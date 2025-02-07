# base image with python 3.8
FROM python:3.8

# set working directory 
WORKDIR /app

# install netcat
RUN apt-get update && apt-get install -y netcat

# install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# copy application code
COPY . .

# make entrypoint.sh executable
RUN chmod +x entrypoint.sh

# expose port 8020
EXPOSE 8020

# run entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]
