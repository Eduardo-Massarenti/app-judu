from flask import Flask, render_template
from datetime import datetime
import json

app = Flask(__name__)

with open("config.json", "r", encoding="utf-8") as f:
  config = json.load(f)

@app.route("/")
def home():
  return render_template(
    "index.html",
    titulo=config.get("titulo", "Página"),
    imagens=config.get("imagens", []),
    frase=config.get("frase", [])
  )

if __name__ == "__main__":
  app.run()
