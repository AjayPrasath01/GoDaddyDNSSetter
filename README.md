# GoDaddyDNSSetter
The above python code can be used to set dns in godaddy. 

Most of the ISP accross the India provide DDNS (Dynamic DNS) for their customers. That means your DNS change when there no useage of internet or during reboot 
of the router. If the IP changed, then Domians linked to the IP can't find the server with the old IP. 

To fix this issue some domin provider have some application some provide API. Here in GoDaddy they provid us API to set our new Ip with our domain.

To retrive domain details such as ttl, data.
https://api.godaddy.com/v1/domains/your/records/type-to-bechanged/name

Above must be a get request along with the key and value included in header as Authorization

To update data we must set a PUT or PATCH request to below url with the correct detalis
https://api.godaddy.com/v1/domains/your/records/type-to-bechanged/name

The above code does the required get and put calls as sets the data dor you. 

You use cron sevice so that the above script will be called at specified time. 
In GoDaddy they suggest  time period of 10min that is 600 seconds and the cron for it is as follow
*/10 * * * * /path/python-script.py

If your using a ubuntu server the command is
-> crontab -e 
this will as you to select a editor go with what you are confortable with
-> */10 * * * * "/path/python-script.py" enter correct details and save the file

make sure that cron is running 
The command to check the status is 
systemctl status cron

