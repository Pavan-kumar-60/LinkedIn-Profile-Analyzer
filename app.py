from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()

from ice_breaker import ice_break_with


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process():
    name = request.form["name"]
    summary_and_facts, profile_pic_url = ice_break_with(
        name=name
    )
    data = {
        "summary_and_facts": summary_and_facts.to_dict(),
        "picture_url": profile_pic_url,
        "name": name
    }
    
    # Render the results template with the data
    return render_template('results.html', data=data)



if __name__ == "__main__":

    app.run(host="0.0.0.0", debug=True)