# Stage 1: Builder stage to create wheels for dependencies
FROM python:3.10-alpine as builder

# Install build dependencies
RUN apk update && \
    apk add --no-cache postgresql-dev gcc python3-dev musl-dev

# Set working directory
WORKDIR /app

# Copy the requirements file and build wheels for dependencies
COPY requirements.txt .
RUN pip wheel --no-cache-dir --wheel-dir /app/wheels -r requirements.txt

# Stage 2: Final image stage
FROM python:3.10-alpine


RUN apk update && \
    apk add --no-cache libpq

# Set working directory
WORKDIR /app

# Copy built wheels from the builder stage and install them
COPY --from=builder /app/wheels /wheels
RUN pip install --no-cache /wheels/*

# Copy application code
COPY . .

# Expose the application port
EXPOSE 8000

