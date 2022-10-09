# Chanong DNS to current ip in godaddy
import json
import logging

import requests

# To be changed with your values

DOMAIN = "Your domain"
KEY = "Your API Key"
VALUE = "Your api secret key"
TYPE = "A"
NAMES = ["@"]

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(levelname)s %(message)s",
                    filemode="w")


def response_handler(reponse: requests.Response) -> bool:
    """
    :param reponse: Response of the request
    :return: Boolean
    """
    if reponse.status_code == 200:
        return True
    elif response.status_code == 401:
        logging.critical("Authorization is wrong")
        return False
    elif response.status_code == 404:
        logging.critical("Page Not found")
        return False
    return False


if __name__ == '__main__':
    current_ip = requests.get("https://ipinfo.io/ip").content.decode("utf-8")
    logging.debug("Current Ip : " + current_ip)

    headers = {"Authorization": f"sso-key {KEY}:{VALUE}", "Content-Type": "application/json",
               "Accept": "application/json"}
    for NAME in NAMES:
        response = requests.get(f"https://api.godaddy.com/v1/domains/{DOMAIN}/records/{TYPE}/{NAME}", headers=headers)
        logging.debug("Response Raw : " + str(response))
        if response_handler(response):
            response = json.loads(response.content.decode("utf-8"))[0]
            logging.debug("Response Content : " + str(response))
            logging.debug("DNS IP : " + response['data'])
            if response['data'] != current_ip:
                data = [{"data": current_ip, "ttl": response["ttl"]}]
                logging.debug("Body : " + str(data))
                logging.debug("Chaning DNS ip for " + NAME)
                res = requests.put(f"https://api.godaddy.com/v1/domains/{DOMAIN}/records/{TYPE}/{NAME}",
                                   headers=headers,
                                   data=json.dumps(data))
                print("Should be changed for " + NAME)
                logging.debug("DNS is changing")
            else:
                logging.debug("IPs are same for " + NAME)
                print("IPs are same for " + NAME)
