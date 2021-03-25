from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd

login_url = 'sample.com'

data = {
    'username': 'MY_USER',
    'password': 'MY_PASS',
}



def openDriver():
    # i put some security measures so website can't detect that u use selenium, just incase!
    options = webdriver.ChromeOptions()
    options.add_experimental_option("useAutomationExtension", False)
    options.add_argument("--headless")
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-features=NetworkService") ##this did it for me
    options.add_argument("--window-size=1920x1080")
    options.add_argument("--disable-features=VizDisplayCompositor")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
            Object.defineProperty(navigator, 'webdriver', {
            get: () => undefined
            })
        """
    })
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
            Object.defineProperty(navigator, 'plugins', {
            get: () => '[1,2,3]'
            })
        """
    })
    return driver
            
# open driver
driver = openDriver()

# open login page
driver.get(login_url)

# type username
userBox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH ,'//*[@id="user_id"]')))
userBox.send_keys(data['username'])

# click on the continue button
contineButton = driver.find_element_by_xpath('//*[@id="login_user_form"]/div[2]/button')
contineButton.click()

# type password
passBox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH ,'//*[@id="password"]')))
passBox.send_keys(data['password'])

# click on the login button
loginButton = driver.find_element_by_xpath('//*[@id="action-complete"]')
loginButton.click()


# scrape url

report_final = []


url='sample.com'

i = 0
for x in range(0,300):
    
    driver.get(url+str(i))
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    content = soup.find_all('table', class_='andes-table table table-sticky')

    table = soup.find("table", { "class" : "andes-table table table-sticky" })
    for row in table.findAll("tr"):
        cells = row.findAll("td")
        if len(cells) == 9:
            td = cells[0].find(text=True)
            process = cells[1].find(text=True)
            tp = cells[2].find(text=True)
            inventory_id = cells[3].find(text=True)
            qty = cells[4].find(text=True)
            origem = cells[5].find(text=True)
            destino = cells[6].find(text=True)
            data = cells[7].find(text=True)
            

            movements_report = {
                'td':td,
                'process':process,
                'tp':tp,
                'inventory_id':inventory_id,
                'qty':qty,
                'origem':origem,
                'destino':destino,
                'data':data
            

            

            }
            report_final.append(movements_report)
    df = pd.DataFrame(report_final)
    df['data'] = df['data'].str.replace('\n', '|', regex=False)
    df.to_csv('v11.csv', index=False)
    i = i + 1000
    time.sleep(3)

    login_url = 'sample.com'

    data = {
        'username': 'MY_USER',
        'password': 'MY_PASS',
    }



    def openDriver():
        # i put some security measures so website can't detect that u use selenium, just incase!
        options = webdriver.ChromeOptions()
        options.add_experimental_option("useAutomationExtension", False)
        options.add_argument("--headless")
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-features=NetworkService") ##this did it for me
        options.add_argument("--window-size=1920x1080")
        options.add_argument("--disable-features=VizDisplayCompositor")
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(10)
        driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": """
                Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
                })
            """
        })
        driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": """
                Object.defineProperty(navigator, 'plugins', {
                get: () => '[1,2,3]'
                })
            """
        })
        return driver
            
    
    driver.close()
    # open driver
    driver = openDriver()

    # open login page
    driver.get(login_url)

    # type username
    userBox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH ,'//*[@id="user_id"]')))
    userBox.send_keys(data['username'])

    # click on the continue button
    contineButton = driver.find_element_by_xpath('//*[@id="login_user_form"]/div[2]/button')
    contineButton.click()

    # type password
    passBox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH ,'//*[@id="password"]')))
    passBox.send_keys(data['password'])

    # click on the login button
    loginButton = driver.find_element_by_xpath('//*[@id="action-complete"]')
    loginButton.click()

    


print(df.head())




print(len(report_final))
print(soup.title)



# close driver
driver.close()
