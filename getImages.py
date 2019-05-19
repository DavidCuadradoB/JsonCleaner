import requests
import time
import properties.prop as prop

def getRedirectedUrl(imageUrl):
    response = requests.get(imageUrl)

    if response.status_code == "404" or not response.history:
        print("===== ERROR: ", imageUrl, " =====")
    time.sleep(0.5)
    print("imageUrl imported correctly: ", response.url)
    return response.url

def getImage(imageRef, maxWidth):
    if (imageRef == "") :
        return ""
    maxWidth = maxWidth if maxWidth else prop.google_image_default_maxwidth
    imageKeyUrl = prop.google_image_url % (maxWidth, imageRef)
    return getRedirectedUrl(imageKeyUrl)

code = "CmRZAAAAu1HnmEbPl4sR7xHkHDZVQTJ9kLq-j-8u138EzwjXGUE0QZgmjxmEToJIya0csMXCmQ1zHyo6HNt2MZBFb8ZYqxrd_LJNYidViFNf5FdN73WA5RaPozSo6gWKOnhSgVYfEhD08QroLE7PZHxNmKWPXSjAGhRttCgsM--7pXJUt6f03iFkiWdo_w"
width = 400

getImage(code, width)