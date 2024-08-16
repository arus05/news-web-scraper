from flask import Flask, render_template
import os
from articles import get_articles

app = Flask(__name__)

@app.route("/")
def index():
    return render_template(
        "index.jinja",
        get_articles = get_articles
    )


if __name__ == "__main__":
    app.debug = True
    app.run(
        port=5000,
        extra_files=[
            os.path.join(app.root_path, app.template_folder, "index.html")
        ]
    )