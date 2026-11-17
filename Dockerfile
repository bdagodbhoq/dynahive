FROM python:3.10-slim
WORKDIR /app
COPY . /app
ENV PYTHONPATH=/app
RUN useradd --create-home --uid 1000 decoy \
 && chown -R decoy:decoy /app
USER decoy
CMD ["python", "scripts/run_mock.py"]
