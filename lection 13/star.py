from atf import *
from saby_pages import *



class TestPlansList(TestCaseUI):

    @classmethod
    def setUpClass(cls):
        """Авторизация"""
        login = cls.config.get('LOGIN')
        password = cls.config.get('PASSWORD')
        sbis_link = cls.config.get('SBIS_ONLINE_LINK')

        cls.page = PlansRegistry(cls.driver)
        cls.browser.open(sbis_link)
        log('Авторизация')
        sbis_login = AuthPage(cls.driver)
        sbis_login.login_input.type_in(login + Keys.ENTER)
        sbis_login.password_input.type_in(password + Keys.ENTER).should_not_be(Visible)

    def setUp(self):
        log('Переход в Планы работ')
        self.browser.open('https://fix-online.sbis.ru/page/plans')

    def test_registry_plan(self):
        """Проверить, что в реестре отображается шкала выполнения (2 зеленых прямоугольника, 2 жёлтых и 4 серых)"""

        log('Проверка отображения цветов на шкале выполнения плана')
        self.page.scale.item(1).should_be(CssClass('controls-StateIndicator__sector1'))
        self.page.scale.item(2).should_be(CssClass('controls-StateIndicator__sector1'))
        self.page.scale.item(3).should_be(CssClass('controls-StateIndicator__sector2'))
        self.page.scale.item(4).should_be(CssClass('controls-StateIndicator__sector2'))
        self.page.scale.item(5).should_be(CssClass('controls-StateIndicator__emptySector'))
        self.page.scale.item(6).should_be(CssClass('controls-StateIndicator__emptySector'))
        self.page.scale.item(7).should_be(CssClass('controls-StateIndicator__emptySector'))
        self.page.scale.item(8).should_be(CssClass('controls-StateIndicator__emptySector'))

    def test_get_link(self):
        """Получить ссылку в буфер обмена и открыть её в новой вкладке (эталонный url НЕ использовать). Проверить наличие 4 пунктов и их статусы."""

        log('Открыть план в новой вкладке')
        self.page.plan.mouse_over()
        self.page.controls_button.click()
        self.page.menu_button.item(with_text='Открыть в новой вкладке').click()
        self.browser.switch_to_opened_window()

        log('Проверка эталонных пунктов и их статусов')
        self.page.paragraph_one.should_be(ExactText('Выполнен'))
        self.page.status_completed.should_be(Displayed)
        self.page.paragraph_two.should_be(ExactText('Готово'))
        self.page.status_ready.should_be(Displayed)
        self.page.paragraph_three.should_be(ExactText('В работе'))
        self.page.status_in_work.should_be(Displayed)
        self.page.paragraph_four.should_be(ExactText('Не выполнен'))
        self.page.status_not_done.should_be(Displayed)

    def tearDown(self):
        self.browser.close_windows_and_alert()
