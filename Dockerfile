FROM python:3.11-slim

# Install git (and other tools if needed)
RUN apt-get update && \
    apt-get install -y \
    bash \
    git git-lfs \
    wget curl procps \
    htop vim nano && \
    rm -rf /var/lib/apt/lists/*

RUN useradd -m -u 1000 user
USER user
ENV PATH="/home/user/.local/bin:$PATH"
WORKDIR /app

# Configure git
RUN git config --global user.email "slongia@users.noreply.huggingface.co"
RUN git config --global user.name "Surinder Longia"

COPY --chown=user ./requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY --chown=user . /app
ENV PYTHONPATH="/app/src:${PYTHONPATH}"
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]