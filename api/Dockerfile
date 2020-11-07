FROM python:3
WORKDIR /usr/src/
COPY requirements.txt /usr/src/
RUN pip install -r /usr/src/requirements.txt
COPY . .
CMD [ "python", "main.py" ]
