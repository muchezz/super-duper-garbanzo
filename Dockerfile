FROM python:3.9-slim

# Create a non-root user to run the application
RUN adduser --disabled-password --gecos "" appuser

WORKDIR /app
COPY . /app

# Install dependencies
RUN pip install flask pytest

# Switch to non-root user
USER appuser

# Add a health check to verify the app is running
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:5000/ || exit 1

# Expose the application port
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]