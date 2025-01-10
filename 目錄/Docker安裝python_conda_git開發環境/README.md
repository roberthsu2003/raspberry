## Docker安裝python_conda_git開發環境

- **Dockfile**

```dockfile
# Use an official Python base image
FROM python:3.10-slim

# Set environment variables to avoid prompts during installation
ENV DEBIAN_FRONTEND=noninteractive

# Install dependencies: curl, wget, git
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    git \
    && rm -rf /var/lib/apt/lists/*

# Download and install Miniconda
ENV CONDA_DIR=/opt/conda
RUN curl -fsSL https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh -o /tmp/miniconda.sh \
    && bash /tmp/miniconda.sh -b -p $CONDA_DIR \
    && rm /tmp/miniconda.sh

# Add Conda to PATH
ENV PATH=$CONDA_DIR/bin:$PATH

# Verify installation
RUN conda --version

# Set the working directory
WORKDIR /app

# Default command
CMD ["bash"]
```

- **建立image**
```bash
docker build -t my-python-miniconda-git .
```

- **建立容器**

```bash
docker run -it --name python-conda-container my-python-miniconda-git
```