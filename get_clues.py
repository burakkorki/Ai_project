from selenium import webdriver
import os
import numpy as np
import textwrap
import time
import wikipedia
import time
import nltk as ntlk
from nltk.corpus import wordnet

def clear(sentence, word):
    if word in sentence:  # see if one of the words in the sentence is the word we want
        replaced = sentence.replace(word, "____")
        #print(replaced)



def word_hippo(word):

    chrome_options = webdriver.ChromeOptions()
    browser = webdriver.Chrome(os.path.abspath(os.curdir)+'/chromedriver 78',options=chrome_options)

    new_clues = list()

    try:
        browser.get('https://www.wordhippo.com/what-is/sentences-with-the-word/' + word + '.html')
        sentence = browser.find_element_by_xpath("/html/body/div[3]/table/tbody/tr[2]/td/table/tbody/tr/td/div/table/tbody/tr[1]/td[2]/div/table/tbody/tr/td/div[2]/table/tbody/tr[2]").text.splitlines()
    except:
        print("No solution in word hippo")
        return False

    clear(sentence[0], word)
    return sentence



def wiki(word):

    try:
        results_of_search = wikipedia.search(word)
    

        if("disam" in results_of_search[0] or len(results_of_search)>1):
            first_result = wikipedia.summary(results_of_search[1], sentences=1)
        else:
            first_result = wikipedia.summary(results_of_search[0], sentences=1)

    except:
        print("No solution in wikipedia")
        return False

    first_result = first_result.lower()
    word = word.lower()
    first_result = first_result.replace(word, "____")
    return first_result


def anagram(browser,word):
    #Setting browser
    #chrome_options = webdriver.ChromeOptions()
    #To hide chrome comment out the following line
    #chrome_options.add_argument('--headless')
    #browser = webdriver.Chrome(os.path.abspath(os.curdir)+'/chromedriver79',options=chrome_options)

    browser.get('https://ingesanagram.appspot.com')
    browser.find_element_by_xpath("/html/body/div/div/div[1]/div[1]/div/div[2]/div/input").send_keys(word)
    browser.find_element_by_xpath("/html/body/div/div/div[1]/div[1]/div/div[3]/div[1]/button").click()
    time.sleep(2)
    clues = browser.find_element_by_xpath("/html/body/div/div/div[1]/div[3]/div").text.splitlines()
    print (clues)




def findIndex(word, list):

    for element in list:
        if(word in element):
            return list.index(element)

    return -1

def anagramSmith(browser,word):

    #Setting browser
    #chrome_options = webdriver.ChromeOptions()
    #To hide chrome comment out the following line
    #chrome_options.add_argument('--headless')
    #browser = webdriver.Chrome(os.path.abspath(os.curdir)+'/chromedriver 78',options=chrome_options)

    try:
        browser.get('https://new.wordsmith.org/anagram/anagram.cgi?anagram=' + word)
        #browser.find_element_by_xpath("/html/body/topbar/blockquote/form/table/tbody/tr[1]/td[1]/input").send_keys(word)
        #browser.find_element_by_xpath("/html/body/topbar/blockquote/div/div").click()
        clues = browser.find_element_by_xpath("/html/body/topbar/blockquote/div").text.splitlines()

    except:
        print("No solution in anagram smith")
        return False

    #finds the position of Displaying elements label
    index = findIndex("Displaying", clues)

    #prints out the first element after displaying label on page
    return "Anagram of " +  word + " is " + clues[index+1].lower()


def wordnetFunction(clue):
    for word in clue:
        synset = wordnet.synsets(word)
        if(len(synset) != 0):
            print('Word and Type : ' + synset[0].name())
            print('Synonym of ' + word + ' is: ' + synset[0].lemmas()[0].name())
            print('The meaning of the word : ' + synset[0].definition())
            print('Example of ' + word + ' : ' + str(synset[0].examples()))


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
        try:
            indexof2 = new_clues.index("2")
            new_clues = new_clues[:indexof2]           
        except:
            a = 0
            #print("No 2")
        """try:
            new_clues += browser.find_element_by_xpath("//*[@id=\"etymology-anchor\"]").text.splitlines()[1:]
        except:
            print("No history and etymology info")"""
    except:
        print("No solution in marrian webster")
        return False


    #print(new_clues)

    for i in range(len(new_clues)-1,-1,-1):
        """if new_clues[i][0]=="—" and i!=0:
            new_clues.remove(new_clues[i])
        el"""
        if new_clues[i][0].isdigit()==True :
            new_clues.remove(new_clues[i])
        elif len(new_clues[i])==1 :
            new_clues.remove(new_clues[i])

    for i in range(len(new_clues)):
        if new_clues[i][0]==":" or new_clues[i][0]=="—":
            new_clues[i] = new_clues[i][1:]
        new_clues[i] = new_clues[i].replace(":",". ")
    
    for i in range(len(new_clues)):
        new_clues[i] = new_clues[i].lower().replace(word.lower(),"_"*len(word))
        
    
    
    #print(new_clues)
    return textwrap.fill('. '.join(map(str, new_clues)),50)


# Test cases

#print(word_hippo("hou"))
#print(wiki("justin"))
#print(anagramSmith("ubers"))
#wordnetFunction("dog")




"""#Finding new clues for accross solutions
browser.get('https://www.wordplays.com/crossword-clues')
for i in range(0,len(accross_solution),2):
    browser.get('https://www.wordplays.com/crossword-clues')
    browser.find_element_by_xpath("/html/body/div[1]/div[3]/div[3]/div[1]/form/div/table/tbody/tr[3]/td/input").send_keys(accross_solution[i+1])
    browser.find_element_by_xpath("//*[@id=\"search\"]").click()
    print("Clues getting for: ",accross_solution[i+1])
    new_clues_accross.append(accross_solution[i])
    new_clues_accross.append(browser.find_element_by_xpath("//*[@id=\"wordlists\"]").text.splitlines()[2:])
    print(len(new_clues_accross[i+1])," new clues are found")


#Finding new clues for down solutions

for i in range(0,len(down_solution),2):
    browser.get('https://www.wordplays.com/crossword-clues')
    browser.find_element_by_xpath("/html/body/div[1]/div[3]/div[3]/div[1]/form/div/table/tbody/tr[3]/td/input").send_keys(down_solution[i+1])
    browser.find_element_by_xpath("//*[@id=\"search\"]").click()
    print("Clues getting for: ",down_solution[i+1])
    new_clues_down.append(down_solution[i])
    new_clues_down.append(browser.find_element_by_xpath("//*[@id=\"wordlists\"]").text.splitlines()[2:])
    print(len(new_clues_down[i+1])," new clues are found")"""
