FROM python:3.9-buster

# make app directry in container
RUN mkdir app
# copy files to app directry from local directry
COPY /PythonApp /app/

# setting WORKDIR is app directry
WORKDIR /app

# exec pip install in container
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# open a port 8080
EXPOSE 8080

# exec python program in container
CMD ["python","myWebserver.py"]