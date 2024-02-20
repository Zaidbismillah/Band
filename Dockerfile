# Use an official Python runtime as a parent image
FROM python:3.12.1

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000 to the outside world (if applicable)
# EXPOSE 8000

# Define the command to run on container start
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "bandsite.wsgi:application"]
