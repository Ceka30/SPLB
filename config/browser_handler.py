from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def setup_chrome_driver():
    chrome_options = ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--log-level=3")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    # driver = webdriver.Chrome(options=chrome_options)

    return webdriver.Chrome(options=chrome_options)


def setup_edge_driver():
    edge_options = EdgeOptions()
    edge_options.add_argument("--window-size=1920,1080")
    edge_options.add_argument("--disable-web-security")
    edge_options.add_argument("--allow-running-insecure-content")
    edge_options.add_argument("--remote-allow-origins=*")
    return edge_options


def setup_firefox_driver():
    firefox_options = FirefoxOptions()
    firefox_options.add_argument("--width=1920")
    firefox_options.add_argument("--height=1080")
    return firefox_options


def setup_safari_driver():
    safari_options = webdriver.SafariOptions()
    return safari_options


browser_handler = {
    "chrome": setup_chrome_driver,
    "edge": setup_edge_driver,
    "firefox": setup_firefox_driver,
    "safari": setup_safari_driver,
}
