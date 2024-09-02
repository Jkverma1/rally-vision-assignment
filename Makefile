install:
	pip install -r requirements.txt

run:
	uvicorn server:app --reload

docker-build:
	docker build -t person-detection-app .

docker-run:
	docker run -p 8000:8000 person-detection-app

test:
	pytest tests/
