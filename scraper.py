import requests
from lxml import etree
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

fullfcf = ''
fcfyield = 0
module = int(input('Input module code:\n1. Operating Margin\n2. ROI\n3. EBITDA\n4. Price to Book\n5. Price to Earnings\n6. Dividend Yield\n7. Free Cash Flow Yield\n8. Debt to Equity Ratio\n9. Current Ratio\n'))
decide = input("Input '1' for single ticker or '2' file path:\n")
if decide == '1':
    stock = input('Input ticker:\n')
elif decide == '2':
    path = input('Input file path:\n')
    tickers = open(r"'"+path+"'", 'r')
while True:
    if decide == '2':
        line = tickers.readline()
        stock = line.rstrip('\n')
    if not stock:
        break
    else:
        session = requests.Session()
        sessionHeaders = {
            "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
            "accept": "application/json",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9",
            "Connection": "keep-alive",
            "content-type": "application/json"
        }
        gurusession = requests.Session()
        guruHeaders = {
            "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9",
            "Connection": "keep-alive",
            "content-type": "application/json",
            "cookie": "PHPSESSID=lv81d6h2e9ggi20gqu75dhf963"}
        if module == 1:
            r = requests.get("https://www.macrotrends.net/stocks/charts/" + stock + "/~/operating-margin", headers=sessionHeaders)
            data = r.text
            soup = BeautifulSoup(data, 'html.parser')
            site = etree.HTML(str(soup))
            if site.xpath('/html/head/title')[0].text != 'Oops! Page not found	 | MacroTrends':
                tenyear = site.xpath('//*[@id="main_content"]/div[2]/span/strong')[0].text
                operatingmarginscraped = float(tenyear.replace('%',''))
                if operatingmarginscraped >= 27:
                    operatingmargin = 10
                elif operatingmarginscraped >= 24 and operatingmarginscraped < 27:
                    operatingmargin = 9
                elif operatingmarginscraped >= 22 and operatingmarginscraped < 24:
                    operatingmargin = 8
                elif operatingmarginscraped >= 20 and operatingmarginscraped < 22:
                    operatingmargin = 7
                elif operatingmarginscraped >= 16 and operatingmarginscraped < 20:
                    operatingmargin = 6
                elif operatingmarginscraped >= 13 and operatingmarginscraped < 16:
                    operatingmargin = 5
                elif operatingmarginscraped >= 10 and operatingmarginscraped < 13:
                    operatingmargin = 4
                elif operatingmarginscraped >= 5 and operatingmarginscraped < 10:
                    operatingmargin = 3
                elif operatingmarginscraped >= 0 and operatingmarginscraped < 5:
                    operatingmargin = 2
                elif operatingmarginscraped < 0:
                    operatingmargin = 1
            else:
                operatingmargin = 0
            print(operatingmargin)
        if module == 2:
            r = requests.get("https://www.macrotrends.net/stocks/charts/" + stock + "/~/financial-ratios", headers=sessionHeaders)
            data = r.text
            soup = BeautifulSoup(data, 'html.parser')
            site = etree.HTML(str(soup))
            newdata = data.split('var originalData = ')
            try:
                newnewdata = newdata[1]
                newnewnewdata = newnewdata.split("roi'>ROI")
                finaldata = newnewnewdata[1]
                finalfinaldata = finaldata.split("class='fas fa-chart-bar'>")
                finalfinalfinaldata = finalfinaldata[1]
                roidata = finalfinalfinaldata.split('"')
                if site.xpath('/html/head/title')[0].text != 'Oops! Page not found	 | MacroTrends':
                    firstyearroi = roidata[4]
                    secondyearroi = roidata[20]
                    try:
                        step1roi = float(firstyearroi)+float(secondyearroi)
                        roiavg = float(step1roi/2)
                        if roiavg >= 20:
                            roi = 10
                        elif roiavg >= 18 and roiavg < 20:
                            roi = 9
                        elif roiavg >= 16 and roiavg < 18:
                            roi = 8
                        elif roiavg >= 14 and roiavg < 16:
                            roi = 7
                        elif roiavg >= 12 and roiavg < 14:
                            roi = 6
                        elif roiavg >= 10 and roiavg < 12:
                            roi = 5
                        elif roiavg >= 8 and roiavg < 10:
                            roi = 4
                        elif roiavg >= 6 and roiavg < 8:
                            roi = 3
                        elif roiavg >= 4 and roiavg < 6:
                            roi = 2
                        elif roiavg < 4:
                            roi = 1
                    except:
                        roi = 0
                else:
                    roi = 0
            except IndexError:
                roi = 0
            print(roi)
        if module == 3:
            r = requests.get("https://www.macrotrends.net/stocks/charts/" + stock + "/~/ebitda", headers=sessionHeaders)
            data = r.text
            soup = BeautifulSoup(data, 'html.parser')
            site = etree.HTML(str(soup))
            if site.xpath('/html/head/title')[0].text != 'Oops! Page not found	 | MacroTrends':
                try:
                    newyear = site.xpath('//*[@id="style-1"]/div[1]/table/tbody/tr[1]/td[2]')[0].text
                    oldyear = site.xpath('//*[@id="style-1"]/div[1]/table/tbody/tr[4]/td[2]')[0].text
                    ebitda1 = str(newyear.replace('$',''))
                    ebitda2 = str(oldyear.replace('$',''))
                    if ebitda1 == '' and ebitda2 == '':
                        print(stock,'0')
                    try:
                        ebitda1final = float(ebitda1.replace(',',''))
                    except:
                        continue
                    try:
                        ebitda2final = float(ebitda2.replace(',',''))
                    except:
                        continue
                    try:
                        ebitda = ebitda1final/ebitda2final
                        ebitdaparsed = ebitda - 1
                        if ebitdaparsed >= 0.29:
                            ebitdarank = 10
                        elif ebitdaparsed >= 0.26 and ebitdaparsed < 0.29:
                            ebitdarank = 9
                        elif ebitdaparsed >= 0.23 and ebitdaparsed < 0.26:
                            ebitdarank = 8
                        elif ebitdaparsed >= 0.20 and ebitdaparsed < 0.23:
                            ebitdarank = 7
                        elif ebitdaparsed >= 0.17 and ebitdaparsed < 0.20:
                            ebitdarank = 6
                        elif ebitdaparsed >= 0.14 and ebitdaparsed < 0.17:
                            ebitdarank = 5
                        elif ebitdaparsed >= 0.11 and ebitdaparsed < 0.14:
                            ebitdarank = 4
                        elif ebitdaparsed >= 0.08 and ebitdaparsed < 0.11:
                            ebitdarank = 3
                        elif ebitdaparsed >= 0.05 and ebitdaparsed < 0.08:
                            ebitdarank = 2
                        elif ebitdaparsed < 0.05:
                            ebitdarank = 1
                    except:
                        continue
                except:
                    ebitdarank = 0
                    continue
            else:
                ebitdarank = 0
            print(ebitdarank)
        if module == 4:
            r = requests.get("https://www.macrotrends.net/stocks/charts/" + stock + "/~/price-book", headers=sessionHeaders)
            data = r.text
            soup = BeautifulSoup(data, 'html.parser')
            site = etree.HTML(str(soup))
            if site.xpath('/html/head/title')[0].text != 'Oops! Page not found	 | MacroTrends':
                ptob = float(site.xpath('//*[@id="main_content"]/div[2]/span/p[1]/strong')[0].text)
                if ptob >= 5:
                    pb = 1
                elif ptob >= 4.5 and ptob < 5:
                    pb = 2
                elif ptob >= 4 and ptob < 4.5:
                    pb = 3
                elif ptob >= 3.5 and ptob < 4:
                    pb = 4
                elif ptob >= 3 and ptob < 3.5:
                    pb = 5
                elif ptob >= 2.5 and ptob < 3:
                    pb = 6
                elif ptob >= 2 and ptob < 2.5:
                    pb = 7
                elif ptob >= 1.5 and ptob < 2:
                    pb = 8
                elif ptob >= 1 and ptob < 1.5:
                    pb = 9
                elif ptob < 1:
                    pb = 10
            else:
                pb = 0
            print(pb)
        if module == 5:
            r = requests.get("https://www.macrotrends.net/stocks/charts/" + stock + "/~/pe-ratio", headers=sessionHeaders)
            data = r.text
            soup = BeautifulSoup(data, 'html.parser')
            site = etree.HTML(str(soup))
            if site.xpath('/html/head/title')[0].text != 'Oops! Page not found	 | MacroTrends':
                ptoe = float(site.xpath('//*[@id="main_content"]/div[2]/span/p[1]/strong')[0].text)
                if ptoe >= 80:
                    pe = 1
                elif ptoe >= 60 and ptoe < 80:
                    pe = 2
                elif ptoe >= 45 and ptoe < 60:
                    pe = 3
                elif ptoe >= 30 and ptoe < 45:
                    pe = 4
                elif ptoe >= 20 and ptoe < 30:
                    pe = 5
                elif ptoe >= 15 and ptoe < 20:
                    pe = 6
                elif ptoe >= 12 and ptoe < 15:
                    pe = 7
                elif ptoe >= 8 and ptoe < 12:
                    pe = 8
                elif ptoe >= 3 and ptoe < 8:
                    pe = 9
                elif ptoe < 3:
                    pe = 10
            else:
                pe = 0
            print(pe)
        if module == 6:
            r = requests.get("https://www.macrotrends.net/stocks/charts/" + stock + "/~/dividend-yield-history", headers=sessionHeaders)
            data = r.text
            soup = BeautifulSoup(data, 'html.parser')
            site = etree.HTML(str(soup))
            if site.xpath('/html/head/title')[0].text != 'Oops! Page not found	 | MacroTrends':
                divscraped = site.xpath('//*[@id="main_content"]/div[2]/span/strong[2]')[0].text
                div = float(divscraped.replace('%',''))
                if div >= 5.75:
                    divyield = 10
                elif div >= 4.75 and div < 5.75:
                    divyield = 9
                elif div >= 4 and div < 4.75:
                    divyield = 8
                elif div >= 3.25 and div < 4:
                    divyield = 7
                elif div >= 2.5 and div < 3.25:
                    divyield = 6
                elif div >= 1.75 and div < 2.5:
                    divyield = 5
                elif div >= 1 and div < 1.75:
                    divyield = 4
                elif div >= 0.5 and div < 1:
                    divyield = 3
                elif div >= 0.1 and div < 0.5:
                    divyield = 2
                else:
                    divyield = 1
            else:
                divyield = 0
            print(divyield)
        if module == 7:
            fcfyield = 0
            fcf = '0'
            fcfscraped = '0%'
            options = Options()
            options.headless = True
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
            driver.get("https://www.gurufocus.com/term/total_freecashflow/" + stock + "/Free-Cash-Flow/")
            #r = requests.get("https://www.gurufocus.com/term/total_freecashflow/" + stock + "/Free-Cash-Flow/", headers=guruHeaders)
            #data = r.text
            #soup = BeautifulSoup(data, 'html.parser')
            #site = etree.HTML(str(soup))
            #fcfwebtest = "Results similar to '" + stock + "'"
            try:
                fcfscraped = driver.find_element(By.XPATH, '//*[@id="target_def_description"]/p[3]/strong[6]').text.strip(' ')
                #fcfscraped = site.xpath('//*[@id="target_def_description"]/p[3]/strong[6]')[0].text
            except:
                try:
                    fcfscraped = driver.find_element(By.XPATH, '//*[@id="target_def_description"]/p[3]/strong[4]').text.strip(' ')
                    #fcfscraped = site.xpath('//*[@id="target_def_description"]/p[3]/strong[4]')[0].text
                except:
                    try:
                        fcfscraped = driver.find_element(By.XPATH, '//*[@id="target_def_description"]/p[3]/strong[2]]').text.strip(' ')
                        #fcfscraped = site.xpath('//*[@id="target_def_description"]/p[3]/strong[2]')[0].text
                    except:
                        fcfyield = 0
            fcf = float(fcfscraped.replace('%',''))
            if fcf >= 14:
                fcfyield = 10
            elif fcf >= 11 and fcf < 14:
                fcfyield = 9
            elif fcf >= 9 and fcf < 11:
                fcfyield = 8
            elif fcf >= 7 and fcf < 9:
                fcfyield = 7
            elif fcf >= 5 and fcf < 7:
                fcfyield = 6
            elif fcf >= 4 and fcf < 5:
                fcfyield = 5
            elif fcf >= 2 and fcf < 4:
                fcfyield = 4
            elif fcf >= 1.5 and fcf < 2:
                fcfyield = 3
            elif fcf >= 1 and fcf < 1.5:
                fcfyield = 2
            elif fcf > 0 and fcf < 1:
                fcfyield = 1
            elif fcf <= 0:
                fcfyield = 0
            driver.close()
            fullfcf += fcfyield + '\n'
        if module == 8:
            r = requests.get("https://www.macrotrends.net/stocks/charts/" + stock + "/~/debt-equity-ratio", headers=sessionHeaders)
            data = r.text
            soup = BeautifulSoup(data, 'html.parser')
            site = etree.HTML(str(soup))
            if site.xpath('/html/head/title')[0].text != 'Oops! Page not found	 | MacroTrends':
                try:
                    de1 = site.xpath('//*[@id="style-1"]/table/tbody/tr[3]/td[4]')[0].text
                    de2 = site.xpath('//*[@id="style-1"]/table/tbody/tr[7]/td[4]')[0].text
                    d = float(de1)+float(de2)
                    de = d/2
                    if de >= 4:
                        derate = 1
                    elif de >= 3.2 and de < 4:
                        derate = 2
                    elif de >= 2.5 and de < 3.2:
                        derate = 3
                    elif de >= 1.8 and de < 2.5:
                        derate = 4
                    elif de >= 1.4 and de < 1.8:
                        derate = 5
                    elif de >= 1.2 and de < 1.4:
                        derate = 6
                    elif de >= 1.0 and de < 1.2:
                        derate = 7
                    elif de >= 0.8 and de < 1.0:
                        derate = 8
                    elif de >= 0.5 and de < 0.8:
                        derate = 9
                    elif de < 0.5:
                        derate = 10
                except:
                    derate = 0
                    continue
            else:
                derate = 0
            print(derate)
        if module == 9:
            r = requests.get("https://www.macrotrends.net/stocks/charts/" + stock + "/~/current-ratio", headers=sessionHeaders)
            data = r.text
            soup = BeautifulSoup(data, 'html.parser')
            site = etree.HTML(str(soup))
            if site.xpath('/html/head/title')[0].text != 'Oops! Page not found	 | MacroTrends':
                try:
                    ce1 = site.xpath('//*[@id="style-1"]/table/tbody/tr[3]/td[4]')[0].text
                    ce2 = site.xpath('//*[@id="style-1"]/table/tbody/tr[7]/td[4]')[0].text
                    c = float(ce1)+float(ce2)
                    ce = c/2
                    if ce >= 8:
                        cerate = 10
                    elif ce >= 6 and ce < 8:
                        cerate = 9
                    elif ce >= 4 and ce < 6:
                        cerate = 8
                    elif ce >= 2.5 and ce < 4:
                        cerate = 7
                    elif ce >= 1.75 and ce < 2.5:
                        cerate = 6
                    elif ce >= 1.25 and ce < 1.75:
                        cerate = 5
                    elif ce >= 1.0 and ce < 1.25:
                        cerate = 4
                    elif ce >= 0.75 and ce < 1.0:
                        cerate = 3
                    elif ce >= 0.5 and ce < 0.75:
                        cerate = 2
                    elif ce < 0.5:
                        cerate = 1
                except:
                    cerate = 0
                    continue
            else:
                cerate = 0
            print(cerate)
if module == 9:
    print(fullfcf)
