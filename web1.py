import sys
import requests
import hashlib
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd    
from interruptingcow import timeout
import html2text

def get_soup(link):
    """
    Return the BeautifulSoup object for input link

    """
    try:
        with timeout(8, exception=RuntimeError):

            request_object = requests.get(link, auth=('user', 'pass'))
            soup = BeautifulSoup(request_object.content,"html")
            return soup,request_object
    except:

        return 'failed','failed'
   

def get_status_code(link):
    """
    Return the error code for any url
    param: link
    """
    try:
        error_code = requests.get(link).status_code
    except :
        error_code = 'fucked'
    return error_code
def LCSubStr(X, Y): 
      
    # Create a table to store lengths of 
    # longest common suffixes of substrings.  
    # Note that LCSuff[i][j] contains the  
    # length of longest common suffix of  
    # X[0...i-1] and Y[0...j-1]. The first 
    # row and first column entries have no 
    # logical meaning, they are used only 
    # for simplicity of the program. 
      
    # LCSuff is the table with zero  
    # value initially in each cell 
    LCSuff = [[0 for k in range(len(Y)+1)] for l in range(len(X)+1)] 
      
    # To store the length of  
    # longest common substring 
    result = 0 
  
    # Following steps to build 
    # LCSuff[m+1][n+1] in bottom up fashion 
    for i in range(len(X) + 1): 
        for j in range(len(Y) + 1): 
            if (i == 0 or j == 0): 
                LCSuff[i][j] = 0
            elif (X[i-1] == Y[j-1]): 
                LCSuff[i][j] = LCSuff[i-1][j-1] + 1
                result = max(result, LCSuff[i][j]) 
            else: 
                LCSuff[i][j] = 0
    print()
    return result 

def longestSubstringFinder(string1, string2):
    answer = ""
    len1, len2 = len(string1), len(string2)
    for i in range(len1):
        match = ""
        for j in range(len2):
            if (i + j < len1 and string1[i + j] == string2[j]):
                match += string2[j]
            else:
                if (len(match) > len(answer)): answer = match
                match = ""
    return answer
