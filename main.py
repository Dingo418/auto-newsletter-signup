import requests
import database as d
import globals as g

def main():
    #repeats for the whole list
    for i in range(0, len(d.data.keys())):
        data = d.data[i]
        if data.get("type") == "get":
            print("get")
            push = requests.get(url=data.get("url"), params=data.get("payload"))
            print(f"{g.email} was succesfully subscribed to {data.get('name')} Newsletter")
            print(push.text)
        elif data.get("post") == 2:
            print("post")
            push = requests.post(url=data.get("url"), data=data.get("payload"))
            print(push.text)
            print(f"{g.email} was succesfully subscribed to {data.get('name')} Newsletter")
        elif data.get("post_json") == 3:
            print("post_json")
            break
        else: 
            print("error, no type listed ")

if __name__ == "__main__":
    main()