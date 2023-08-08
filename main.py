import requests
import re
from bs4 import BeautifulSoup

if __name__ == "__main__":
    # get the data from the page
    data = requests.get("https://github.com/neovim/neovim/releases")

    # load the data into bs4(Beautiful Soup 4)
    soup = BeautifulSoup(data.text, 'html.parser')

    # getting data by looking into divs
    div = soup.find('div', {'class': 'markdown-body my-3'})
    div2 = div.find('div', {'class': 'snippet-clipboard-content notranslate position-relative overflow-auto'})
    pre = div2.find_all('pre')

    text = list(str(pre[0].text))

    data = []

    for tex in text: 
        if tex == "\n":
            break
        data.append(tex)

    print(''.join(map(str, data)))
