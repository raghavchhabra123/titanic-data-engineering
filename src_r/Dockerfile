# Use the official R base image
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
    libjpeg-dev

# Set working directory inside the container
WORKDIR /app

# Copy all R scripts and supporting files into the container
COPY . .

# Copy the local dataset from the parent folder into the container
COPY ../data ./data

# Install necessary R packages
RUN Rscript src_r/install_packages.R

# Run the main R script
CMD ["Rscript", "src_r/main.R"]
