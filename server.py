from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def detect_emotion():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    emotions_str = ", ".join(
        [f"'{key}': {value}" for key, value in response.items() if key != "dominant_emotion"]
    )
    dominant = response.get("dominant_emotion", "unknown")
    result = (f"For the given statement, the system response is {emotions_str}. "
              f"The dominant emotion is {dominant}.")
    return result

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
