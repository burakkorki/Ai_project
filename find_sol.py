from selenium import webdriver
import os
import numpy as np
from get_clues import *
from operator import itemgetter
import time
chrome_options = webdriver.ChromeOptions()

#To hide chrome comment out the following line 
#chrome_options.add_argument('--headless')
browser = webdriver.Chrome(os.path.abspath(os.curdir)+'/chrome_driver/chromedriver 78',options=chrome_options)

username = ""
password = ""
#Log in
browser.get('https://www.nytimes.com/crosswords/game/mini')
browser.find_element_by_xpath("//*[@id=\"root\"]/div/div/div[1]/header/div[3]/div/a[5]").click()
browser.find_element_by_xpath("//*[@id=\"username\"]").send_keys(username)
browser.find_element_by_xpath("//*[@id=\"password\"]").send_keys(password)
browser.find_element_by_xpath("//*[@id=\"myAccountAuth\"]/div[1]/div/form/div/div[5]/button").click()
time.sleep(30)
browser.get('https://www.nytimes.com/crosswords/game/mini/2019/12/12')

try:
    browser.find_elements_by_xpath('//*[@id="root"]/div/div/div[4]/div/main/div[2]/div/div[2]/div[3]/div/article/div[2]/button/div/span')[0].click()
    browser.find_elements_by_xpath('//*[@id="root"]/div/div/div[4]/div/main/div[2]/div/div/ul/div[2]/li[2]/button')[0].click()
    browser.find_elements_by_xpath('//*[@id="root"]/div/div/div[4]/div/main/div[2]/div/div/ul/div[2]/li[2]/ul/li[3]/a')[0].click()
    browser.find_elements_by_xpath('//*[@id="root"]/div/div[2]/div[2]/article/div[2]/button[2]/div/span')[0].click()
    browser.find_elements_by_xpath('//*[@id="root"]/div/div[2]/div[2]/span')[0].click()
except:
    print("Already revealed")
try:
    today = browser.find_element_by_xpath("//*[@id=\"root\"]/div/div/div[4]/div/main/div[2]/header/div/div/div/div[1]").text
except:
    browser.quit()
clues_across = list()
clues_down = list()

clues_across = browser.find_elements_by_xpath('//*[@id="root"]/div/div/div[4]/div/main/div[2]/div/article/section[2]/div[1]/ol')[0].text.split('\n')
clues_down = browser.find_elements_by_xpath('//*[@id="root"]/div/div/div[4]/div/main/div[2]/div/article/section[2]/div[2]/ol')[0].text.split('\n')

print("Getting Original Clues from: nytimes.com\n")
print("Across Clues\n",clues_across)
print()
print("Down Clues\n",clues_down)

solutions = []


for i in range(25):
    css_link = '#xwd-board > g:nth-child(5) > g:nth-child('+str(i+1)+')'
    #print(css_link)
    if not browser.find_elements_by_css_selector(css_link):
        solutions.append('')
    else:
        solutions.append(browser.find_elements_by_css_selector(css_link)[0].text.split("\n"))

sol = list()
loc = list()
counter = 0
for i in solutions:
    if i[0].isdigit():
        sol.append(i[1])
        loc.append(i[0])
    else:
        sol.append(i[0])
        loc.append('')
    counter += 1

sol = np.array(sol).reshape(5,5)
loc = np.array(loc).reshape(5,5)

accross_solution = list()
for i in range(5):
    for j in range(5):
        if loc[i][j].isdigit() == True:
            accross_solution.append(loc[i][j])
            accross_solution.append(''.join(map(str,sol[i])))
            break

print("\nGetting Solutions from: nytimes.com\n")
print("Accross solutions:\n",accross_solution,"\n")

down_solution = list()
for i in range(5):
    for j in range(5):
        if loc[j][i].isdigit() == True:
            down_solution.append(loc[j][i])
            down_solution.append(''.join(map(str,sol[:,i])))
            break

temp = list()
for i in range(0,len(down_solution),2):
    temp.append((int(down_solution[i]),down_solution[i+1]))


temp = sorted(temp,reverse = False)

for i in range(0,len(down_solution),2):
    down_solution[i],down_solution[i+1] = str(temp[int(i/2)][0]),temp[int(i/2)][1]

print("Down solutions:\n",down_solution)



output = open("output.txt",'w')
output.writelines(str(clues_across))
output.write('\n')
output.writelines(str(clues_down))
output.write('\n')
output.writelines(str(solutions))
output.write('\n')
output.close()

new_clues_accross = list()
new_clues_down = list()

for i in range(0,len(accross_solution),2):
    print()
    print("Step1 - From Meriam Webster Finding clue for ", accross_solution[i+1])
    new_clues_accross.append(accross_solution[i])
    clue = merriam_webster(browser,accross_solution[i+1])
    if clue!=False and (accross_solution[i+1][-1] != "S" or len(accross_solution[i+1])<=3) and len(clue) < 150:
        new_clues_accross.append(clue)
    else:
        print()
        print("Step2 - From Wikipedia Finding clue for ", accross_solution[i+1])
        clue = wiki(accross_solution[i+1])
        if clue != False and (accross_solution[i+1][-1] != "S" or len(accross_solution[i+1])<=3)  and len(clue) < 150:
            new_clues_accross.append(clue)
        else:
            print()
            print("Step3 - From Word Hippo Finding clue for ", accross_solution[i+1], "By creating sentences with answer")
            clue = word_hippo(browser,accross_solution[i+1])
            if clue != False:
                new_clues_accross.append(clue)
            else:
                print()
                print("Step4 - From Anagram Smith Finding clue for ", accross_solution[i+1])
                clue = anagramSmith(browser,accross_solution[i+1])
                if clue != False:
                    new_clues_accross.append(clue)
                else:
                    new_clues_accross.append(" ") #Wordnet


    print("New clue is: ",clue)

for i in range(0,len(down_solution),2):
    print()
    print("Step1 - From Meriam Webster Finding clue for ", down_solution[i+1])
    new_clues_down.append(down_solution[i])
    clue = merriam_webster(browser,down_solution[i+1])
    if clue!=False and (down_solution[i+1][-1] != "S" or len(down_solution[i+1])<=3) and len(clue) < 150:
        new_clues_down.append(clue)
    else:
        print()
        print("Step2 - From Wikipedia Finding clue for ", down_solution[i+1])
        clue = wiki(down_solution[i+1])
        if clue != False and (down_solution[i+1][-1] != "S" or len(down_solution[i+1])<=3) and len(clue) < 150:
            new_clues_down.append(clue)
        else:
            print()
            print("Step3 - From Word Hippo Finding clue for ", down_solution[i+1], "By creating sentences with answer")
            clue = word_hippo(browser,down_solution[i+1])
            if clue != False:
                new_clues_down.append(clue)
            else:
                print()
                print("Step4 - From Anagram Smith Finding clue for ", down_solution[i+1])
                clue = anagramSmith(browser,down_solution[i+1])
                if clue != False:
                    new_clues_down.append(clue)
                else:
                    new_clues_down.append(" ") #Wordnet

    print("New clue is: ",clue)

browser.quit()

