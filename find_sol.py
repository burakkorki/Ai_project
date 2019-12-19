from selenium import webdriver
import os
import numpy as np
from get_clues import *

chrome_options = webdriver.ChromeOptions()

#To hide chrome comment out the following line 
#chrome_options.add_argument('--headless')
browser = webdriver.Chrome(os.path.abspath(os.curdir)+'/chromedriver 78',options=chrome_options)

browser.get('https://www.nytimes.com/crosswords/game/mini')
browser.find_elements_by_xpath('//*[@id="root"]/div/div/div[4]/div/main/div[2]/div/div[2]/div[3]/div/article/div[2]/button/div/span')[0].click()
browser.find_elements_by_xpath('//*[@id="root"]/div/div/div[4]/div/main/div[2]/div/div/ul/div[2]/li[2]/button')[0].click()
browser.find_elements_by_xpath('//*[@id="root"]/div/div/div[4]/div/main/div[2]/div/div/ul/div[2]/li[2]/ul/li[3]/a')[0].click()
browser.find_elements_by_xpath('//*[@id="root"]/div/div[2]/div[2]/article/div[2]/button[2]/div/span')[0].click()
browser.find_elements_by_xpath('//*[@id="root"]/div/div[2]/div[2]/span')[0].click()

clues_across = list()
clues_down = list()

clues_across = browser.find_elements_by_xpath('//*[@id="root"]/div/div/div[4]/div/main/div[2]/div/article/section[2]/div[1]/ol')[0].text.split('\n')
clues_down = browser.find_elements_by_xpath('//*[@id="root"]/div/div/div[4]/div/main/div[2]/div/article/section[2]/div[2]/ol')[0].text.split('\n')

print("Across Clues\n",clues_across)
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
print("Accross solutions:\n",accross_solution)

down_solution = list()
for i in range(5):
    for j in range(5):
        if loc[j][i].isdigit() == True:
            down_solution.append(loc[j][i])
            down_solution.append(''.join(map(str,sol[:,i])))
            break
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

for i in range(0,len(accross_solution),2):
    new_clues_accross.append(accross_solution[i])
    clue = merriam_webster(browser,accross_solution[i+1])
    if clue!=False:
        new_clues_accross.append(clue)

print("New clues accross:\n",new_clues_accross)

for i in range(0,len(down_solution),2):
    new_clues_down.append(down_solution[i])
    clue = merriam_webster(browser,down_solution[i+1])
    if clue!=False:
        new_clues_down.append(clue)

print("New clues down:\n",new_clues_down)

browser.quit()

