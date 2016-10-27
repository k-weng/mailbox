import json

with open('examples.json') as json_data:
    data = json.load(json_data, strict=False)
    json_data.close()

name = "Bob"
ndata = data["message"].encode('ascii', 'ignore')
print type(ndata)
print ndata.find("[name]")
body = ndata.replace("[name]", name)
print body
