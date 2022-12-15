FROM python:3.9

ADD main.py /

RUN pip install threaded

CMD [ "python", "./main.py" ]
