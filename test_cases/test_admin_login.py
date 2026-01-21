from selenium import webdriver
from base_page.login_admin_page import LOGIN
from utilities.read_properties import Read_config
class Test1_admin_login:
    # url=r'https://admin-demo.nopcommerce.com/login?returnUrl=%2Fadmin%2F'
    user_name=Read_config.get_username()
    pwd=Read_config.get_password()

    def test_verification(self,setup):
        self.driver=setup

        # self.driver=webdriver.Chrome()
        # self.driver.get(self.url)
        act_title=self.driver.title
        exp_title="nopCommerce demo store. Login"
        if act_title==exp_title:
            assert True
            # self.driver.close()
        else:
            self.driver.save_screenshot('.\\screenshots\\test_verification.png')
            assert False

    def test_login(self,setup):
        self.driver=setup

        self.admin = LOGIN(self.driver)
        # self.driver=webdriver.Chrome()
        # self.driver.get(self.url)

        self.admin.enter_un(self.user_name)
        self.admin.enter_pwd(self.pwd)
        self.admin.login_button()
        # act_text_dashbord=" Dashboard "
        if self.driver.current_url=='https://admin-demo.nopcommerce.com/admin/':
            self.driver.save_screenshot('.\\screenshots\\test_login.png')
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot('.\\screenshots\\test_login.png')
            assert False



