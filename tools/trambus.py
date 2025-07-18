from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_trambus_schedule(stop_id: str):
    url = f"https://jakdojade.pl/krakow/Dworzec Główny Zachód/Wawel?fn=Dworzec Główny Zachód&tn=Wawel&tc=50.054456:19.939759&fc=50.06768:19.94523&fsn=Dworzec Główny Zachód&tsn=Wawel&ft=LOCATION_TYPE_STOP&tt=LOCATION_TYPE_STOP&d=17.02.19&h=16:35&aro=1&t=1&rc=3&ri=1&r=0"

    firefox_options = Options()
    firefox_options.add_argument("--headless") 
    firefox_options.add_argument("--disable-gpu")

    driver = webdriver.Firefox(options=firefox_options)

    try:
        driver.get(url)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        page_content = driver.page_source
        return page_content
    except Exception as e:
        return {
            "status": "error", 
            "message": f"Unexpecter error: {str(e)}"
        }

    finally:
        driver.quit()