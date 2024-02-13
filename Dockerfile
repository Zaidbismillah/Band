# Use an official Nginx base image
FROM nginx


# Set environment variables for Django (if applicable)
ENV ['DJANGO_SETTINGS_MODULE'] = 'Bandsite.settings'

# Create and set the working directory in the container
WORKDIR /usr/share/nginx/html

# Copy the current directory contents into the container
COPY . /usr/share/nginx/html

# Install any needed packages specified in requirements.txt (if applicable)
RUN pip install -r requirements.txt

# Expose port 8000 to the outside world (if your Django app is running on this port)
EXPOSE 8000

# Define the command to run when the container starts
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
