FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /app

# Install the published upstream package on ordinary Linux/Python.
# This keeps the upstream source untouched and avoids Cloudflare/Pyodide
# restrictions on native wheels such as pydantic-monty and watchfiles.
RUN pip install --no-cache-dir "mcp-brasil==0.14.0"

COPY runtimes/cloudflare-mcp-brasil/scripts/smoke_test.py /app/smoke_test.py
COPY runtimes/render-mcp-brasil/start.py /app/start.py

ENV MCP_BRASIL_AUTH_MODE=static \
    MCP_BRASIL_TOOL_SEARCH=bm25 \
    MCP_BRASIL_DATASETS="" \
    MCP_BRASIL_HTTP_TIMEOUT=20.0 \
    MCP_BRASIL_HTTP_MAX_RETRIES=2

EXPOSE 10000

CMD ["python", "/app/start.py"]
