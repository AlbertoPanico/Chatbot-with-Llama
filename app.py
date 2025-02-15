from flask import Flask, render_template, request, jsonify
from chat import get_response
from flask_cors import CORS


app = Flask(__name__, template_folder='template') #  template_folder='templates'
CORS(app)

@app.route("/chat")
#@app.get("/")
def index_get():
    return render_template("index.html")

@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    if len(text) > 100:
        message = {"answer": "I'm sorry, your query has too many characters for me to process. If you would like to speak to a live agent, say 'I would like to speak to a live agent'"}
        return jsonify(message)
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)

if __name__ == "__main__":
    app.run(debug=True) # host='127.0.0.2'


