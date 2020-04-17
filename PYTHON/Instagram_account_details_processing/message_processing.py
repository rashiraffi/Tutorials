#!/usr/bin/env python3
import json
import os
folder_name="Conversations"
filename="messages.json"
os.mkdir(folder_name)
logs={"Chat_count":0 ,"Message_Count": 0,"Null_Count" :0,"Same_User": 0,"url":0}
with open("messages.json") as f:
    msgs=json.load(f)
for chat in msgs:
    if(len(chat["participants"]) == 1):
        logs["Null_Count"] += 1
        User_1=chat["participants"][0]
        User_2="NULL_" + str(logs["Null_Count"])
    else:
        User_1=chat["participants"][0]
        User_2=chat["participants"][1]
    filename=User_1+" & "+User_2+" .txt"
    if os.path.exists(os.path.join(folder_name,filename)):
        logs["Same_User"] += 1
        filename=User_1+" & "+User_2+"_"+str(logs["Same_User"])+" .txt"
    with open(os.path.join(folder_name,filename),"w") as chatfile:
        logs["Chat_count"] += 1
        for message in chat["conversation"]:
            if ("text" in message):
                logs["Message_Count"] += 1
                msg = str(message["sender"]) + " : " + str(message["text"]) + "\n"
                chatfile.write(msg)
            elif("media_share_url" in message):
                logs["url"] += 1
                msg = str(message["sender"]) + " : " + str(message["media_share_url"]) + "\n"
                chatfile.write(msg)
print("\n\n{} Of Chats Processed...!\n\n{} Of messages Processed..!\n\n{} Of Blocked Accounts\n\n{} Of Same\
     User Name\n\n{} Of Url Processed".format(logs["Chat_count"],logs["Message_Count"],logs["Null_Count"],logs["Same_User"],logs["url"]))