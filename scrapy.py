import argparse
import mechanicalsoup
from getpass import getpass
import os
import pathlib
from urllib.parse import urlparse

parser = argparse.ArgumentParser(description="Login do AVA.")
parser.add_argument("username")
args = parser.parse_args()

args.password = getpass("Entre a senha do AVA: ")

page3 = input("Endereço do Quiz: ")


browser = mechanicalsoup.StatefulBrowser(
    soup_config={'features': 'lxml'},
    raise_on_404=True,
    user_agent='MyBot/0.1: mysite.example.com/bot_info',
)


# Uncomment for a more verbose output:
# browser.set_verbose(2)

browser.open("https://ava.pr1.uerj.br")
browser.follow_link("login")
browser.select_form()
browser["username"] = args.username
browser["password"] = args.password
resp = browser.submit_selected()

# Uncomment to launch a web browser on the current page:
# browser.launch_browser()

# verify we are now logged in
page = browser.page
print(page.title.text)

browser.open(page3)

links=browser.page.find_all("a", {"class": "reviewlink"}, href=True)
W=len(links)

for n in range(0, W):
    print(links[n]['href'])
    browser.open(links[n]['href'])

    aluno=browser.page.find_all("td", {"class": "cell"})[0].find_all("a", {"class": ""}, id=True)[0].text
    print(aluno)

    if os.path.isdir(aluno):
        folder_name=aluno+' 2'
    else:
        folder_name=aluno

    pathlib.Path(folder_name).mkdir(parents=True, exist_ok=True)

    filename=folder_name+'/prova.html'
    browpage=browser.page

    with open(filename, "w") as file:
        file.write(str(browpage))

    S=len(browser.page.find_all("div", {"class": "attachments"}))

    for j in range(0, S):

        T=len(browpage.find_all("div", {"class": "attachments"})[j])

        if T > 0:
            link_item=browpage.find_all("div", {"class": "attachments"})[j].find_all("a", href=True)[0]['href']
            a = urlparse(link_item)
            file=os.path.basename(a.path)
            filename=folder_name+'/'+file
            response = browser.open(link_item)

            with open(filename, "wb") as f:
                f.write(response.content)

    S=len(browpage.select("a[href*=response_bf]"))

    for j in range(0, S):

        link_item=browpage.select("a[href*=response_bf]")[j]['href']
        a = urlparse(link_item)

        file=os.path.basename(a.path)
        filename=folder_name+'/'+file
        response = browser.open(link_item)

        with open(filename, "wb") as f:
            f.write(response.content)
