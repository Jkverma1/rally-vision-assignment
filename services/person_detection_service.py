import requests

class PersonDetectionService:
    def __init__(self, model_weights_url: str):
        self.model_weights_url = model_weights_url

    def detect_person(self, input_url: str):
        # Code to detect person using the YOLO model
        response = requests.post('https://api.ultralytics.com/v1/detect', json={
            'model': self.model_weights_url,
            'input': input_url
        })
        return response.json()
