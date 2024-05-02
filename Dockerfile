# Use an official Python runtime as a parent image
FROM python:3.12

# Set the working directory in the container
WORKDIR /app

# Install poetry
RUN pip install pipx
RUN pipx install poetry

# Copy pyproject.toml and install dependencies
COPY pyproject.toml .
COPY poetry.lock .
RUN /root/.local/bin/poetry install

# Copy the rest of the application code
COPY src .
#COPY tests .


# Expose the port the app runs on
EXPOSE 8000 
# Run the application
#CMD ["/root/.local/bin/poetry", "run", "uvicorn", "main:app", "--host", "127.0.0.1", "--port", "8000"]
#Run the application
#CMD ["/root/.local/bin/poetry", "run", "python", "main.py", "--host", "127.0.0.1", "--port", "8000"]
CMD ["/root/.local/bin/poetry","run", "python", "main.py", "--host", "127.0.0.1", "--port", "8000"]