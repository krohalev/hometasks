from atf.ui import *


class AuthPage(Region):
    login_input = TextField(By.CSS_SELECTOR, "[name='Login']", 'Логин')
    password_input = TextField(By.CSS_SELECTOR, "[name='Password']", 'Пароль')


class MainPage(Region):
    accordion = CustomList(By.CSS_SELECTOR, "span.NavigationPanels-Accordion__title", 'Аккордеон')
    accordion_subtitle_head = Link(By.CSS_SELECTOR, ".NavigationPanels-SubMenu__headTitle", 'Раздел')


class TaskPage(Region):
    create_new_button = Button(By.CSS_SELECTOR, '.icon-RoundPlus', 'Создать')
    accept_button = Button(By.CSS_SELECTOR, ".controls-Popup .controls-BaseButton", 'Принять')
    send_button = Button(By.CSS_SELECTOR, ".icon-BtArrow", 'Отправить')
    delete_button = Button(By.CSS_SELECTOR, ".controls-icon_style-danger", 'Удалить')

    create_new_button_menu = CustomList(By.CSS_SELECTOR, ".controls-Menu__row", 'Меню "Создать"')
    sent_messages = CustomList(By.CSS_SELECTOR, '.msg-dialogs-item p', 'Сообщения в реестре')
    main_tabs = CustomList(By.CSS_SELECTOR, ".sabyPage-MainLayout__tabs-item", 'Вкладки')
    folders_list = CustomList(By.CSS_SELECTOR, ".controls-ListEditor__columns", 'Папки')
    current_folder = CustomList(By.CSS_SELECTOR, ".controls-Grid__row-cell_selected__first-master", 'Текущая папка')
    tasks_list = CustomList(By.CSS_SELECTOR, ".edws-MainColumn", 'Задачи')
    tasks_info = CustomList(By.CSS_SELECTOR, ".controls-EditableArea__Text__inner", 'Дата и номер')

    create_name_input = TextField(By.CSS_SELECTOR, ".controls-Popup .controls-InputBase__field", 'Название')
    top_area_search = TextField(By.CSS_SELECTOR, ".controls-StackTemplate__top-area-content "
                                                 ".controls-Search__nativeField_caretEmpty", 'Поиск')
    sending_message_textbox = TextField(By.CSS_SELECTOR, "[role='textbox']", 'Сообщение')

    top_area_search_result = Element(By.CSS_SELECTOR, ".person-BaseInfo__line span[data-qa='person-Information__fio']",
                                     'Результат')
    marker = Element(By.CSS_SELECTOR, ".controls-Grid__row-cell_selected__first-master>"
                                      ".controls-ListView__itemV_marker", 'Маркер')
    task_executor = Element(By.CSS_SELECTOR, ".edws-StaffChooser__itemTpl-name", 'Исполнитель')
    task_author = Element(By.CSS_SELECTOR, ".edo3-Sticker__active", 'Автор')
    task_description = Element(By.CSS_SELECTOR, ".richEditor_Base_textContainer p", 'Описание')

    current_tab = Link(By.CSS_SELECTOR, ".controls-Tabs__item_view_selected", 'Текущая вкладка')