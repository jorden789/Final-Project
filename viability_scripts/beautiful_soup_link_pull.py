# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
#from urllib import urlopen, request
import re
import spacy
import sys
from bs4.element import Comment
if sys.version_info[0] == 3:
 from urllib.request import urlopen, request
else:
 from urllib import urlopen

# Set Spacy Language to Englishe
nlp = spacy.load('en')

# Set search link for LiveCareer Website (currently for Software Engineering CVs)
html_page = urlopen("https://resumes.livecareer.com/search?jt=software%20engineering&p=1")
soup = BeautifulSoup(html_page, "html5lib")

# Find all list items in returned search results page
pagination_soup = soup.findAll("li", {"class": "list-head"})

# For each list item, trim all leading/trailing spaces and if token (word) is of type number, then format as ##### and print result (for this page will be total number of records
for page_text in pagination_soup:
    doc1 = nlp((page_text.text).strip())
    for token in doc1:
        if token.pos_ == "NUM":
            num_results = str.replace(str(token.text), ',', '')
            print("Total Number of Records: " + str(num_results))

# For the page range 1 to 5, of the previously mentioned search, we specify specific pages in result set of search
for i in range(5):
    url = "https://resumes.livecareer.com/search?jt=software%20engineering&pg=" + str(i + 1)
# Open specified page and process with specified html5 parser
    html_page = urlopen(url)
    soup = BeautifulSoup(html_page, "html5lib")

# Set variable n = 0 which will be used as distinguishing metric for CV file name when stored as text 
    n = 0

# Find all link in search results page that have the hyperlink begin with '/r' as this points to a sample resume
    for link in soup.findAll('a', attrs={'href': re.compile("^/r")}):
        n += 1 

# Append the href link to the Domain to get the fully qualified link to individual Sample CV under the specified search term
        cv_url = "https://www.livecareer.com" + link.get('href')

        def tag_visible(element):
            if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
                return False
            if isinstance(element, Comment):
               return False
            return True

        def text_from_html(body):
            soup = BeautifulSoup(body, 'html.parser')
            texts = soup.findAll(text=True)
            visible_texts = filter(tag_visible, texts)
            return u" ".join(t.strip() for t in visible_texts)

# Open the Specified CV URL and read all contents
        try:
            if '/r/' in cv_url:
                html = urlopen(cv_url)
                print("Processing URL: " + cv_url)
                path = "/home/jallcock/environments/python_output/CV-" + str((i * 10) + n) + ".txt"
                cv_soup = BeautifulSoup(html.read(), 'html5lib')

                cv_info = cv_soup.find_all('div', {'id' : 'document'})
                for cv_info_line_item in cv_info:
                    #print(cv_info_line_item)
                    with open(path, 'w') as f:
                        article = cv_info_line_item.get_text()
                        f.write(article.translate(''.join( [chr(i) for i in range(128)] + [' '] * 128 )))

        except:
            continue


#        os.system('python /home/jallcock/environments/Final-Project/cv_process.py ' + path)
# Create file ready for storing contents of CV URL page
#        path = "/home/jallcock/environments/python_output/CV-" + str((i * 10) + n) + ".txt"	
#        with open(path, 'w') as f:
# Write contents of CV URL page to the newly created file, ready for offline storage/processing
#            f.write(text_from_html(html))


