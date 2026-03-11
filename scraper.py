import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_nba_players():
    URL = "https://www.nba.com/stats"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    response = requests.get(URL, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    all_players = soup.find_all(
        "a",
        class_="Anchor_anchor__cSc3P LeaderBoardPlayerCard_lbpcTableLink__MDNgL"
    )

    player_names = [player.get_text(strip=True) for player in all_players]

    df = pd.DataFrame({"Player": player_names})
    df.to_excel("nba_players.xlsx", index=False)

    return player_names