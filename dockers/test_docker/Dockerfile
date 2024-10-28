# указание базового образ (python:3-onbuild)
FROM python:3.11
# указание директории (создаст если не существует)
WORKDIR /test_docker
COPY ./requirements.txt /test_docker/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /test_docker/requirements.txt
COPY ./api.py /test_docker/api.py
COPY ./task.py /test_docker/task.py
#
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
