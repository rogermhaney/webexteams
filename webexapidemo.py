from flask import Flask, render_template, request, redirect
import json
import requests

app = Flask(__name__)
app.debug=True

access_token = "N2JjODhmYzYtOWQ1NS00YWEwLTk4N2EtYzExODhjNDdlZTUxN2Y2MzUxMjAtNTI5_PF84_e022b5d5-fdca-4b8a-9d1c-1f7f4d958cd7"
newRoomId = " "

def makearoom(nameofroom):
    url = 'https://api.ciscospark.com/v1/rooms'
    headers = {
        "Authorization": "Bearer " + access_token,
        "Content-Type": "application/json"
        }
    payload = {
        "title": nameofroom
        }
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    roomId = response.json()['id']
    print(response.json())
    print("In Function: ", roomId)
    return (roomId)

def listrooms():
    url = 'https://api.ciscospark.com/v1/rooms'
    headers = {
	    "Authorization": "Bearer " + access_token,
	    "Content-Type": "application/json"
	    }
    queryParams = {
	    "sortBy" : "lastactivity", 
        "max" : "5"
	    }
    response = requests.get(url, headers=headers, params=queryParams)
    print(response)

def sendamessage(theRoomId, theMessage):
    url = 'https://api.ciscospark.com/v1/messages'
    headers = {
	    "Authorization": "Bearer " + access_token,
	    "Content-Type": "application/json"
	    }
    payload = {
	    "roomId": theRoomId,
        "text" : theMessage
	    }
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    print(response)

def adduser(nameofmember, aRoomId):
    url = 'https://api.ciscospark.com/v1/memberships'
    headers = {
    	"Authorization": "Bearer " + access_token,
    	"Content-Type": "application/json"
    	}
    payload = {
	    "roomId": aRoomId,
	    "personEmail": nameofmember
	    }
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    print(response.json())

def getauser():
    url = 'https://api.ciscospark.com/v1/memberships'
    headers = {
    	"Authorization": "Bearer " + access_token,
    	"Content-Type": "application/json"
    	}
    queryParams = {
    	"sortBy" : "lastactivity", 
        "max" : "5",
    	"roomId" : newRoomId
    	}
    response = requests.get(url, headers=headers, params=queryParams)
    print(response.json())

@app.route('/home', methods=['GET', 'POST'])
def hello_world():

    if request.method == 'POST':
        roomname = request.form['teamsroomname']
        membername = request.form['membername']
        messagetosend = request.form['themessage']
        print(roomname, membername, messagetosend)

        if roomname != "":
            global newRoomId
            newRoomId = makearoom(roomname)
            print("In Post: ", newRoomId)
            return render_template('makeroom.html')
        

        if membername != "":
            print("In Post: ", membername)
            print("In Post: ", newRoomId)
            adduser(membername, newRoomId)
            return render_template('addmember.html')
        
        if messagetosend != "":
            sendamessage(newRoomId, messagetosend)
            messagetosend = ""
            return render_template('sendamsg.html')

    return render_template('home.html')

@app.route('/makeroom', methods=['GET', 'POST'])
def makeroom():
    return render_template('makeroom.html')

@app.route('/addmember', methods=['GET', 'POST'])
def addmember():
    return render_template('addmember.html')

@app.route('/sendamsg', methods=['GET', 'POST'])
def sendamsg():
    return render_template('sendamsg.html')