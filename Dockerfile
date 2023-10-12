# Use the official Python base image
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create and set the working directory inside the container
WORKDIR /app

# Copy the rest of the application code to the container
COPY . /app/

# Copy the requirements.txt file and install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN python manage.py makemigrations \
    && python manage.py migrate

#Port on which server runs
EXPOSE 8000

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]