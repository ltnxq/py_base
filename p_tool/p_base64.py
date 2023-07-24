import base64
with open("base64.txt","r") as base64f:
    imgdata_64 = base64f.read()

imgdata = base64.b64decode(imgdata_64)
print(type(imgdata))

with open("temp.JPEG","wb") as f:
    f.write(imgdata) 