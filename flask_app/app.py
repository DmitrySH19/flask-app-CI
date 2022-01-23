from flask import Flask, render_template
from datetime import datetime


app = Flask(__name__)


@app.route("/")
def hello_world():
    time = datetime.now()
    # return render_template("index.html")
    return render_template(
        "index.html",
        current_date=datetime.date(time),
        current_time=datetime.time(time),
    )


if __name__ == "__main__":
    app.run()
