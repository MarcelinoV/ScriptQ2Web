import requests

api_endpt = 'https://pastebin.com/api/api_post.php' # URL where POST request is sent
api_key = '3ae9f18ac5db686bb577ad9987fc2282' # API Developer key

file = open("testfile.txt", "r") # function to open text file in program
source = file.read() # function to print text file

data = { # keys & parameters required to post through API
    'api_dev_key': api_key,
    'api_option': 'paste',
    'api_paste_code': source,
    'api_paste_format': 'python'
}

r = requests.post(url=api_endpt, data=data) # post request & saving of response

pastebin_url = r.text # extracting response text
print("The pastebin URL is: {}".format(pastebin_url))

