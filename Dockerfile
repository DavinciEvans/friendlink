FROM python:3.6
WORKDIR /Home/python_projects

COPY requirements.txt ./
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

COPY . .

ENV FLASK_APP friendLink

CMD ["flask", "initenv"]
CMD ["gunicorn", "start:app", "-c", "./gunicorn.conf.py"]