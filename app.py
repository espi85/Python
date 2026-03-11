from flask import Flask, render_template, send_file
from scraper import scrape_nba_players

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/scrape")
def scrape():
    players = scrape_nba_players()
    return render_template("index.html", players=players, done=True)

@app.route("/download")
def download():
    return send_file("nba_players.xlsx", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
