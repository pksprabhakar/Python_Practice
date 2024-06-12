import requests
from bs4 import BeautifulSoup as bp

# Here i am done to retierve the gitlab profile picture
# using web scraping 
# first we need install two module 
# request module & bs4 module


# here i got username of git user
# added to git url
github_profile=input("Gitlab username :")
url="https://github.com/"+github_profile

# that url send it as get method on web url section
# if it connect status code will 200 or it will throw a error 500

r=requests.get(url) 
if r.status_code==200:  
    print("Success")
else:
    raise Exception(f"Not success:{r.status_code}")


# And we use html.parser using .content it mean 
# it reterive html content as tree format

get=bp(r.content,'html.parser')

# as i said earlier we have html tree here
# we find img tag using object identification it means 
# we reterive the object data not all that'y
deliver=get.find('img',{'class': 'avatar avatar-user width-full border color-bg-default'})

# here i retierve the img src content to got profile pic of the user
if deliver:
    img_url=deliver['src']
    print(img_url)
else:
    raise Exception (f'img is not found')