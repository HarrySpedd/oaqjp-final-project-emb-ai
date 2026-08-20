import json
import requests


def emotion_detector(text_to_analyze):
  url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
  headers = {
      'grpc-metadata-mm-model-id': (
          'emotion_aggregated-workflow_lang_en_stock'
      )
  }
  myobj = {'raw_document': {'text': text_to_analyze}}

  response = requests.post(url, json=myobj, headers=headers)

  # Step 1: Convert response text into a dictionary
  formatted_response = json.loads(response.text)

  # Step 2: Extract required emotion scores
  emotions = formatted_response['emotionPredictions'][0]['emotion']
  anger_score = emotions['anger']
  disgust_score = emotions['disgust']
  fear_score = emotions['fear']
  joy_score = emotions['joy']
  sadness_score = emotions['sadness']

  # Step 3: Find the dominant emotion (highest score)
  emotion_scores = {
      'anger': anger_score,
      'disgust': disgust_score,
      'fear': fear_score,
      'joy': joy_score,
      'sadness': sadness_score,
  }

  dominant_emotion = max(emotion_scores, key=emotion_scores.get)

  # Step 4: Return formatted dictionary
  return {
      'anger': anger_score,
      'disgust': disgust_score,
      'fear': fear_score,
      'joy': joy_score,
      'sadness': sadness_score,
      'dominant_emotion': dominant_emotion,
  }