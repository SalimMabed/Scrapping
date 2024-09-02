
#watch this video to understand the code , 
#by the way it's his code(i don't know if he stole it too) and it's well explaned
#https://youtu.be/xh28F6f-Cds?si=XHY8xStmbaLutsRA

import requests
import json

def retrieve_messages(channelid):
    headers={
        'authorization':''}
    r=requests.get(
        f'https://discord.com/api/v9/channels/{channelid}/messages', headers=headers)
    jsonn=json.loads(r.text)
    for value in jsonn:
        print(value['content'],'\n')
        
retrieve_messages('')