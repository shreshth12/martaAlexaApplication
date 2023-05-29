import requests, json

# IDEAL_URL = "http://developer.itsmarta.com/RealtimeTrain/RestServiceNextTrain/GetRealtimeArrivals?apikey={api_key}"


def getAllTrainData() -> dict:
    query_url = "http://developer.itsmarta.com/RealtimeTrain/RestServiceNextTrain/GetRealtimeArrivals"
    response = requests.get(query_url)
    return response.json()


def prettyPrintJson(json_object: list) -> str:
    data = json.dumps(json_object, indent=4)
    print(data)


def getStationData(station_name: str, direction: str) -> list:
    station_data = []
    json_object = getAllTrainData()
    for value in json_object:
        if value["STATION"] == station_name and value["DIRECTION"] == direction:
            station_data.append(value)
    return station_data


obj = getStationData(station_name="LINDBERGH STATION", direction="S")
prettyPrintJson(obj)
