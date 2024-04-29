# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app
COPY ./run.sh /app
# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5001

# Define environment variable

# Run app.py when the container launches
##CMD ["flask", "run", "--host=0.0.0.0"]
RUN chmod +x ./run.sh 
CMD ["./run.sh"]

## IN ORDER TO RUN THE APPLICATION MAKE SURE YOU HAVE DOCKER DESKTOP INSTALLED AND RUNNING
## ONCE THE DOCKER DESKTOP IS RUNNING EXECUTE docker build <ABSOLUTE PATH TO ROOT> fyle-interview-intern-backend -t my-flask-app 
## THEN EXECUTE docker-compose up