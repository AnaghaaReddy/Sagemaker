FROM ubuntu:20.04

# Set environment variable to avoid timezone prompt
ENV DEBIAN_FRONTEND=noninteractive

# Install necessary packages
RUN apt-get update && \
    apt-get -y install build-essential libatlas-base-dev git wget curl python3-dev python3-distutils software-properties-common && \
    add-apt-repository ppa:ubuntu-toolchain-r/test && \
    apt-get update && \
    apt-get -y install gcc-9 g++-9 libstdc++6 && \
    rm -rf /var/lib/apt/lists/*

# Set gcc and g++ as the default compilers
RUN update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-9 100
RUN update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-9 100

# Install Miniconda
RUN curl -LO https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh && \
    bash Miniconda3-latest-Linux-x86_64.sh -b -p /miniconda3 && \
    rm Miniconda3-latest-Linux-x86_64.sh

# Set the PATH
ENV PATH=/miniconda3/bin:${PATH}

# Update conda and install required packages directly into the base environment
RUN conda update -y conda && \
    conda install -y python=3.9 numpy pandas scikit-learn scipy && \
    pip install --no-cache-dir boto3 sagemaker retrying

# Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 PYTHONIOENCODING=UTF-8 LANG=C.UTF-8 LC_ALL=C.UTF-8

# Copy your scripts and binaries
ADD process_script.py /
ADD a.out /

# Give executable permissions to a.out
RUN chmod +x /a.out

# Specify the command to run your application by default (optional)
CMD ["python3", "/process_script.py"]
FROM ubuntu:20.04

# Set environment variable to avoid timezone prompt
ENV DEBIAN_FRONTEND=noninteractive

# Install necessary packages
RUN apt-get update && \
    apt-get -y install build-essential libatlas-base-dev git wget curl python3-dev python3-distutils software-properties-common && \
    add-apt-repository ppa:ubuntu-toolchain-r/test && \
    apt-get update && \
    apt-get -y install gcc-9 g++-9 libstdc++6 && \
    rm -rf /var/lib/apt/lists/*

# Set gcc and g++ as the default compilers
RUN update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-9 100
RUN update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-9 100

# Install Miniconda
RUN curl -LO https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh && \
    bash Miniconda3-latest-Linux-x86_64.sh -b -p /miniconda3 && \
    rm Miniconda3-latest-Linux-x86_64.sh

# Set the PATH
ENV PATH=/miniconda3/bin:${PATH}

# Update conda and install required packages directly into the base environment
RUN conda update -y conda && \
    conda install -y python=3.9 numpy pandas scikit-learn scipy && \
    pip install --no-cache-dir boto3 sagemaker retrying

# Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 PYTHONIOENCODING=UTF-8 LANG=C.UTF-8 LC_ALL=C.UTF-8

# Copy your scripts and binaries
ADD process_script.py /
ADD a.out /

# Give executable permissions to a.out
RUN chmod +x /a.out

# Specify the command to run your application by default (optional)
CMD ["python3", "/process_script.py"]
FROM ubuntu:20.04

# Set environment variable to avoid timezone prompt
ENV DEBIAN_FRONTEND=noninteractive

# Install necessary packages
RUN apt-get update && \
    apt-get -y install build-essential libatlas-base-dev git wget curl python3-dev python3-distutils software-properties-common && \
    add-apt-repository ppa:ubuntu-toolchain-r/test && \
    apt-get update && \
    apt-get -y install gcc-9 g++-9 libstdc++6 && \
    rm -rf /var/lib/apt/lists/*

# Set gcc and g++ as the default compilers
RUN update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-9 100
RUN update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-9 100

# Install Miniconda
RUN curl -LO https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh && \
    bash Miniconda3-latest-Linux-x86_64.sh -b -p /miniconda3 && \
    rm Miniconda3-latest-Linux-x86_64.sh

# Set the PATH
ENV PATH=/miniconda3/bin:${PATH}

# Update conda and install required packages directly into the base environment
RUN conda update -y conda && \
    conda install -y python=3.9 numpy pandas scikit-learn scipy && \
    pip install --no-cache-dir boto3 sagemaker retrying

# Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 PYTHONIOENCODING=UTF-8 LANG=C.UTF-8 LC_ALL=C.UTF-8

# Copy your scripts and binaries
ADD process_script.py /
ADD a.out /

# Give executable permissions to a.out
RUN chmod +x /a.out

# Specify the command to run your application by default (optional)
CMD ["python3", "/process_script.py"]
