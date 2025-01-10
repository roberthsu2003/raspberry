# Docker安裝python_conda_git開發環境
- 電腦必需有安裝Docker

## 方法1:使用Docker Hub Repository
- 使用以下的repository

`continuumio/miniconda3`

### 步驟1 **下載repository**

```
docker pull continuumio/miniconda3
```

### 步驟2 **建立容器**
- 請不要直接使用Docker Desktop直接啟動(因為容器啟動後會直接關閉)
- 使用以下指令,建立容器,並且要求可互動,和配置一個偽TTY(容器啟動後不會自動關閉)

```bash
docker run -it --name python-miniconda continuumio/miniconda3

#-it 要求可互動,和配置一個偽TTY
#--name python-miniconda 建立容器名稱
#continuumio/miniconda3 映像名稱(一定在最後面)
```

### 步驟3 **使用VSCode Docker容器開發工具**
### 步驟4 **下載github專案**
### 步驟5 **安裝VSCode套件**
- python
- jupyter
### 步驟6 **安裝python外部套件**

## 方法2:自訂Dockerfile方式(不方便)
- 自已下載的方式

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