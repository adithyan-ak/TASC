from bs4 import BeautifulSoup
import requests,urllib3,re
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def FacebookScrapper(keyword):

    cookies = {
        '$fr': '0vQABpcQZwjTpBMmX.AWX0PwLhaUv1ktOxsouLHyHdfRY.Bd5gy7.4g.AAA.0.0.Bd9P1N.AWURA5LL',
        'wd': '1316x602',
        'datr': 'ZWPzXfPGgqzCxcYoeF5FOFAp',
        'sb': 'r2bzXQjlJGU5mx25L2r1mqcZ',
        'locale': 'en_GB',
        'c_user': '100025059800297',
        'xs': '1%3AoaupB5_F7WIOkA%3A2%3A1576336717%3A13272%3A4196',
    }

    headers = {
        '$Host': 'mbasic.facebook.com',
        '$User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0',
        '$Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        '$Accept-Language': 'en-US,en;q=0.5',
        '$Accept-Encoding': 'gzip, deflate',
        '$Referer': 'https://mbasic.facebook.com/home.php?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F%3Fref%3Ddbl&ref=dbl&_rdr',
        '$Connection': 'close',
        '$Upgrade-Insecure-Requests': '1',
    }

 #   keyword = input("Enter the keyword to Monitor : ")
    print()

    #keyword = "Fucker"

    params = (
        ('q', keyword),
        ('refid', '7'),
        ('ref', 'dbl'),
        ('_rdr', ''),
    )

    def stop():
        print()
        print("->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->")
        print()
        return
    #=====================================Home=======================================

    url = "https://mbasic.facebook.com/search/top"
    main_resp = requests.get(url=url, headers=headers, params=params, cookies=cookies, verify=False)

    soup = BeautifulSoup(main_resp.content, 'html.parser')


    #cw cx -> fucker
    # bt bu -> fucker 2
    #bt bu -> bitch 1 & 2
    #pervert -> df dg
    #bt bu -> pervert 2nd
    #bt bu -> pervert 3rd

    posts = soup.find_all('div', class_ = 'bt bu')
    if len(posts) == 0:
        posts = soup.find_all('div', class_='cw cx')
        if len(posts) == 0:
            posts = soup.find_all('div', class_='df dg')


    for i in range(len(posts)):
        u_name = str(posts[i].div.a)
        name = re.sub('<.*?>', '', u_name)
        name = name.replace("amp;", '')
        print("Name : "+name)
        u_caption = str(posts[i].div.p)
        caption = re.sub('<.*?>', '', u_caption)
        caption = caption.replace("amp;", '')
        print("Post : "+caption)
        u_img = str(posts[i].div.img)
        img = re.findall(r'src="(.*?) width=', u_img) or re.findall(r'src="(.*?)/>', u_img)
        jpg = img
        img_url = str([item.replace("amp;", "") for item in jpg])
        print("Image :"+ img_url)
        print("------------------------------")

    #======================================2nd-page================================================

    next_page = soup.find('div', id="see_more_pager")
    u_next = str(next_page.a)
    next = re.findall(r'href="(.*?)"><span>', u_next)
    next_url = next[0].replace("amp;",'')

    sec_resp = requests.get(url=next_url, headers=headers, cookies=cookies, verify=False)


    soup = BeautifulSoup(sec_resp.content, 'html.parser')

    posts = soup.find_all('div', class_='bt bu')


    if len(posts) == 0:
        posts = soup.find_all('div', class_='cw cx')
        if len(posts) == 0:
            posts = soup.find_all('div', class_='df dg')
            if len(posts) == 0:
                posts = soup.find_all('div', class_='bq br')
                if len(posts) == 0:
                    print("End of Results")
                    stop()

    for i in range(len(posts)):
        u_name = str(posts[i].div.a)
        name = re.sub('<.*?>', '', u_name)
        name = name.replace("amp;", '')
        print("Name : " + name)
        u_caption = str(posts[i].div.p)
        caption = re.sub('<.*?>', '', u_caption)
        caption = caption.replace("amp;", '')
        print("Post : " + caption)
        u_img = str(posts[i].div.img)
        img = re.findall(r'src="(.*?) width=', u_img) or re.findall(r'src="(.*?)/>', u_img)
        jpg = img
        img_url = str([item.replace("amp;", "") for item in jpg])
        print("Image :" + img_url)
        print("------------------------------")

    # ======================================3rd-page=============================================

    next_page = soup.find('div', id="see_more_pager")
    u_next = str(next_page.a)
    next = re.findall(r'href="(.*?)"><span>', u_next)
    next_url = next[0].replace("amp;", '')

    third_resp = requests.get(url=next_url, headers=headers, cookies=cookies, verify=False)

    soup = BeautifulSoup(third_resp.content, 'html.parser')

    posts = soup.find_all('div', class_='bt bu')

    if len(posts) == 0:
        posts = soup.find_all('div', class_='cw cx')
        if len(posts) == 0:
            posts = soup.find_all('div', class_='df dg')
            if len(posts) == 0:
                print("End of posts")
                stop()

    for i in range(len(posts)):
        u_name = str(posts[i].div.a)
        name = re.sub('<.*?>', '', u_name)
        name = name.replace("amp;",'')
        print("Name : " + name)
        u_caption = str(posts[i].div.p)
        caption = re.sub('<.*?>', '', u_caption)
        caption = caption.replace("amp;", '')
        print("Post : " + caption)
        u_img = str(posts[i].div.img)
        img = re.findall(r'src="(.*?) width=', u_img) or re.findall(r'src="(.*?)/>', u_img)
        jpg = img
        img_url = str([item.replace("amp;", "") for item in jpg])
        print("Image :" + img_url)
        print("------------------------------")

    # ======================================4th-page=============================================

    next_page = soup.find('div', id="see_more_pager")
    u_next = str(next_page.a)
    next = re.findall(r'href="(.*?)"><span>', u_next)
    next_url = next[0].replace("amp;", '')

    fourth_resp = requests.get(url=next_url, headers=headers, cookies=cookies, verify=False)

    soup = BeautifulSoup(fourth_resp.content, 'html.parser')

    posts = soup.find_all('div', class_='bt bu')

    if len(posts) == 0:
        posts = soup.find_all('div', class_='cw cx')
        if len(posts) == 0:
            posts = soup.find_all('div', class_='df dg')
            if len(posts) == 0:
                print("End of posts")
                stop()

    for i in range(len(posts)):
        u_name = str(posts[i].div.a)
        name = re.sub('<.*?>', '', u_name)
        name = name.replace("amp;",'')
        print("Name : " + name)
        u_caption = str(posts[i].div.p)
        caption = re.sub('<.*?>', '', u_caption)
        caption = caption.replace("amp;", '')
        print("Post : " + caption)
        u_img = str(posts[i].div.img)
        img = re.findall(r'src="(.*?) width=', u_img) or re.findall(r'src="(.*?)/>', u_img)
        jpg = img
        img_url = str([item.replace("amp;", "") for item in jpg])
        print("Image :" + img_url)
        print("------------------------------")

    print()
    print("->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->")
    print()