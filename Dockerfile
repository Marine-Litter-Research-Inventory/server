FROM --platform=linux/amd64 python:3

# copy the requirements file into the image
COPY . /app/

# switch working directory
WORKDIR /app

# install the dependencies and packages in the requirements file
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# configure the container to run in an executed manner
CMD gunicorn -w 2 main:app

EXPOSE 8000