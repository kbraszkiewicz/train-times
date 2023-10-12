import requests
import json

from data import Board, Train, Stop
def loadKey():
    with open("apikey.txt") as file:
        key = file.read()
    return key

def getLiveData(code):
    responce = requests.get(
        f"https://api1.raildata.org.uk/1010-live-arrival-and-departure-boards-arr-and-dep/LDBWS/api/20220120/GetArrDepBoardWithDetails/{code}?numRows=50,timeWindow",
        headers={"x-apikey":loadKey()}
    )
    return json.loads(responce.text)

def getDepartureBoard(code):
    data = getLiveData(code)
    trains = data["trainServices"]
    trainsOut=[]
    print(trains)
    for train in trains:
        print(train)
        if train.get("subsequentCallingPoints") ==None:
            continue
        if len(train["subsequentCallingPoints"][0]["callingPoint"])>0:

            print(train["destination"][0]["locationName"])

            stopsOut=[]
            for i in train["subsequentCallingPoints"][0]["callingPoint"]:
                stopsOut.append(Stop(i["locationName"],i["st"]))


            trainsOut.append(Train( "LDS",
                    train["destination"][0]["locationName"],
                    "?" if train.get("std") is None else train["std"],
                    "On Time" if train.get("etd") is None else train["etd"],
                    "N/A" if train.get("platform") is None else train["platform"],
                    stopsOut
                    ))
    return Board(
        "leeds",
        trainsOut
    )
    



getDepartureBoard("LDS")