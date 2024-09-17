# Simple implementation of RestAPI (FastAPI)

[For Django](https://github.com/ZeroNiki/Django-RestAPI-Example)<br>
A simple example of using RestAPi on FastAPI

## Install

```bash
git clone https://github.com/ZeroNiki/FastAPI-RestAPI-Example.git

cd FastAPI-RestAPI-Example
```

```bash
python3 -m venv venv

source venv/bin/activate

pip insatll -r requirements.txt
```

```bash
alembic revision --autogenerate -m "INIT"

alembic upgrade head
```

```bash
uvicorn start:app --reload
```

go to http://localhost:8000/docs<br>
Enjoy!

## Usage

### Curl

get all:

```bash
curl --request GET --url "localhost:8000/operations/data"
```

get todo:

```bash
curl --request GET --url "localhost:8000/operations/task/{id}"
```

add todo:

```bash
curl --header "Content-Type: application/json" \
--request POST \
--data '{"title": "title test"}' \
http://127.0.0.1:8000/operations/add
```

Update todo:

```bash
curl --header "Content-Type: application/json" \
--request PUT \
--data '{"title": "Update title test"}' \
http://127.0.0.1:8000/operations/update/{id}
```

Delete todo:

```bash
curl --request DELETE "localhost:8000/operations/delete/{id}"
```
