from selenium import webdriver
import os
import numpy as np

import time

def merriam_webster(browser,word):
    """#Setting browser
    chrome_options = webdriver.ChromeOptions()
    #To hide chrome comment out the following line 
    #chrome_options.add_argument('--headless')
    browser = webdriver.Chrome(os.path.abspath(os.curdir)+'/chromedriver 78',options=chrome_options)"""

    new_clues = list()

    try:
        browser.get('https://www.merriam-webster.com/')
        browser.find_elements_by_xpath('//*[@id=\"s-term\"]')[0].send_keys(word)
        browser.find_element_by_xpath("//*[@id=\"mw-search-frm\"]/div[1]/div[2]").click()
        new_clues = list(browser.find_element_by_xpath("//*[@id=\"dictionary-entry-1\"]").text.splitlines()[1:])
        #Kafa Açıyo
        """try:
            new_clues += browser.find_element_by_xpath("//*[@id=\"examples-anchor\"]/div").text.splitlines()[1:]           
        except:
            print("No sentence example")"""
        try:
            new_clues += browser.find_element_by_xpath("//*[@id=\"etymology-anchor\"]").text.splitlines()[1:]
        except:
            print("No history and etymology info")
    except:
        print("Exception")
        return False


    print(new_clues)

    for i in range(len(new_clues)-1,-1,-1):
        if new_clues[i][0]=="—" and i!=0:
            new_clues.remove(new_clues[i])
        elif new_clues[i][0].isdigit()==True :
            new_clues.remove(new_clues[i])
        elif len(new_clues[i])==1 :
            new_clues.remove(new_clues[i])

    for i in range(len(new_clues)):
        if new_clues[i][0]==":":
            new_clues[i] = new_clues[i][1:]
        new_clues[i] = new_clues[i].replace(":",". ")
    
    for i in range(len(new_clues)):
        new_clues[i] = new_clues[i].lower().replace(word.lower(),"_"*len(word))
        
    
    
    #print(new_clues)
    return new_clues


