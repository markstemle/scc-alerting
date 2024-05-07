import base64
import functions_framework
from json import dumps
from httplib2 import Http
import json

# Triggered from a message on a Cloud Pub/Sub topic.
@functions_framework.cloud_event
def hello_pubsub(cloud_event):
    # Print out the data from Pub/Sub, to prove that it worked
    print(base64.b64decode(cloud_event.data["message"]["data"]))
    print("Cody was here")
    """Hangouts Chat incoming webhook quickstart."""
    url = '<URL>'
    x = base64.b64decode(cloud_event.data["message"]["data"])
    scc_load = json.loads(x)
    str_vuln_category = dumps(scc_load["finding"]["category"])
    str_finding_class = dumps(scc_load["finding"]["findingClass"])
    str_state = dumps(scc_load["finding"]["state"])

    bot_message = {
        'text': f'Finding: {str_vuln_category}, Class: {str_finding_class}, State: {str_state}'}
    message_headers = {'Content-Type': 'application/json; charset=UTF-8'}
    http_obj = Http()
    response = http_obj.request(
        uri=url,
        method='POST',
        headers=message_headers,
        body=dumps(bot_message),
    )
    print(response)
