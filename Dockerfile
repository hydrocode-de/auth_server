ARG PYTHONVERSION=3.10

FROM python:$PYTHONVERSION
LABEL maintainer="Mirko Mälicke"

# create structure
RUN mkdir -p /src/auth_server
RUN mkdir -p /src/config

COPY ./auth_server /src/auth_server
COPY ./README.md /src/README.md
COPY ./requirements.txt /src/requirements.txt
COPY ./setup.py /src/setup.py

# install
RUN python -m pip install --upgrade pip
RUN cd /src && pip install -e .

CMD [ "python", "/src/auth_server/server.py" ]