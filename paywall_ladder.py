import requests
import tempfile
import webbrowser
import time
#from bs4 import BeautifulSoup

while True:
    url = input('\nUrl: ').split('?', 1)[0]

    if 'https' not in url and '.com' not in url and '.edu' not in url and '.net' not in url and '.org' not in url and '.biz' not in url and '.co' not in url and '.is' not in url and '.uk' not in url:
        proceed = input("\nThis doesn't look like a link. Are you sure you want to proceed? (y) or (n) ")

        if proceed == 'y':
            break
    else:
        break

def cache():
    print('\nChecking Google cache...\n')

    c_url = f'https://webcache.googleusercontent.com/search?q=cache:{url}'
    r = requests.get(c_url)

    if r.status_code == 200:
        webbrowser.open(c_url)
    else:
        print('Cache returned error')

def archiveIs():
    print('\nChecking Archive.ph...\n')

    webbrowser.open(f'https://archive.is/latest/{url}')

def twelveFt():
    print('\nChecking 12ft.io...\n')

    webbrowser.open(f'https://12ft.io/{url}')

def webArchive():
    print('\nChecking The Internet Archive...\n')

    webbrowser.open(f'https://web.archive.org/web/{url}')

def googleBot():
    print('\nAttempting direct access with GoogleBot...\n')

    gb_headers = {
                "User-Agent": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
            }

    r = requests.get(url=url, headers=gb_headers)

    with tempfile.NamedTemporaryFile('w', delete=False, suffix='.html', encoding="utf-8") as f:
        url_file = 'file://' + f.name
        f.write(r.text)

    webbrowser.open(url_file)

def bingBot():
    print('\nAttempting direct access with BingBot...\n')

    bb_headers = {
        "User-Agent": "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm) Chrome/"
    }

    r = requests.get(url=url, headers=bb_headers)

    with tempfile.NamedTemporaryFile('w', delete=False, suffix='.html', encoding="utf-8") as f:
        url_file = 'file://' + f.name
        f.write(r.text)

    webbrowser.open(url_file)

def notBypassed():
    print("Paywall not bypassed.")
    time.sleep(1)

func_list = [cache, archiveIs, twelveFt, webArchive, googleBot, bingBot, notBypassed]
worked = 'n'

for func in func_list:
    if worked == 'n' and func != notBypassed:
        paywall_free = func()

        while True:
            worked = input("Did that work (y) or should we continue searching (n)? ")

            if worked != 'y' and worked != 'n':
                print("Hey! That's not a (y) or (n). Try again (and don't break it this time).")
            else:
                break
    elif worked =='n' and func == notBypassed:
        func()
