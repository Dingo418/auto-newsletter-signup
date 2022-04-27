import requests
import database as d
import globals as g

def main():
    #repeats for the whole list
    for i in range(0, len(d.data.keys())):
        data = d.data[i]
        if data.get("type") == 1:
            print("type 1")
            push = requests.get(url=data.get("url"), params=data.get("payload"))
            print(f"{g.email} was succesfully subscribed to {data.get('name')} Newsletter")
            print(push.text)
        elif data.get("type") == 2:
            print("type 2")
            push = requests.post(url=data.get("url"), data=data.get("payload"))
            print(push.text)
            print(f"{g.email} was succesfully subscribed to {data.get('name')} Newsletter")
        elif data.get("type") == 3:
            print("3")
            break
        else: 
            print("error")

if __name__ == "__main__":
    main()