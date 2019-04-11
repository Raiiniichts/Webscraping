# BRUCE Cybersecurity Database Search Engine

The BRUCE Engine is a database search function that allows a user to search for a large number of cybersecurity courses through the domain bruce.ist.psu.edu. A search can return many courses in the area of cybersecurity. Each search result contains information such as professor, university, and textbook. It also includes a link to the course syllabus website and a screenshot preview of what the website looks like.

## Process



### Web Scraping
* [scrarping through google search] Use keywords search to on google and extract hyperlinks on the result page.
* [scrarping through conference list] Conduct DFS scraping given the list of professors personal websites.
* [scrarping through School] Conduct DFS scraping given the list of school faculty websites.

### Page Classification 
* [Naive Bayes] Feed directly with text corpus, achieved >90% test accuracy (from google search corpus).
* [SVM] Feed directly with text corpus achieved >95% test accuracy (from google search corpus).
* [LSTM] Feed directly with text corpus, title, numbers of hyperlinks, numbers of pictures achieved >97% test  accuracy(from google search corpus). (reference:https://www.linkedin.com/pulse/identifying-clickbaits-using-machine-learning-abhishek-thakur/) 
* Note: the distributioin of the dataset varies depending of the web scraping methods, therefore the testing accuracy might change. 

### Feature Extraction 


### Full Stack Development





## Built With

* [Python== 3.5]  - Language

* [BeautifulSoup==4.4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - The Web Scraping 
* [requests==2.21](https://docs.python.org/3/library/urllib.html) - The Web Scraping 
* [urllib==3.7.3](https://docs.python.org/3/library/urllib.html) - The Web Scraping 
* [tldextract](https://github.com/john-kurkowski/tldextract) - The Web Scraping  -Domain Extractor 

* [textblob](https://textblob.readthedocs.io/en/dev/) - Page Classificatoin- Naive Bayes Algorithm 
* [Scikit-learn==0.20.3](https://scikit-learn.org/stable/modules/svm.html) - Page Classificatoin- SVM 

* [nltk==3.4](https://www.nltk.org/) -Feature Extraction - Named Entity extraction 
* [html2text==2018.1.9](https://pypi.org/project/html2text/) - Feature Extraciton 
## Contributing

For those assuming control of this project in Fall 2019, let Dongwon contact us and I can give over master control of the repository to an account.


## Authors
* **Weiqin Wang
* **Andrew Yang


## Acknowledgments

Thanks to Dongwon Lee for overseeing this project.

