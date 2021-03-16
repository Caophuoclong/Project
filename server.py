from flask import Flask, render_template, request, url_for
import json
import requests
my_token = "26032001"
app = Flask(__name__)        

@app.route("/")
def index():
    return "Long"
@app.route('/webhooks', methods=["GET","POST"])
def handle_message():
    '''
    Handle messages sent by facebook messenger to the applicaiton
    '''
    if request.method == "GET":
        if request.args.get("hub.verify_token") == my_token:
            return request.args.get("hub.challenge")
    elif request.method == "POST":
        data = request.get_json()
        if data["object"] == "page":
            for entry in data["entry"]:
                for messaging_event in entry["messaging"]:
                    if messaging_event.get("message"):
                        sender_id = messaging_event["sender"]["id"]
                        recipient_id = messaging_event["recipient"]["id"]  
                        message_text = messaging_event["message"]["text"]
                        print(message_text)
                        sendmessage(sender_id,"Long dep trai")  
        return "ok"

def sendmessage(sender_id,message_text):
    token_access = "EAAHPTZBQbRLABAAi5UKcZA0WxPAPmTI0cjiQBiRRtt5fFTR4S0Dyex8QrFXWuJAZBSL8nnPA3a8ZBkOhuIOjyIaOiVOL2Pcx4JNC15PXgz17R8RnnCrC8wzDtW0cga6M7AjaPdZC0xTbLIisvjZATGsvw65v6kJSZA9kTgcp5Kgskqy8Kk4O1fz"
    url = "https://graph.facebook.com/v2.6/me/messages"
    x = requests.request("POST",url,
    params={"access_token" : token_access},
    headers={"Content-Type": "application/json"},
     data=json.dumps({
        "recipient": {"id": sender_id},
        "message": {"text": message_text}}))




if __name__ == "__main__":
    app.run()
