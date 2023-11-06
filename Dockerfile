FROM python:3

WORKDIR /usr/app/src

COPY app.py ./
COPY requirements.txt ./

RUN pip install --no-cache-dir --upgrade pip \
  && pip install --no-cache-dir -r requirements.txt

CMD ["python", "-u", "./app.py"]