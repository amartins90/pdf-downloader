from dotenv import load_dotenv
import os
import requests

class Downloader:

    def __init__(self, year=None, competition_id=None, match_id=None):
        if year is None:
            year = 0
        self.year = str(year)

        if competition_id is None:
            competition_id = 0
        self.competition_id = str(competition_id)
        
        if match_id is None:
            match_id = 0
        self.match_id = str(match_id)

        load_dotenv()
        
        print(f"Year: {year}, Competition ID: {competition_id}, Match ID: {match_id}")

    def buildUrl(self):
        base_url = os.getenv("BASE_URL")
        financial_path = os.getenv("FINANCIAL_PATH")
        scoresheet_path = os.getenv("SCORESHEET_PATH")

        if base_url is None or financial_path is None or scoresheet_path is None:
            return None, None

        financial_url = base_url + financial_path.replace("{year}", self.year).replace("{competition_id}", self.competition_id).replace("{match_id}", self.match_id)
        scoresheet_url = base_url + scoresheet_path.replace("{year}", self.year).replace("{competition_id}", self.competition_id).replace("{match_id}", self.match_id)

        return financial_url, scoresheet_url

    def downloadFile(self):
        financial_url, scoresheet_url = self.buildUrl()
        # TODO create logs
        if financial_url is not None:
            if requests.options(financial_url).ok:
                filename = self.match_id + "_f.pdf"
                with open(filename, "wb") as f:
                    f.write(requests.get(financial_url).content)

        if scoresheet_url is not None:
            if requests.options(scoresheet_url).ok:
                filename = self.match_id + "_s.pdf"
                with open(filename, "wb") as f:
                    f.write(requests.get(financial_url).content)

        return None

