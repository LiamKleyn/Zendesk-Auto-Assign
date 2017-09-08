#!/usr/local/bin/python3.6

import requests
import json
import random


### This job will check for new tickets in Zendesk support, and auto assign it randomly to agents. I call it Mrs Robin!


user = 'USERNAME@COMPANY.com/token'
pwd = '*************************'

### pwd is api key, you can generate this in agent dashboard



agents = ['11111111111','2222222222', '3333333333']
# a list of agent ids, you can get these ids by making a GET request to users endpoint.




url = 'https://COMPANY.zendesk.com/api/v2/search.json?query=type%3Aticket+status%3Anew'

### 1. First, we find tickets that has a status of "new", this is when a ticket is first submitted.

response = requests.get(url, auth=(user, pwd))

# Check for HTTP codes other than 200
if response.status_code != 200:
    print('Status:', response.status_code, 'Problem with the request. Exiting.')
    exit()


data = response.json()



### 2. Then, we update that ticket, by changing the assignee ID (agent) from NULL to one of us, which triggers Zendesk to send you a custom email, telling you you have been assigned a ticket.


tickets = data['results']
if (len(tickets) != 0):   ##check if there is actual 'New' tickets in array
    for ticket in tickets:
      #print(ticket['subject'] + " ID: " + str(ticket['id']))
      id = ticket['id']
      agent = random.choice(agents)
      #print(str(id) + ' ' + agent)
      payload = {"ticket": {"assignee_id" : agent}}
      assignrequest = requests.put('https://COMPANY.zendesk.com/api/v2/tickets/' + str(id) + '.json', data = json.dumps(payload), auth=(user, pwd), headers={"Content-Type" : "application/json"})
      if assignrequest.status_code != 200:
        print('Status:', response.status_code, 'Problem with the request. Exiting.')
        exit()
      data2 = assignrequest.json()
      print(data2)
      
else:
  print("No tickets")
