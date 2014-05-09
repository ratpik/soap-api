'''
from suds.client import Client

import logging
logging.basicConfig(level=logging.INFO)
logging.getLogger('suds.client').setLevel(logging.DEBUG)
logging.getLogger('suds.transport').setLevel(logging.DEBUG)

wsdl_url = "http://localhost:8002/notification.wsdl"

client = Client(wsdl_url)
'''

from flask import Flask, request, Response
app = Flask(__name__)


soap_mimetype = "application/soap+xml"

NOTIFICATION_RESPONSE_XML = """
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
xmlns:xsd="http://www.w3.org/2001/XMLSchema"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
<soapenv:Body>
<notificationToCPResponse xmlns="http://SubscriptionEngine.ibm.com"/>
</soapenv:Body>
</soapenv:Envelope>

"""


@app.route("/notification", methods=['GET', 'POST'])
def handle_notification():
    if request.method == 'POST':
        #TODO: Parse the XML in the request body
        #print request.data
        return Response(NOTIFICATION_RESPONSE_XML, mimetype=soap_mimetype)
    else:
        return NOTIFICATION_RESPONSE_XML

if __name__ == "__main__":
    app.run()


