FROM python:3.11 as requirements_stage

WORKDIR /tmp

RUN pip install poetry

COPY ./pyproject.toml ./poetry.lock /tmp/

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

FROM python:3.11

WORKDIR /app

COPY --from=requirements_stage /tmp/requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./app.py /app/app.py

COPY ./vetclinic_service /app/vetclinic_service

CMD [ "uvicorn", "app:app", "--host=0.0.0.0", "--port=8000" ]