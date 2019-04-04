FROM alpine:3.5

RUN apk add --no-cache python3 && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
rm -r /root/.cache

WORKDIR /task1

ADD migrations /task1

ADD web_app /task1

ADD Procfile /task1

ADD config.py /task1

ADD first_app.py /task1

ADD consumer.py /task1

ADD secret.py /task1

ADD app.db /task1

ADD requirements.txt /task1

ADD requirements1.txt /task1

RUN pip install -r /task1/requirements1.txt

EXPOSE 72

CMD rabbitmq-server

