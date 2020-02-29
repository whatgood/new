import selenium
from selenium import webdriver
from selenium.webdriver import ChromeOptions

option=ChromeOptions()
option.add_argument('user-agent="Mozilla/5.0 (iPod; U; CPU iPhone OS 2_1 like Mac OS X; ja-jp) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5F137 Safari/525.20"')
prefs = {'profile.managed_default_content_settings.images': 2}
option.add_experimental_option('prefs',prefs)
c=webdriver.Chrome(chrome_options=option)
c.maximize_window()
c.get(r"https://www.gtloli.net/forum.php?mod=forumdisplay&fid=84&mobile=1")
