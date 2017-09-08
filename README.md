# Zendesk-Auto-Assign
This is a python script which you can connect to Zendesk, to randomly auto assign tickets. This is a feature that Zendesk does not have. It is sometimes called round robin assignment.


# Installation

#### Step 1. Get API key from Zendesk
- Go to Settings in Zendesk
- Select Channels > API
- Enable Token Access and get your key
- Select Save

> NB: Keep this key somewhere safe, you will insert this into script later.

#### Step 2.

Modify autoassign.py's following fields

- user - This is your Zendesk username
- pwd - Your API key
 - On line 24, change company.zendesk.com... to match yours.
 - Same thing on Line 51 as above.

 #### Step 3. 
 
 Save autoassign in your scripts directory. This can be anywhere, I reccommend putting iton a server that is always running. Mine is in /root/scr/autoassign.py
 
 #### Step 4. 
 
 Add script to crontab, so it will run every 5 minutes (or whatever you specify).
 
 I added this to my crontab file, */5 meaning EVERY 5 minutes.
 
 ```
 */5 * * * * root /root/scr/autoassign.py
 ```
 
 #### Step 5.
 
 You want your agents to know that they have been randomly assigned a ticket. To do this, we can make a trigger in Zendesk. The trigger's condition will be (Assignee changed), and the action will be to mail the new assignee.
 
 - Go to settings, Business Rules, Triggers.
 - On the top right, click add trigger
 - Enter any name, I named mine Assigned API, also enter a desc so you know what the trigger is doing.
 - Conditon is: Asignee -> Changed
 - Action is: Email user -> (assignee)
 
 
#### Step 6. 

Test by submitting a few test tickets and see if it is randomly assigning them.

Voila!

Let me know if you need any help. I was looking for something like this, and couldn't find any. I still can't believe Zendesk does not have a random auto assign feature!


>Liam Kleyn
>www.liamkleyn.co.za
>info@liamkleyn.co.za
 



  
