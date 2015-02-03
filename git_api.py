API_TOKEN='******************'
GIT_API_URL='https://api.github.com'

Username = raw_input("Enter the Github Username\n")

import requests
url='https://api.github.com/users/'+Username+'/repos'
url = '%s?access_token=%s' % \
    (url,API_TOKEN)
r = requests.get(url).json()

for data in r:
	print data["full_name"]
