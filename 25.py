from selenium import webdriver
from time import sleep
driver = webdriver.Chrome(executable_path="/Users/shaishabtai/Downloads/chromedriver_mac_arm64/chromedriver")
#driver.get("https://github.com")
driver.get("file:///Users/shaishabtai/Downloads/tip_calc/index.html")
billamt = driver.find_element(by="id", value="billamt")
billamt.send_keys("100")
s = driver.find_element(by="xpath", value="//*[@id=\"serviceQual\"]/option[5]")
s.click()
sound = driver.find_element(by="xpath", value="//*[@id=\"soundQual\"]/option[3]")
sound.click()
peopleamt = driver.find_element(by="id", value="peopleamt")
peopleamt.send_keys("5")
driver.find_element(by="id", value="calculate").click()
expected = "4.00"
actual = driver.find_element(by="id", value="tip").text
if expected == actual:
    print("Tip calculation is OK!")
assert expected == actual
sleep(5)
driver.close()