FROM python:3.8-slim AS BUILDER
WORKDIR /app
RUN python -m venv venv
COPY requirements.txt requirements.txt
RUN . venv/bin/activate && pip install -r requirements.txt

FROM python:3.8-slim AS APP
WORKDIR /app
COPY --from=BUILDER /app/venv /app/venv
COPY . .
ENV PATH="/app/venv/bin:$PATH"
RUN ['python', 'src/main.py']
