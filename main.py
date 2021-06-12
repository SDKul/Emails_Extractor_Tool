#Importing the required libaries
import requests
import re

url_list =["https://gtlsoftwares.com/" ,"https://www.intellectsoft.net/"] #URL used to extract emails from this website
EMAIL =r"[\w\.-]+@[\w\.-]+"  #email regular expression


for url in url_list:#For Iterating url in List of url 

    print(f"For This {url} following is Result:\n")

    r = requests.get(url)#Connecting to website

    #Storing Result for Each URL in Text file:
    with open("email.txt","a") as file:
        file.write(f"Result Fetched For url is:{url}\n")

    for re_match in re.findall(EMAIL,r.text): #for finding the emails 

        #Search Result in Text file to avoid duplicates enteries:
        with open("email.txt","r") as file:
            contentent =file.read()
        if re_match in contentent:
            continue
        else:
            with open("email.txt","a") as file:  #stored fetched results in email.txt
                file.write(f"{re_match} \n")

        print(re_match)  #Showning Results

            


          
    




   
