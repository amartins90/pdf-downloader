from Downloader import Downloader

def main():
    # Paulista x Colorado - Final, 2nd leg
    t = Downloader(2024, 74104, 130)
    t.downloadFile()

if __name__ == "__main__":
    main()
