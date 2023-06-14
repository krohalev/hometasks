from atf import *
from atf.ui import *
from saby_pages import *



class TestSendMessage(TestCaseUI):

    def test_01_sending_message(self):
        """Отправка сообщения самому себе, и последующие удаление этого сообщения"""
        login = self.config.get('LOGIN')
        password = self.config.get('PASSWORD')
        sbis_link = self.config.get('SBIS_ONLINE_LINK')
        person_name = self.config.get('PERSON_NAME')
        message = self.config.get('MESSAGE')

        self.browser.open(sbis_link)
        log('Авторизация')
        sbis_login = AuthPage(self.driver)
        sbis_login.login_input.type_in(login + Keys.ENTER)
        sbis_login.password_input.type_in(password + Keys.ENTER).should_not_be(Visible)

        log('Переход в Контакты')
        self.browser.open('https://fix-online.sbis.ru/page/dialogs')


