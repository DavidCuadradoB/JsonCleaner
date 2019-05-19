import json
import glob, os
import codecs
import requests


cleanPath = "C:\\Users\\fnxcu\\Documents\\python\\cleanerJson\\cleanedFiles"
originJsonPath = "C:\\Users\\fnxcu\\Documents\\python\\cleanerJson\\jsonsFiles"

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)


def cleanTypes(types):
    acceptedTypes = ["church", "museum", "park"]
    cleanTypes=[]
    for type in types:
        if type in acceptedTypes:
            cleanTypes.append(type)

    return cleanTypes

def getCityName(originCity):
    acceptedTypes = ["amsterdam", "londres", "madrid", "salamanca"]
    genericCity="otro"
    if originCity in acceptedTypes:
        return originCity
    else:
        return genericCity

def cleanPhotos(photos):
    if photos:
        photo = photos[0]
        if "photo_reference" in photo:
            return photo["photo_reference"]
    return ""

def getLocation(geometry):
    if geometry:
        if "location" in geometry:
            return geometry["location"]
    return {}

def generateJson(filePath):
    data=""

    fileSplited = filePath.split("\\")
    cityFolder = getCityName(fileSplited[-2])
    resultFile = fileSplited[-1]


    # with open(filePath, 'rb') as myFile:
    with codecs.open(filePath, 'rb', "utf-8") as myFile:
        data = myFile.read()

    dataParsed = json.loads(data)
    results = dataParsed["results"]

    pois=[]
    for result in results:
        poi={}
        poi["city"]=cityFolder
        poi["location"] = getLocation(result["geometry"]) if "geometry" in result else ""
        poi["id"] = result["id"] if "id" in result else ""
        poi["name"]=result["name"] if "name" in result else ""
        poi["photo_reference"] = cleanPhotos(result["photos"]) if "photos" in result else ""
        poi["rating"]=result["rating"] if "rating" in result else ""
        poi["types"]= cleanTypes(result["types"]) if "types" in result else []


        # if "geometry" in result:
        #     poi["geometry"]=result["geometry"]
        # if "icon" in result:
        #     poi["icon"]=result["icon"]
        # if "id" in result:
        #     poi["id"]=result["id"]
        # if "name" in result:
        #     poi["name"]=result["name"]
        # if "photos" in result:
        #     poi["photo_reference"] = cleanPhotos(result["photos"])
        # if "opening_hours" in result:
        #     poi["opening_hours"]=result["opening_hours"]
        # if "place_id" in result:
        #     poi["place_id"]=result["place_id"]
        # if "plus_code" in result:
        #     poi["plus_code"]=result["plus_code"]
        # if "rating" in result:
        #     poi["rating"]=result["rating"]
        # if "reference" in result:
        #     poi["reference"]=result["reference"]
        # if "scope" in result:
        #     poi["scope"]=result["scope"]
        # if "types" in result:
        #     poi["types"]= cleanTypes(result["types"])
        # if "user_ratings_total" in result:
        #     poi["user_ratings_total"] = result["user_ratings_total"]
        # if "vicinity" in result:
        #     poi["vicinity"]=result["vicinity"]
        pois.append(poi)

    cleanFile = cleanPath + "\\" + cityFolder + "\\" + resultFile

    createFolder(cleanPath + "\\" + cityFolder)

    with codecs.open(cleanFile, 'wb', "utf-8") as outFile:
        json.dump(pois, outFile, indent=4, ensure_ascii=False)
    print("end")

for file in glob.glob(originJsonPath + '/**/*.json', recursive=True):
    print("\n\n\ngenerating: ", file.split("\\")[-2], " - ", file.split("\\")[-1])
    generateJson(file)
    print("========end=======")

# testFile = "C:\\Users\\fnxcu\\Documents\\python\\cleanerJson\\jsonsFiles\\madrid\\park.json"

# generateJson(testFile)