import requests
from bs4 import BeautifulSoup
import urllib.request

if __name__ == '__main__':

    while True:
        print("Enter a word to search or /q to quit")
        try:
            word = input(">Search word:\t")
            if word == "q":
                break

            search = requests.get("https://www.signingsavvy.com/sign/" + word).text

            soup = BeautifulSoup(search, 'lxml')

            videoContent = soup.find("div", class_="videocontent")
            # By default , ASL 1 shows video
            # Make a loop that allows me to go through the different links and gets all links
            videoLink = videoContent.find("source")["src"]

            meaning = soup.find("ul", class_="list tags-v2 margin-bottom-10").text

            print(f"""
            Video Link: {videoLink}
            Meaning: {meaning}
            """)
            while True:
                print("Do you wish to download the video file?")
                answer = input(">y/n:\t")
                if answer == "y":
                    urllib.request.urlretrieve(videoLink, f'{word}.mp4')
                    break
                elif answer == "n":
                    break
                else:
                    print("invalid answer")

        except AttributeError:
            print("Make sure the content is a word. Word can't be a number")
