
from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    df = pd.read_excel("baseballPOG.xlsx", sheet_name="支配下選手")
    players = df.to_dict(orient="records")
    selected_players = []

    if request.method == "POST":
        for player in players:
            name = player["選手名"]
            position = request.form.get(f"position_{name}")
            order = request.form.get(f"order_{name}")
            if position or order:
                selected_players.append({
                    "name": name,
                    "position": position,
                    "order": order
                })
        return render_template("result.html", selected_players=selected_players)

    return render_template("index.html", players=players)

if __name__ == "__main__":
    app.run(debug=True)
