# Use R base image
FROM r-base:latest

# Install system dependencies for tidyverse & caret
RUN apt-get update && apt-get install -y \
    libcurl4-openssl-dev \
    libssl-dev \
    libxml2-dev \
    libfontconfig1-dev \
    libharfbuzz-dev \
    libfribidi-dev \
    libfreetype6-dev \
    libpng-dev \
    libtiff5-dev \
    libjpeg-dev && \
    rm -rf /var/lib/apt/lists/*

# Set working directory inside the container
WORKDIR /app

# Copy all project files and data into the container
COPY . .

# Install necessary R packages
RUN Rscript src_r/install_packages.R

# Run the main R script
CMD ["Rscript", "src_r/main.R"]
