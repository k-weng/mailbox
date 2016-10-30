import json
from template import get_fields

with open('cfg_nonprofits.json') as json_data:
    data = json.load(json_data, strict=False)
    json_data.close()

body = data["message"].encode('ascii', 'ignore')
fields = get_fields(body)
for field in fields:
    inp = raw_input(field[1:-1] + ": ")
    body = body.replace(field, inp)
print body

