FROM python:3.11

WORKDIR /usr/src/app

COPY ../../backend/requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY ../../backend .

CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0", "--port=5001"]
