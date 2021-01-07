import base64
import requests
import datetime

# grab from Spotify Developers dashboard
client_id = '0b2811caa398417098072a32295d8652'

client_secret = 'f8751bc9c2d843f3b7c19c727aa1cea6'


client_creds = f"{client_id}:{client_secret}"
# converting client_creds to b64 encoding
client_creds_b64 = base64.b64encode(client_creds.encode())

# Required spotify API parameters

# endpoint
method = 'POST'
token_url = 'https://accounts.spotify.com/api/token'

# body
token_data = {
    "grant_type": "client_credentials"
}
# header
token_headers = {
    "Authorization": f"Basic {client_creds_b64.decode()}"
}

# finalized request call
r = requests.post(token_url, data=token_data, headers=token_headers)

print(r.json())
valid_request = r.status_code in range(200, 299)
token_response_data = r.json()

# save access token json object to variable
access_token = token_response_data['access_token']

# expiration check
now = datetime.datetime.now()
expires_in = token_response_data['expires_in']  # in seconds
expires = now + datetime.timedelta(seconds=expires_in)
did_expire = expires < now
print(did_expire)
