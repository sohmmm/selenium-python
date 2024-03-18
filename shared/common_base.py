from selenium import webdriver


class CommonBase:
    driver = None

    @classmethod
    def initialize(cls):
        if cls.driver is None:
            options = webdriver.ChromeOptions()
            options.add_experimental_option('detach', True)
            cls.driver = webdriver.Chrome(options)
            cls.driver.maximize_window()
            cls.driver.implicitly_wait(5)

    @classmethod
    def launch_browser(cls, url):
        cls.driver.get(url)

    @classmethod
    def quit_driver(cls):
        cls.driver.quit()


if __name__ == '__main__':
    x = CommonBase()
    x.launch_browser('https://www.google.com')
