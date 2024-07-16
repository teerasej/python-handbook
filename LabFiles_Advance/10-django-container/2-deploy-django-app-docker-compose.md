
# Deploy Django Application with docker compose

In this section, you will learn how to deploy a Django application with Docker Compose.

## Step 1: Create a Docker Compose file

1. Open the directory `LabFiles_Advance/10-django-container/project` in Visual Studio Code.
2. Create a new file named `docker-compose.yml` in the root directory of the project directory `project/docker-compose.yml`.
3. Write script to create a Docker Compose file in the `docker-compose.yml`.

```yml
# docker-compose.yml
version: '3'

# Define the services
services:

  # Define the web service
  web:
    # Build the Docker image from the Dockerfile
    build: .
    # Run the command to start the Django application in the container
    command: python manage.py runserver 0.0.0.0:8000

    # Mount the current directory to the /app directory in the container
    volumes:
      - .:/app

    # Expose the port 8000
    ports:
      - "8000:8000"
```

4. Save the file.
5. Right-click on the `project` directory and select `Open in Integrated Terminal` to open the terminal.
6. Run the following command to deploy the Django application with Docker Compose:

```bash
docker compose up --build
```

7. Open a web browser and go to `http://localhost:8000/admin` to view the Django application.