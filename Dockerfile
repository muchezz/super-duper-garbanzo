FROM python:3.9-slim

WORKDIR /app
COPY . /app

RUN pip install flask
RUN pip install pytest

# 👇 Intentionally hardcoded env vars (to be caught by scanners like Trivy)
ENV ENV=production
ENV VERSION=2.3.1
ENV SECRET_KEY=supersecretkey123
ENV API_TOKEN=ghp_ThisIsADemoTokenToTriggerWarning

EXPOSE 5000

CMD ["python", "app.py"]
