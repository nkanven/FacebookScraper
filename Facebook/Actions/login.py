from RPA.Browser.Selenium import Selenium
import time


class Login:

    def __init__(self):
        self._browser = Selenium(auto_close=False)

    def connect(self) -> bool:
        try:
            self._browser.open_available_browser('facebook.com')
            self._browser.input_text_when_element_is_visible("id:email", "nkanven@yahoo.fr")
            self._browser.input_text_when_element_is_visible("id:pass", "@Meanselme89")
            submit = self._browser.find_element("name:login")
            submit.click()

            while True:
                if str(self._browser.get_location()).find('checkpoint') != -1:
                    print("Please confirm Two factor authentication")
                else:
                    break
                time.sleep(10)

            # TODO: Close alert box
            # self._browser.is_alert_present(action="DISMISS")

            return True

        except Exception:
            return False
