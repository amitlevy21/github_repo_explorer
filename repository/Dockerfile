FROM python:3.8.5

COPY requirments.txt /tmp
RUN pip install -r /tmp/requirments.txt

COPY . /app
WORKDIR /app

RUN chmod +x /app/main.sh

CMD [ "./main.sh" ]