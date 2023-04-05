FROM python:3.9-slim-buster

WORKDIR /Users/suraaj/Desktop/dsml_minions/docker_for_minions

COPY requirements.txt ./
RUN python3 -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python","-m", "flask", "--app", "loan_app", "run", "--host=0.0.0.0"]