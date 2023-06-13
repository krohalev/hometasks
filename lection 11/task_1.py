# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from selenium import webdriver
from selenium.webdriver.common.by import By

sbis_site = 'https://sbis.ru/'
driver = webdriver.Chrome()
try:
    print('Переходим на сайт')
    driver.get(sbis_site)
    print('Перейти в раздел Контакты')
    contacts = driver.find_element(By.CSS_SELECTOR, '.sbisru-Header__menu-item-1')
    contacts.click()
    print('Клик по банеру Тензор')
    baner = driver.find_element(By.CSS_SELECTOR, '.sbisru-Contacts__logo-tensor')
    baner.click()
    print('переход на tensor.ru')
    driver.switch_to.window(driver.window_handles[1])
    print('Проверка наличия блока новости "Сила в людях"')
    news = driver.find_element(By.CSS_SELECTOR,
                               ".tensor_ru-Index__block4-content "
                               "[class='tensor_ru-Index__card-title tensor_ru-pb-16']")
    assert news.text == 'Сила в людях'
    print('Переход в блок "Подробнее", должен открыться https://tensor.ru/about')
    about = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__card-text [href="/about"]')
    about.location_once_scrolled_into_view
    about.click()
    assert "https://tensor.ru/about" in driver.current_url, "Неверный сайт"
    print('SUCCESS')

finally:
    driver.quit()
