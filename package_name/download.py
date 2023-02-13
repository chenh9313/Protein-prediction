import requests
from bs4 import BeautifulSoup

def download_sequence(genename,link):
    """Return the genome sequence information of target gene from website."""
    #The following library downloads the data and stores it in a page variable
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'html.parser')
    #getting the raw target genome sequence and stores it in a rawseq variable
    rawseq = soup.find_all('p', style="font-family: monospace")
    rawseq2 = rawseq[0].get_text().replace("\xa0","").replace("\n","").replace(" ","")
    seq = ''.join([i for i in rawseq2 if not i.isdigit()])
    print("Length is:",len(seq),"pb")
    print(genename, "genome sequence is:\n", seq)
    return len(seq)
