# Use Python 3.9.1
FROM python:3.9-slim-buster as base

# Work directory inside container
WORKDIR /app

ADD infra ./infra
ADD requirements.txt setup.py Makefile ./

# Install Python packages
RUN apt-get update -y -qq &&  apt install build-essential -y 
RUN pip install -r requirements.txt && make install_dev

###########START NEW IMAGE : DEBUGGER ###################
FROM base as debug

# Environment variables to configure debugpy
ENV DEBUG_HOST="0.0.0.0" \ 
    DEBUG_PORT="5678" \
    DEBUG_LIB_PATH="./infra" \
    DEBUG_MODULE="configs" \
    DEBUG_FILE="connection.py"

# Work directory inside container
WORKDIR /app
RUN pip install debugpy
CMD python -m debugpy --listen ${DEBUG_HOST}:${DEBUG_PORT} --wait-for-client ${DEBUG_LIB_PATH}/${DEBUG_MODULE}/${DEBUG_FILE}
EXPOSE ${DEBUG_PORT}

###########START NEW IMAGE: PRODUCTION ###################
FROM base as prod
