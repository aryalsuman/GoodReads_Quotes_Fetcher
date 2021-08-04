import requests,re
from bs4 import BeautifulSoup
def remove_all_spaces(string):
    return " ".join(string.split())
website=input("Enter Url:")
page=input("Enter Page:")
for i in range(1,int(page)+1):    
    urls=website+"?page="+str(i)
    html_doc = requests.get(urls)
    # print(r.text)
    soup = BeautifulSoup(html_doc.text, 'lxml')
    # print(soup.prettify())
    # mydivs = soup.find("div", {"class": "quoteText"})
    # print(mydivs.content)

    quo=soup.get_text()
    quo=remove_all_spaces(quo)
    # print(quo)
    regex=re.compile(' \“(.*)\” ― (.*) tags')
    quotes=regex.findall(quo)
    quotes2=re.sub('tags:.*?Like '," ",str(quotes))
    quotes2=quotes2.replace('\\',"")
    print(quotes2)

    q=False
    d=False
    for quote in str(quotes2):
        if quote =='“':
            # file1.write('''{"text:"''')
            print('''"\n},\n{\n"text": ''',end="")
            q=True
            d=False
        if q== True:
            # file1.write(quote)
            print(quote,end="")
            if quote=='”':
                q=False
        if quote   == '―':
            # file1.write('''\n"author:"''')
            print(',\n"author":"',end="")
            d=True
        if d==True:
            # file1.write(quote)
            print(quote,end="")

    
    
    
