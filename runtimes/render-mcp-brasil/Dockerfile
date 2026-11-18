FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /app

# Install the published upstream package on ordinary Linux/Python.
# This keeps the upstream source untouched and supports native dependencies
# required by FastMCP Code Mode.
RUN pip install --no-cache-dir "mcp-brasil==0.14.0"

COPY runtimes/cloudflare-mcp-brasil/scripts/smoke_test.py /app/smoke_test.py
COPY runtimes/render-mcp-brasil/start.py /app/start.py

EXPOSE 10000

CMD ["python", "/app/start.py"]
