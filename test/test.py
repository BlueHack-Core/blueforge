from blueforge.apis.facebook import CreateFacebookApiClient
from blueforge.apis.facebook.message import RequestDataFormat, Recipient, Message

client = CreateFacebookApiClient(
    access_token='EAACCjNQkVwoBAEnHNQbl2xLG5935vSVX8kSsBUTFzYFnB62ZCvZCZCIZCUZAcY9ZCBliQpoUiaMo0uesVct0FkDAHgsxXWjPTZCZC7dZAnhO0kalcN7NtJkuHnelMiHe5O8UAYkQQbDUCPaBShRHl25mG6fCIhm1bBFEt70k21qswZAHTuK4ryGpnr')

recipient = Recipient(recipient_id='1053565541409779')
message = Message(text='Hard Study')
final_message = RequestDataFormat(recipient=recipient, message=message)
print(client.send_message(final_message))
