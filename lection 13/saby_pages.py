from atf.ui import *
from controls import *



class AuthPage(Region):
    login_input = TextField(By.CSS_SELECTOR, "[name='Login']", 'Логин')
    password_input = TextField(By.CSS_SELECTOR, "[name='Password']", 'Пароль')


class ContactsRegistry(Region):
    sent_messages = CustomList(By.CSS_SELECTOR, '.msg-dialogs-item p', 'Конкретные сообщения')
    controls_button = Button(By.CSS_SELECTOR, '[data-qa="controls-itemActions__action null"]',
                                                                                        'Кнопки настройки сообщений')
    menu_button = CustomList(By.CSS_SELECTOR, '.controls-Menu__content_baseline', 'Кнопка в меню опций сообщений')
    move_in_folder = Button(By.CSS_SELECTOR, '[title="Крохалев"].controls-Grid__row-cell__content', 'Перемещение в папку')
    tiny_folder = CustomList(By.CSS_SELECTOR, '[title="Крохалев"].tag-base', 'Маленькая папка в сообщении')
    count_folder = CustomList(By.CSS_SELECTOR, '[data-qa="msg-folders-counter_total"]', 'Счетчик в папке')
    folder_test = ControlsListView(By.CSS_SELECTOR, '[title="Крохалев"].msg-entity-plain-text', 'Папка "Крохалев"')
    folder_all_messages = ControlsListView(By.CSS_SELECTOR, '[title="Все сообщения"].msg-entity-plain-text',
                                                                                                'Папка "Все сообщения')
    delete_tiny_folder = Button(By.CSS_SELECTOR, '.tags-base__close', 'Удаление маленькой папки из сообщения')
    message_data_info = CustomList(By.CSS_SELECTOR, '[data-qa="msg-entity-date"]', 'Дата сообщения в разделе "Диалоги')
    tab_chats = Element(By.CSS_SELECTOR, '[title="Чаты"]', 'Раздел "Чаты"')
    tab_dialog = Element(By.CSS_SELECTOR, '[title="Диалоги"]', 'Раздел "Диалоги"')
    message_chats_data_info = CustomList(By.CSS_SELECTOR, '[data-qa="msg-entity-date"]', 'Дата сообщения в разделе "Чаты"')
    tag = CustomList(By.CSS_SELECTOR, '[title="тег для ат"][style="max-width: 170px; min-width: 0px; cursor: pointer;"]',
                                                                                                            'Тег "тег для ат"')
    tiny_tag = CustomList(By.CSS_SELECTOR, '[title="тег для ат"][style="max-width: 170px; min-width: 40px; cursor: pointer;"]',
                                                                                            'Маленький тег в сообщении')
    count_tag = CustomList(By.CSS_SELECTOR, '.tags-base__countEntities', 'Счетчик тегов')
    delete_tiny_tag = CustomList(By.CSS_SELECTOR, '.tags-base__close', 'Удаление тега из сообщения')


class PlansRegistry(Region):
    scale = CustomList(By.CSS_SELECTOR, '.controls-StateIndicator__box', 'Шкала')

    plan = ControlsTreeGridView(By.CSS_SELECTOR, '.plan-List__detailsView-planName', 'План')
    controls_button = CustomList(By.CSS_SELECTOR, '[data-qa="controls-itemActions__action null"][tabindex="-1"]',
                                                                                        'Кнопки настройки сообщений')
    menu_button = CustomList(By.CSS_SELECTOR, '.controls-Menu__content-wrapper_width', 'Кнопка в меню опций сообщений')
    paragraph_one = CustomList(By.CSS_SELECTOR, '[title="Выполнен"]', 'Выполнен')
    paragraph_two = CustomList(By.CSS_SELECTOR, '[title="Готово"]', 'Готово')
    paragraph_three = CustomList(By.CSS_SELECTOR, '[title="В работе"]', 'В работе')
    paragraph_four = CustomList(By.CSS_SELECTOR, '[title="Не выполнен"]', 'Не выполнен')
    status_completed = CustomList(By.CSS_SELECTOR, '[title="Выполнен"]', 'Выполнен')
    status_ready = CustomList(By.CSS_SELECTOR, '[title="Готово"]', 'Готово')
    status_in_work = CustomList(By.CSS_SELECTOR, '[title="В работе"]', 'В работе')
    status_not_done = CustomList(By.CSS_SELECTOR, '[title="Не выполнен"]', 'Не выполнен')
