# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8-slim

EXPOSE 8000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

RUN apt update && apt dist-upgrade -y
RUN apt install -y locales libc-bin locales-all
RUN sed -i '/pt_BR.UTF-8/s/^#//g' /etc/locale.gen \
  && locale-gen en_US en_US.UTF-8 pt_BR pt_BR.UTF-8 \
  && dpkg-reconfigure locales \
  && update-locale LANG=pt_BR.UTF-8 LANGUAGE=pt_BR.UTF-8 LC_ALL=pt_BR.UTF-8
ENV LANG pt_BR.UTF-8  
ENV LANGUAGE pt_BR:pt  
ENV LC_ALL pt_BR.UTF-8
ENV LC_CTYPE pt_BR.UTF-8
ENV LC_TIME pt_BR.UTF-8

RUN apt-get install -y build-essential libssl-dev libffi-dev python-dev
RUN apt-get install -y default-mysql-client libmariadb-dev-compat libmariadb-dev 

# Install pip requirements
COPY requirements.txt .

RUN python -m pip install pip -U
RUN python -m pip install -r requirements.txt -U

WORKDIR /home/userapp
COPY ./src /home/userapp

# Creates a non-root user with an explicit UID and adds permission to access the /home/userapp folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 1001 --disabled-password --gecos "" appuser && chown -R appuser /home/userapp
USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "SolicitacaoDeTurmas.wsgi"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
