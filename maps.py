import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import os
import base64

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Emulator-5554',
    appPackage='com.google.android.apps.maps',
    appActivity='com.google.android.maps.MapsActivity',
    language='en',
    locale='US'
)

appium_server_url = 'http://127.0.0.1:4723'

class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, capabilities)

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_maps(self) -> None:
        self.driver.start_recording_screen()
        WebDriverWait(self.driver, 600).until(EC.presence_of_element_located((By.XPATH, '//*[@content-desc="Search here"]')))
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@content-desc="Search here"]')
        el.click()
        
        directory = '%s/' % os.getcwd()
        file_name = 'screenshot-correios-1.png'
        self.driver.save_screenshot(directory + file_name)

        
        WebDriverWait(self.driver, 600).until(EC.presence_of_element_located((By.XPATH, '//*[@resource-id="com.google.android.apps.maps:id/search_omnibox_edit_text"]')))
        actions = ActionChains(self.driver)
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@resource-id="com.google.android.apps.maps:id/search_omnibox_edit_text"]')
        el.click()
        el.send_keys("Teresopolis, RJ")
        actions.send_keys(Keys.ENTER)
        actions.perform()
        
        directory = '%s/' % os.getcwd()
        file_name = 'screenshot-maps-2.png'


        
        #WebDriverWait(self.driver, 600).until(EC.presence_of_element_located((By.XPATH, '//*[@text="Allow Maps to send you notifications?"]')))
        #el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Allow"]')
        #el.click()

        file_name = 'screenshot-maps-2.png'
        self.driver.save_screenshot(directory + file_name)
        
        WebDriverWait(self.driver, 600).until(EC.presence_of_element_located((By.XPATH, '//*[@resource-id="com.google.android.apps.maps:id/qu_sv_entrypoint_container"]')))

        filepath = os.path.join(directory, "screen_recording_maps.mp4")
        payload = self.driver.stop_recording_screen()
        with open(filepath, "wb") as fd:
            fd.write(base64.b64decode(payload))

if __name__ == '__main__':
    unittest.main()



