from datetime import datetime
import json
from instagrapi import Client

cl = Client()
account_name = ""
password = ""
cl.login(account_name, password)

print("please input hashtag: ")
input_hashtag = input()

print("please input total records: ")
input_amount = int(input())


medias = cl.hashtag_medias_top(input_hashtag, amount=input_amount)

res = []
if(medias.__len__() > 0):
    # json_media = json.dumps(medias.__dict__, default=set_default)
    for x in medias:                
        res.append(x.model_dump(mode='json'))
    
res2 = json.dumps(res)

now = datetime.now() # current date and time

print(now)

file_name = input_hashtag + "_" + now.strftime("%m%d%Y_%H%M%S") + ".json"
with open(file_name, "w") as outfile:
    outfile.write(res2)

cl.logout()

print("Finish")

