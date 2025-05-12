from flask import Flask, request, render_template
from dotenv import load_dotenv
import logging

from app.services import analyze_business_card

load_dotenv()

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if 'business_card_image' in request.files:
            business_card_image = request.files['business_card_image']
            if business_card_image.filename != '':
                try:
                    business_card_data = analyze_business_card(business_card_image=business_card_image)
                    return render_template("index.html", card_data=business_card_data)
                except Exception as e:
                    logging.info(f"Exeption: {e}")
                    return render_template("index.html", error='There was error processing image.')
            else:
                return render_template("index.html", error='No file selected')
        else:
            return render_template("index.html", error='Business card image not found')
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)