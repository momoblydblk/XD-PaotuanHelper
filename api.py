"""
Module to implement XD APIs
Methods:

Todos:


"""
import requests
import json

# URI to post to when creating a thread
API_URI = "https://api.nmb.best/api/"
retrieveBoardURI = API_URI + "getForumList"
createThreadURI = "https://www.nmbxd1.com/Home/Forum/doPostThread.html"


def getBoard() -> list:
    board_list_response = requests.get(retrieveBoardURI)
    board_list: list[dict] = json.loads(board_list_response.text)
    for i in board_list:
        print("\n\n\n")
        for j in i["forums"]:
            print(j)
            for key, value in j.items():
                print(key + ":" + value)



if __name__ == "__main__":
    pass
    #getBoard()
