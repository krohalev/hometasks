from atf import *
from saby_pages import *



class TestContactsList(TestCaseUI):

    @classmethod
    def setUpClass(cls):
        """Авторизация"""
        login = cls.config.get('LOGIN')
        password = cls.config.get('PASSWORD')
        sbis_link = cls.config.get('SBIS_ONLINE_LINK')

        cls.page = ContactsRegistry(cls.driver)
        cls.browser.open(sbis_link)
        log('Авторизация')
        sbis_login = AuthPage(cls.driver)
        sbis_login.login_input.type_in(login + Keys.ENTER)
        sbis_login.password_input.type_in(password + Keys.ENTER).should_not_be(Visible)

    def setUp(self):
        log('Переход в Контакты')
        self.browser.open('https://fix-online.sbis.ru/page/dialogs')

    def test_move_record(self):
        """Переместить запись в другую папку и проверить перемещение (убедиться в: наличии в папке и увеличении счётчика). И вернуть обратно."""

        log('Перемещение сообщения в папку')
        self.page.sent_messages.mouse_over()
        self.page.controls_button.click()
        self.page.menu_button.item(with_text='Переместить').click()
        self.page.move_in_folder.click()

        log('Сообщение находится в другой папке')
        self.page.tiny_folder.should_be(ExactText('Крохалев'))
        self.page.count_folder.should_be(ExactText('1'))
        self.page.folder_test.click()
        self.page.sent_messages.should_be(ExactText('Мусорит123'))

        log('Удаление сообщения из папки')
        self.page.folder_all_messages.click()
        delay(3)
        self.page.delete_tiny_folder.click()

    def test_comparison(self):
        """Проверить, что дата сообщения в реестре Диалоги совпадает с датой в Чатах"""

        log('Дата создания совпадает в реестрах "Диалоги" и "Чаты"')
        delay(5)
        self.page.message_data_info.item(contains_text='20 июн 14:39').should_be(Displayed)
        self.page.tab_chats.click()
        self.page.message_chats_data_info.item(contains_text='20 июн 14:39').should_be(Displayed)
        self.page.tab_dialog.click()

    def test_tagging(self):
        """Пометить сообщение эталонным тегом. Убедиться, что тег появился на сообщении, а счётчик тегов увеличился. Снять тег и проверить."""

        log('Пометить сообщение тегом')
        delay(5)
        self.page.folder_all_messages.click()
        self.page.sent_messages.mouse_over()
        self.page.controls_button.click()
        self.page.menu_button.item(with_text='Пометить').click()
        self.page.tag.click()

        log('Проверить отметку тегом и увеличение счетчика тега')
        self.page.tiny_tag.should_be(ExactText('тег для ат'))
        self.page.count_tag.should_be(ExactText('1'))

        log('Удалить тег и проверить, что он удалился')
        self.page.delete_tiny_tag.click()
        self.page.tiny_tag.should_not_be(Visible)

    def tearDown(self):
        self.browser.close_windows_and_alert()
