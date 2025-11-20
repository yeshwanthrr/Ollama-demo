FROM python:3.11-slim
WORKDIR /workdir
COPY demo.py /workdir/
RUN pip install --no-cache-dir requests
CMD ["python3", "demo.py"]
