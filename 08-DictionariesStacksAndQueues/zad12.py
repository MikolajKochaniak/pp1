import json
phone = {
"number":"35625362",
"model":"13",
"brand": "Banach",
"age": 25,
"guarantee": True,
"apps":["App_strore","chrome"]

}
with open("favourite.json","w") as json_file:
    json.dump(phone,json_file,indent = 4)