
FROM python:3.11-slim-bullseye

# Set environment variables.
ENV PYTHONWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

# Set working directory.
WORKDIR /code

# Copy dependencies.
COPY requirements.txt /code/

# Install dependencies.
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy project.
COPY  ./app /code/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]