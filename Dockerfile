FROM python:3.11

WORKDIR /usr/src/app
COPY . .

COPY requirements.txt .
RUN apt update
RUN apt-get install -y libsm6 libxext6 libxrender-dev libgl1-mesa-glx build-essential
RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python3", "app.py"]
