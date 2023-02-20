import requests
import datetime

error = True
while error:
    url = input("Write a url of your choice or press ENTER for the default (http://python.org/):\n")

    if url == '':
        url = "http://python.org/"
    try:
        with requests.get(url) as response:
            print("\nHeaders for: " + url)
            for header in response.headers:
                print(header + ":", response.headers[header])
            print("\nThe software used by the server is: " + response.headers['Server'])
            if response.cookies.get_dict() == {}:
                print("\nThe website with url: '" + url + "' has no cookies")
            else:
                print("\nCookies for: " + url)
                for cookie in response.cookies:
                    timestamp = datetime.datetime.fromtimestamp(cookie.expires)
                    print("cookie name: {:20s}".format(cookie.name), end='')
                    print("is valid until:", timestamp.strftime('%d-%m-%Y %H:%M:%S'))
        error = False
        
    except Exception as e:
        url = input("Write a url of your choice or press ENTER for the default (http://python.org/):\n")
        
