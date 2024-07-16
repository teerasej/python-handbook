
# Create docker image

In this section, you will learn how to create a Docker image for the Django application.

## Step 1: Create a Dockerfile

1. Open the directory `LabFiles_Advance/10-django-container/project` in Visual Studio Code.
2. Create a new file named `Dockerfile` in the root directory of the project directory `project/Dockerfile`.
3. Write script to create a Docker image in the `Dockerfile`.

```Dockerfile
# Dockerfile
FROM python:3.11

# Set environment variables, this is optional
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app/

# The command in starting the container is to run the Django application at port 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

4. Save the file.
5. Right-click on the `project` directory and select `Open in Integrated Terminal` to open the terminal.
6. Run the following command to build the Docker image:

```bash
docker build -t django-app-01 .
```

## Step 2: Verify the Docker image

1. Run the following command to verify the Docker image:

```bash
docker images
```

2. You will see the `django-app-01` image in the list.
3. (Optional) You can check the images with Docker Desktop.
