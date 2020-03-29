# Requirements

## Selenium

> > pip install selenium

## Tkinter

> > pip install tkinter

## Numpy

> > pip install numpy

## Wikipedia

> > pip install wikipedia

## Wordnet

> > pip install wordnet

# 1.0 Introduction

Puzzles are very popular around many people as they are mysterious, challenging and fun. Solving puzzles can enhance vocabulary knowledge and improve writing and speaking skills. That's why many people enjoy solving puzzles on a daily basis. One of the most famous newspaper, The New York Times, does publish an online puzzle called “Mini crossword puzzle”. It is designed by Joel Fagliano and it is released every day. This Puzzle contains 5 rows and 5 columns and it comes with 5 across and 5 down clues. Our team, Suzzle Polver, developed a program that is based on artificial intelligence (AI) technology that is designed to generate different clues over the available ones for any given mini crossword puzzle. The program takes advantage of many online resources, such as dictionaries, to come up with different clues while keeping the same answers to the puzzle. This way, users will be able to obtain another set of clues if they fail to solve the puzzle with existing ones. As Suzzle Polver, we believe that our program will help the future puzzle solvers by providing them with a few more changes so they can improve in this beneficial habit and continue to perform this rewarding hobby.

# 2. AI Aspect

In this section, problem-solving techniques and models of the Suzzle Polver are explained. Our problem-solving methods start with selecting sources for generating new clues. In the beginning, we decided to use qualitative sources as Merriam Webster, Wikipedia, Urban Dictionary, Word Hippo, and Anagram Smith generator. In terms of generating qualitative clues, we decided not to use sentence paraphrasing tools such as Free Article Spinner, and Seo Magnifier. These tools generate similar sentences with the original clues, and they contain security check services which cause delays, so we did not use paraphrasing tools. We implemented the Goal Tree method to indicate the steps in the clue generating process. We decided to get shorter clues as Joel Fagliano’s style. As a problem reduction method, we eliminated sentences longer than 120 words and we underscored the words that matched with the solution in these sentences. Diving the problem into smaller subproblems helped us to generate meaningful new clues for many word types. These methods and sources that will be investigated in the 2.1 Generate and Test, and 2.2 Goal Tree subsection in detail.

## 2.1 Generate and Test

The main procedure that we used in our project was to Generate and Test. Firstly, we generate possible clues from different websites. These websites are Merriam Webster, Wikipedia, Wordhippo, Urban Dictionary, and Anagram Smith. Since Merriam Webster is a dictionary, sometimes it can not find special names, plural words or place names. Another issue of Merriam Webster was, it sometimes finds very long definitions. Very long definitions are contrary to the logic of the puzzle. Therefore they are not proper clues for answers. We decided that a clue of an answer to the puzzle is long if it is larger than 120 characters. Additionally, we filtered parentheses in sentences. If resulted definitions are long or it can not find any result, we
continue to test other clues that we have
obtained from the mentioned websites.

After Merriam Webster, we test the result that we obtained from Wikipedia. While doing that we get the first sentence in the summary part of the Wikipedia page of the searched answer. Wikipedia is useful for special names, and abbreviations. The first sentence contains the answer to the puzzle. So we eliminated the answer from the sentence and converted the position of the answer to an empty slot. In most of the cases, special name issue that Merriam Webster cannot solve is solved by Wikipedia.​​Like Merriam Webster, Wikipedia sometimes produces long sentences. If the clue we got from Wikipedia is long or it can not find the result, we continue to search the clues from Wordhippo. Wordhippo is a sentence generator tool. We searched the answer in this tool and get the sentence that Wordhippo produced. Wordhippo produces multiple sentences from the searched answer. We picked the shortest sentence from the sentence list. The picked sentence was containing the actual answer, so we eliminated the answer by converting its position to an empty slot. If we cannot find an answer from Wordhippo, we continued to search the clues from the Urban Dictionary. Urban Dictionary provided us to find clues about the slang words and cultural phrases. The last step that we used to find clues is Anagram Generator. Anagram Generator generates all anagrams of the searched word. If we cannot find any clues from previous steps we from clue by using the anagram of the word.

In each step that we used to generate a clue, if we observe a satisfactory solution, we use that solution as a clue for our puzzle. If the solution that a step is not satisfying our constraints for a clue, we’ve eliminated these solutions and look candidate solutions that other websites produced. Therefore by using the Generate and Test Procedure, we generate the best clues for our puzzle.

## 2.2 Goal Tree

### Abbreviations used above:

- M: Merriam Webster
- WP: Wikipedia
- WH: Word Hippo

- WN: Wordnet
- A: Anagram
- Q: Query

### Explanation of Subproblems:

- Crawl - (NY Times): Crawls original clues and answers published at NY-Times crossword.
- Enter: Indicates the entering of a website.
- Generate-Clues: Generate new clues based on original ones and their answers.

- Crawl - (Defined Sites): Crawls predefined five websites.
- Search-Q: Searches the relevant query in a website.
- Copy-Answer: Copy the result of the query.
- Select - Best Clues: The selection of best clues based on the priorities of websites and character length of clues.

