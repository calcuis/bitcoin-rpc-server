import requests
import json

rpc_user = 'your_rpc_username'
rpc_password = 'your_rpc_password'
url = 'http://127.0.0.1:8332/'

headers = {'content-type': 'application/json'}
payload = json.dumps({
    "method": "getblockchaininfo",
    "params": [],
    "jsonrpc": "1.0",
    "id": "python"
})

response = requests.post(url, headers=headers, data=payload, auth=(rpc_user, rpc_password))
print(response.json())
