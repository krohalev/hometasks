from atf.ui import *


class TestSendMessage(TestCaseUI):

    def test_01_sending_message(self):
        """Отправка сообщения самому себе, и последующие удаление этого сообщения"""