### Detailed Explanation:

Our project was composed of lots of subproblems that we had to deal with. As our project demos directed us, we’ve divided it into 3 major and lots of minor subproblems. In the first project demo, we had to crawl original clues and answers from the NY-Times web site, show this crawling process clearly and appropriate user interface.
The Crawling NY Times web site was the easiest subproblem. We were already capable of using tools to crawl websites and in a couple of days, this part has accomplished. Before solving other problems we were saving all clues and answers to a text file for future use.
The Generate Clues subproblem was the hardest among there major problems as expected. First of all, we’ve focused on paraphrasing the original clues, but the paraphrased versions were irrelevant or very similar to the original clue. Therefore, we’ve eliminated this solution without losing time and started focusing on answers.
Secondly, we’ve focused on generating clues by using the answers instead of original clues. A lot of time spent on finding accurate websites to crawl to generate meaningful and convenient to the structure of the NY Times puzzle. In the end, we’ve decided 5 different web sites to search for new clues. A dictionary, Merriam Webster, encyclopedia, Wikipedia, one of the largest word database, Wordnet, an anagram generator, inges-anagram, and sentence generator, Wordhippo. After deciding which websites will be used crawling them and getting new clues were straightforward.
Our third major subproblem was selecting the best clues. After successfully implementing the crawling mechanism and taking all the results from defined websites we’ve started doing experiments about the quality of clues that are gathered from these sites. We’ve tried to increase the quality of resulting clues. In that aspect we’ve spent time understanding the structure of the original NY Times clues structure, it is seen that best clues in terms of similarities to the original clues were coming from Wikipedia and Merriam Webster. Therefore, they are assigned as higher priority clue sources. Although it came up with a solution in every trial, anagram generator has assigned as a lower priority because the structure of anagram clues was not fitting the original structure of clues. After completing these decisions, the resulting priority order of websites as follows, Merriam Webster, Wikipedia, Word Hippo, Wordnet, Anagram generator. After the first demo, we’ve designed this selecting mechanism again with respect to the feedback. Because even though the system was working perfectly and the resulting clues were not perfect yet. As the opposite of original clues, the length of recently created clues was very long and the crawling mechanism was not working perfectly. We’ve decreased the length of sentences by extracting the parentheses. We’ve added a length constraint in order to force the system to eliminate clues longer than 120 characters and the resulting clues reached a better form. Lastly, we’ve fixed the bugs of crawling mechanism and limited word filling type of questions with three.

The showing results subproblem has been solved faster than crawling and selecting the best clues subproblems. Since that part requires less effort the expectations were higher, we’ve tried place the original clues and answers similar to the original NY Times website and after first feedback, we’ve spent time on making our grid composed of perfect squares instead of rectangular boxes. After locating the recently generated clues to the bottom of the original ones this subproblem has solved. That was the last subproblem of the supreme problem "Displaying Solution". Therefore, our term project is concluded. The screenshots of the resulting problem are listed in the appendix.

# 3. Future Work
Different methods which are related to described AI aspects in recent sections used in Suzzle Polver in order to generate clues by using answers and original clues of the New York Times Crossword

Puzzle by checking different sources from the internet. This section contains information about how Suzzle Polver can be improved to generate clues that are more accurate and similar to the original clues in terms of length, language and style. In order to increase the accuracy of the new clues, examining a large data set that contains crossword puzzles both clues and answers from different sources can be done as a first step [2]. Crossword puzzles mostly include clues and answers which are related to the daily life of people. By examining older clues and answers generating similar and related clues as possible. Separate modules should be implemented to examine data and create new clues.
Generated clues may be full sentences, abbreviations, incomplete sentences, synonyms, etc just like an original clue. In most basic sense implementation of two different modules can be optimal for improvement of this project. The first module should deal with large data sets obtained from other crossword puzzles where the second module should be able to create sentences, search for synonyms, opposite meanings of words and also check corner cases like words only used in idioms and daily life language. The second module may use Frame Theory which is an AI approach to generalize linguistic notions with the case of grammar. Which makes a possible representation of both syntactic and procedural knowledge fro parsing and understanding related semantic, contextual sentences [3]. So the second module should able to understand close sentences, clues in terms of domain and context by parsing clues and answers obtained by using the first module. In Suzzle Polver we used different methods for clue generation but it is believed that the accuracy of clues will be increased by implementing and using these two new modules.

# 4. Conclusion

The power of artificial intelligence should not be underestimated as if they are designed and implemented in a proper way. AI’s can accomplish many tasks in a very short period of time compared to humans. In order to be sure about the accuracy of any AI, designers should create a program such that it attaches importance to 2 factors: methods and resources. There are many available methods to solve a problem, in our project we’ve focused on generate and test or goal tree . However, there will always be a dead-end for certain situations. A designer should be aware of this by implementing backup methods so to increase the accuracy of a program. Moreover, benefiting from a few numbers of resources can be restrictive. Searching many more sources and comparing results will assure designers about the legitimacy of the program. This project was very informative about AI so that, as Suzzle Polver, we comprehended what we can achieve with AI technology. However, this is just the tip of the iceberg.