def find_internal_urls(lufthansa_url, depth, max_depth):
    
    if "http" not  in lufthansa_url:
        return {}, ['www'],[]
    
    print(depth)
    i = 0 
    addto =[]
    print(lufthansa_url)
    
    if lufthansa_url == 'failed':
        return {}, ['failed from failed'],[]


    if ".pdf" in lufthansa_url:
        return {}, ['failed from pdf'],[]
    if ".jpg" in lufthansa_url:
        return {}, ['failed from jpg'],[]
    if "@" in lufthansa_url:
        return {}, ['failed from @'],[]
    if ".mp4" in lufthansa_url:
        return {}, ['mp4 failed'],[]
    if ".mov" in lufthansa_url:
        return {}, ['mov failed'],[]
    if ".avi" in lufthansa_url:
        return {}, ['avi failed'],[]
    if ".gz" in lufthansa_url:
        return {}, ['gz failed'],[]
    if ".ps" in lufthansa_url:
        return {}, ['ps failed'],[]
    if ".zip" in lufthansa_url:
        return {}, ['ps zip'],[]
    if ".png" in lufthansa_url:
        return {}, ['ps zip'],[]
    if ".pptx" in lufthansa_url:
        return {}, ['ps zip'],[]
    if ".txt" in lufthansa_url:
        return {}, ['ps zip'],[]
    if ".ps" in lufthansa_url:
        return {}, ['ps zip'],[]
    if ".mp3" in lufthansa_url:
        return {}, ['ps zip'],[]
    if "facebook" in lufthansa_url:
        return {}, ['ps zip'],[]
    if "linkedin" in lufthansa_url:
        return {}, ['ps zip'],[]
    if "twitter" in  lufthansa_url:
        return {}, ['ps zip'],[]
    if "youtube"in  lufthansa_url:
        return {}, ['ps zip'],[]
    if "instgram"in  lufthansa_url:
        return {}, ['ps zip'],[]
    if ".html#"in  lufthansa_url:
        return {}, ['ps zip'],[]


    all_urls_info = []
    wahaha = []
    status_dict = {}
    soup,request_object = get_soup(lufthansa_url)
    dep = lufthansa_url.rfind('/')
    dep += 1
    checkcourse = ['midterm', 'Midterm', 'instructor','Instructor','Textbook','textbook','Grade','grade','Instructors','TAs ','Exams ','HW','Prerequisites','Instructor']
    if soup == 'failed':
        return {}, ['failed from soup'],[]
    check = False
    try:
        html = html2text.html2text(request_object.text)
    except:
        return {}, ['ps zip'],[]

    if (depth >=3):
        for i in checkcourse:
            if i in html:
                check = True
                print(i)
                break

        if(check):
            addto.append(lufthansa_url)
            print(addto)
       # return {}, ['www'],addto
            return {}, ['www'],addto


    a_tags = soup.findAll("a", href=True)
    for a_tag in a_tags:
        try:

        
            if len(a_tag["href"]) <=2:
                continue

            if (("https" not in a_tag["href"]) and("http" not in a_tag["href"] )):
                if 'www' not in a_tag["href"]:
                    
                    c =  LCSubStr(lufthansa_url, a_tag["href"])
                    if c <= 2:
                        c =0
                        url = lufthansa_url[:len(lufthansa_url)-c]+a_tag["href"]
                       # print(url)


                    else:
                        word = longestSubstringFinder(lufthansa_url,a_tag["href"])
                        e = lufthansa_url.find(word)
                        f = a_tag.find(word)
                        url = lufthansa_url[:e] + a_tag[f:]
                        print(url)
                    
                '''
                if "dal" not in a_tag["href"]:
                    url = 'https://www.uoguelph.ca' + a_tag['href'] 
                    print(url)
                
                else:
                

                    if '/'  == a_tag['href'][0]:
                        url = lufthansa_url[:dep-1]  + a_tag['href'] 
                    else:
                        url =  lufthansa_url[:dep] + a_tag['href'] 
                '''


            elif (("https" in a_tag["href"]) or ("http"  in a_tag["href"] )):
                url = a_tag['href']

            elif "login" in a_tag["href"]:
                continue

            else:
                print('failed')
                continue

            if depth == 1:
               # if "directory-detail-g.aspx?" not in url:  psu
               #if "k-Teacher" not in url:  stanford

                if"~"not in url:
                    print('dd')
                    continue




            elif depth == 2:
                if"course"not in url:
                    if"teach" not in url:
                        print('dd')
                        continue

            
            elif depth >= 3:

                if"~"not in url:
                    print('dd')
                    continue





            

            
            wahaha.append(url)
    

           

        except:
            continue
    return all_urls_info, wahaha,[]

if __name__ == "__main__":
    depth = 1 # suppose 
    haha = []
    haha1 =[]
    haha2 = []
    xiong = []
    xiong1= []
    all_page_urls1, haha1,xiong = find_internal_urls("http://web.cs.toronto.edu/people/faculty.htm", 1, 6)
    depth +=1
    haha += haha1
    haha2 += haha1
    haha3 =[]
    xiong1+= xiong
    while depth < 5: 
        for status_dict in haha2:
           all_page_urls, haha1,xiong =  find_internal_urls(status_dict,depth, 5)
           xiong1 += xiong
         #  print(haha1,'this is haha1')
           for i in haha1:
                if i not in haha:
                    haha.append(i)
                    haha3.append(i)
         #  print(haha1 , '    this is haha11111')
          # print(haha3,'    this is haha333333')
        #print(haha1)
       # print('end hahahahaahahahahhhhhhhh')
        haha2 = []
        haha2 += haha3
       # print(haha3)
        #print(haha2)
        haha3 = []
        depth += 1
        print(depth)
    df = pd.DataFrame(xiong1, columns=["colummn"])
    df.to_csv('toronto.csv', index=False)




