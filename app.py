
from flask import Flask, request, render_template
from gradio_client import Client

app = Flask(__name__)
client = Client("duchaba/Friendly_Text_Moderation")


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        text = request.form.get("text")
        safer_value = request.form.get("saferValue")

        try:
            prediction = client.predict(
                msg=text,
                safer=float(safer_value),
                api_name="/fetch_toxicity_level"
            )
            result = prediction
        except Exception as e:
            result = f"Error Message: {str(e)}"

    return render_template("index.html", result=result)
