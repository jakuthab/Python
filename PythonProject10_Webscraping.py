import pandas as pd
import requests
import http.cookiejar as cookielib
import os
from bs4 import BeautifulSoup

credly_endpoint = "https://mqgrmeiggk.execute-api.us-east-2.amazonaws.com/credly/badges?email={}@amazon.com"

def requests_get(url):
    home_dir = os.path.expanduser("~")
    cookie_file = os.path.join(home_dir, ".midway/cookie")
    cookies = cookielib.MozillaCookieJar(cookie_file)
    cookies.load()
	
    session = requests.Session()
    session.cookies.update(cookies)
	
    return session.get(url)

def fetch_data(filepath):
    my_aliases = pd.read_csv(filepath, index_col=False)
    return my_aliases

def fetch_credlyinfo(alias):
    alias_value = alias.values[0]
    credly_response = requests.get(credly_endpoint.format(alias_value))
    return credly_response

def main():
    #aliases = fetch_data("aliases.csv")
    #credly_response = fetch_credlyinfo(aliases.values[0])
    aliases = []

    # run for as we get aliases
    stop_now = False
    i = 1
    while(stop_now is False):
        url = 'https://permissions.amazon.com/group.mhtml?target=11899453&page={}'.format(i)
        response = requests_get(url)
        print(response)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        for td in soup.find_all('td'):
            link = td.find('a')
            if link and 'user.mhtml?lookup_user=' in str(link.get('href')):
                if link.text != '':
                    print(link.text)
                    aliases.append(link.text)
            else:
                stop_now = True
        
        i = i+1
        


    print(len(aliases))
    # Write to a file
    # with open('output.txt', 'w') as file:
    # file.write(response.text)
    


if __name__ == "__main__":
    main()
