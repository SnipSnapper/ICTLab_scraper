from bs4 import BeautifulSoup
import requests

list = []
numberList = range(0, 65)
testNumber = 1



def getData():
    # check if the number is below 9 and insert the number inside of the url we are scraping
    for numbers in numberList:
        if numbers <= 9:
            url = "http://misc.hro.nl/roosterdienst/webroosters/CMI/kw3/14/r/r0000%s.htm" % numbers
        else:
            url = "http://misc.hro.nl/roosterdienst/webroosters/CMI/kw3/14/r/r000%s.htm" % numbers
        # get the url, and store the result
        source_code = requests.get(url)
        # get the text of the page and store it
        plain_text = source_code.text
        # make sure we can sort through everything. BeautifulSoup makes that available
        soup = BeautifulSoup(plain_text, "html.parser")

    #loop through the schedule
    for table in soup.findAll("table"):
        for tbody in table:
            #this is the table itself
            for tr in tbody:
                #this is every row in the table
                for td in tr:
                    #this is the column in the row
                    for table2 in td:
                        #this is the table inside of the column
                        for tbody2 in table2:
                            #this is the body of the table inside of the column
                            for tr2 in tbody2:
                                #this is the row of the table inside of the table
                                for td2 in tr2:
                                    #this is the column of the table inside of the table
                                    list.extend(td2)
    print("".join(list))






getData()

