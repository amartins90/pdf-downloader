from Downloader import Downloader
import sys

def main():
    year = 0
    competition_id = 0

    if len(sys.argv) >= 3:
        if sys.argv[1].isdigit():
            year = sys.argv[1]

        if sys.argv[2].isdigit():
            competition_id = sys.argv[2]

    downloads_total = 0
    match_id = 1

    while match_id - downloads_total < 2:
        t = Downloader(year, competition_id, match_id)
        financial_file, scoresheet_file = t.downloadFile()
        match_id += 1
        if financial_file or scoresheet_file:
            downloads_total += 1

if __name__ == "__main__":
    main()
