class LOGIN:
    un_id='Email'
    pwd_id='Password'
    login_xpath='//button[@type="submit"]'

    def __init__(self,driver):
        self.driver=driver
    def enter_un(self,username):
        self.driver.find_element('id', self.un_id).clear()
        self.driver.find_element('id',self.un_id).send_keys(username)
    def enter_pwd(self,password):
        self.driver.find_element('id', self.pwd_id).clear()
        self.driver.find_element('id',self.pwd_id).send_keys(password)
    def login_button(self):
        self.driver.find_element('xpath',self.login_xpath).click()