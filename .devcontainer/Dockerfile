# Using the official Python 3.11 Image
FROM python:3.11

# Install basic development tools
RUN apt-get update && apt-get install -y \
    git \
    curl \
    vim \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /workspace

# Install common python tools globally
RUN pip install --no-cache-dir \
    black \
    ruff \
    pytest \
    pre-commit \
    jupyter \
    ipykernel

# Note: Requirements will be installed by postCreateCommand to allow caching and faster rebuilds
