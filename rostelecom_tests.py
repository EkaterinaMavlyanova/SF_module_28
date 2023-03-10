from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

import time
import consts


def get_driver():

    options = webdriver.ChromeOptions()
    options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en-GB'})
    driver = webdriver.Chrome(executable_path=consts.driverPathChrome, chrome_options=options)

    driver.get(consts.baseUrl)
    driver.maximize_window()
    wait = WebDriverWait(driver, 30)
    assert wait.until(EC.presence_of_element_located((By.XPATH, '//h1[@class="card-container__title"]'))).text == 'Авторизация'
    return driver, wait


def test_correct_redirect_to_register(): # TK-001 Проверка открытия страницы регистрации
    driver, wait = get_driver()
    wait.until(EC.presence_of_element_located((By.ID, 'kc-register'))).click()
    time.sleep(5)
    assert wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'card-container__title'))).text == 'Регистрация'
    driver.quit()

def test_registration_phoneNumber(): # TK-002 Проверка регистрации по номеру телефона - страница Регистрации
    driver, wait = get_driver()
    actionChain = ActionChains(driver)

    wait.until(EC.presence_of_element_located((By.ID, 'kc-register'))).click()
    assert wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'card-container__title'))).text == 'Регистрация'

    wait.until(EC.presence_of_element_located((By.NAME, 'firstName'))).click()
    actionChain.send_keys('Кирилица').perform()
    wait.until(EC.presence_of_element_located((By.NAME, 'lastName'))).click()
    actionChain.send_keys('Кирилица').perform()
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input#address'))).click()
    actionChain.send_keys('+79097805555').perform()
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input#password'))).click()
    actionChain.send_keys('Latinica2').perform()
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input#password-confirm'))).click()
    actionChain.send_keys('Latinica2').perform()
    time.sleep(2) # Для наглядности - в реальности тестирования закоментировать
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div:nth-of-type(4) > div > div > div:nth-of-type(2) > svg'))).click()
    time.sleep(2) # Для наглядности - в реальности тестирования закоментировать
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div:nth-of-type(4) > div:nth-of-type(2) > div > div:nth-of-type(2) > svg > path'))).click()
    time.sleep(5) # Для наглядности - в реальности тестирования закоментировать
    driver.find_element(By.NAME, 'register').click()
    time.sleep(3) # Для наглядности - в реальности тестирования закоментировать

    confirmPage = wait.until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Подтверждение телефона')]"))).text
    assert confirmPage == 'Подтверждение телефона'
    driver.quit()


def test_registration_email(): # TK-003 проверка регистрации по Е-майлу  - страница Регистрации
    driver, wait = get_driver()
    actionChain = ActionChains(driver)

    wait.until(EC.presence_of_element_located((By.ID, 'kc-register'))).click()
    assert wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'card-container__title'))).text == 'Регистрация'

    wait.until(EC.presence_of_element_located((By.NAME, 'firstName'))).click()
    actionChain.send_keys('КирилицаА').perform()
    wait.until(EC.presence_of_element_located((By.NAME, 'lastName'))).click()
    actionChain.send_keys('КирилицаБ').perform()
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input#address'))).click()
    actionChain.send_keys('test@testtest5555.ru').perform()
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input#password'))).click()
    actionChain.send_keys('Latinica2').perform()
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input#password-confirm'))).click()
    actionChain.send_keys('Latinica2').perform()
    time.sleep(2) # Для наглядности - в реальности тестирования закоментировать
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div:nth-of-type(4) > div > div > div:nth-of-type(2) > svg'))).click()
    time.sleep(2) # Для наглядности - в реальности тестирования закоментировать
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div:nth-of-type(4) > div:nth-of-type(2) > div > div:nth-of-type(2) > svg > path'))).click()
    time.sleep(5) # Для наглядности - в реальности тестирования закоментировать
    driver.find_element(By.NAME, 'register').click()
    time.sleep(3) # Для наглядности - в реальности тестирования закоментировать

    confirmPage = wait.until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Подтверждение email')]"))).text
    assert confirmPage == 'Подтверждение email'
    driver.quit()


def test_register_firstName_and_lastName(): # TK-004 Проверка поля "ИМЯ" и "Фамилия" на коррктность вводимых данных
                                                    # - страница Регистрации
    driver, wait = get_driver()
    actionChain = ActionChains(driver)

    wait.until(EC.presence_of_element_located((By.ID, 'kc-register'))).click()
    assert wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'card-container__title'))).text == 'Регистрация'

    firstNameInput = wait.until(EC.presence_of_element_located((By.NAME, 'firstName')))
    lastNameInput = wait.until(EC.presence_of_element_located((By.NAME, 'lastName')))


    elementsDictionary = {
        'firstName': firstNameInput,
        'lastName': lastNameInput
    }

    for key in consts.registerKeysDict:
        values = consts.registerKeysDict[key]

        actionChain.click(elementsDictionary[key]).perform()

        for j in range(len(values)):
            actionChain.send_keys(values[j]).perform()
            driver.find_element(By.XPATH, "//p[contains(text(),'Личные данные')]").click()

            if j < len(values) - 1:
                if j >= 1:
                    pass
                else:
                    error = wait.until(EC.presence_of_element_located(
                        (By.CSS_SELECTOR, 'span.rt-input-container__meta.rt-input-container__meta--error'))).text
                time.sleep(1)  # Для наглядности - в реальности тестирования закоментировать
                assert error == consts.registerErrorsName
                actionChain.double_click(elementsDictionary[key]).click_and_hold().send_keys(Keys.DELETE).perform()
    driver.quit()


def test_register_email_and_phone(): # TK-005 Проверка полей "Email или Мобильный телефон", на корректность ввода данных
                                     # - страница Регистрации
    driver, wait = get_driver()
    actionChain = ActionChains(driver)

    wait.until(EC.presence_of_element_located((By.ID, 'kc-register'))).click()
    assert wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'card-container__title'))).text == 'Регистрация'

    addressNameInput = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input#address')))

    values = consts.registerFormKeysAddress
    actionChain.click(addressNameInput).perform()

    for j in range(len(values)):
        actionChain.send_keys(values[j]).perform()
        driver.find_element(By.XPATH, "//p[contains(text(),'Личные данные')]").click()

        if j < len(values) - 1:
            if j >= 1:
                pass
            else:
                error = wait.until(EC.presence_of_element_located(
                        (By.CSS_SELECTOR, 'span.rt-input-container__meta.rt-input-container__meta--error'))).text
            assert error == consts.registerErrorsAddress
            time.sleep(1)
            actionChain.double_click(addressNameInput).click_and_hold().send_keys(Keys.DELETE).perform()
            time.sleep(1)
    driver.quit()


def test_register_password():  # TK-006 Проверка поля "Пароль" на корректность вводимых данных
    driver, wait = get_driver()
    actionChain = ActionChains(driver)

    wait.until(EC.presence_of_element_located((By.ID, 'kc-register'))).click()
    assert wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'card-container__title'))).text == 'Регистрация'

    passNameInput = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input#password')))
    time.sleep(2) # Для наглядности - в реальности тестирования закоментировать
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                               'section#page-right > div > div > div > form > div:nth-of-type(4) > div > div > div:nth-of-type(2) > svg'))).click()

    values = consts.registerFormPassword
    actionChain.click(passNameInput).perform()


    for j in range(len(values)):
        actionChain.send_keys(values[j]).perform()
        driver.find_element(By.XPATH, "//p[contains(text(),'Личные данные')]").click()

        if j < len(values) - 1:
            if j >= 1:
                pass
            else:
                error = wait.until(EC.presence_of_element_located(
                        (By.CSS_SELECTOR, 'span.rt-input-container__meta.rt-input-container__meta--error'))).text

            time.sleep(1)
            actionChain.double_click(passNameInput).click_and_hold().send_keys(Keys.DELETE).perform()
            time.sleep(1)
            assert error == consts.regErPass
    driver.quit()


def test_register_passwordConfirm(): # TK-007 Проверка поля "Проверка Пароля" на корректность вводимых данных
    driver, wait = get_driver()
    actionChain = ActionChains(driver)

    wait.until(EC.presence_of_element_located((By.ID, 'kc-register'))).click()
    assert wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'card-container__title'))).text == 'Регистрация'

    wait.until(EC.presence_of_element_located((By.NAME, 'firstName'))).click()
    actionChain.send_keys('КирилицаА').perform()
    wait.until(EC.presence_of_element_located((By.NAME, 'lastName'))).click()
    actionChain.send_keys('КирилицаБ').perform()
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input#address'))).click()
    actionChain.send_keys('+79097805555').perform()
    time.sleep(2)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                               'section#page-right > div > div > div > form > div:nth-of-type(4) > div > div > div:nth-of-type(2) > svg'))).click()
    time.sleep(1) # Для наглядности - в реальности тестирования закоментировать
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input#password'))).click()
    actionChain.send_keys('Latinica1').perform()
    time.sleep(1) # Для наглядности - в реальности тестирования закоментировать
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                               'section#page-right > div > div > div > form > div:nth-of-type(4) > div:nth-of-type(2) > div > div:nth-of-type(2) > svg > path'))).click()
    time.sleep(1) # Для наглядности - в реальности тестирования закоментировать
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input#password-confirm'))).click()
    actionChain.send_keys('Latinica2').perform()
    time.sleep(1) # Для наглядности - в реальности тестирования закоментировать
    driver.find_element(By.NAME, 'register').click()

    error = wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Пароли не совпадают')]"))).text
    assert error == 'Пароли не совпадают'
    driver.quit()


def test_click_forgotPassword(): # TK-008  Проверка перехода по ссылке "Забыл пароль"
    driver, wait = get_driver()
    time.sleep(2) # Для наглядности - в реальности тестирования закоментировать

    wait.until(EC.presence_of_element_located((By.XPATH, "//a[@id='forgot_password']"))).click()
    time.sleep(2) # Для наглядности - в реальности тестирования закоментировать

    assert wait.until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Восстановление пароля')]"))).text == 'Восстановление пароля'
    driver.quit()


def test_refresh_captcha(): # TK-009 Проверка обновление капчи на странице Восстановления пароля
    driver, wait = get_driver()
    actionChain = ActionChains(driver)
    time.sleep(2)  # Для наглядности - в реальности тестирования закоментировать

    wait.until(EC.presence_of_element_located((By.XPATH, "//a[@id='forgot_password']"))).click()
    assert wait.until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Восстановление пароля')]"))).text == 'Восстановление пароля'
    time.sleep(2)  # Для наглядности - в реальности тестирования закоментировать

    oldCaptcha = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'rt-captcha__image'))).get_attribute('src')
    actionChain.move_to_element(driver.find_element(By.CLASS_NAME, 'rt-captcha__reload')).click().perform()
    time.sleep(2)  # Для наглядности - в реальности тестирования закоментировать

    driver.implicitly_wait(20)

    newCaptcha = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'rt-captcha__image'))).get_attribute('src')
    assert oldCaptcha != newCaptcha
    driver.quit()


def test_form_change(): # TK-010 Проверка изменения подсказки текста плейсхолдера в поле "Логин" при изменении
                        # способа авторизации формы авторизация
    driver, wait = get_driver()
    actionChain = ActionChains(driver)

    wait.until(EC.presence_of_element_located((By.XPATH, "//a[@id='forgot_password']"))).click()
    assert wait.until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Восстановление пароля')]"))).text == 'Восстановление пароля'
    tabButtons = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'rt-tab')))

    assert wait.until(EC.title_is('Ростелеком ID'))
    assert len(tabButtons) == 4

    for i in range(len(tabButtons)):
        actionChain.move_to_element(tabButtons[i]).click().perform()
        placeholderInput = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.rt-input__placeholder'))).text
        time.sleep(1)  # Для наглядности - в реальности тестирования закоментировать
        assert wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'rt-tab--active'))).text == driver.find_element(By.ID, consts.tabButtonsId[i]).text
        assert placeholderInput == consts.placeholderInputsValue[i]
    driver.quit()


def test_back_to_login(): # TK-011 Проверка функциональности кнопки "Вернуться назад", на странице Восстановление пароля
    driver, wait = get_driver()

    wait.until(EC.presence_of_element_located((By.XPATH, "//a[@id='forgot_password']"))).click()
    assert wait.until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Восстановление пароля')]"))).text == 'Восстановление пароля'
    time.sleep(1)  # Для наглядности - в реальности тестирования закоментировать

    wait.until(EC.presence_of_element_located((By.XPATH, "//button[@id='reset-back']"))).click()
    assert wait.until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Авторизация')]"))).text == 'Авторизация'
    time.sleep(2)  # Для наглядности - в реальности тестирования закоментировать
    driver.quit()


# TK-012
# Проверка автоматической смены таба при вводе - телефона/почты/лицевого счета/логина, на странице Авторизации
def test_correct_change_input():
    driver, wait = get_driver()
    actionChain = ActionChains(driver)

    tabButtons = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'rt-tab')))
    placeholderInput = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.rt-input__placeholder'))).text
    assert placeholderInput == consts.placeValue[0]

    for i in range(len(tabButtons)):
        actionChain.move_to_element(driver.find_element(By.ID, 'username')).click().perform()
        actionChain.send_keys(consts.sendedKeys[i]).perform()
        actionChain.move_to_element(driver.find_element(By.ID, 'password')).click().perform()
        activeTabButton = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, f'.rt-tabs .{consts.activeTab}')))
        assert activeTabButton.text == consts.tabTitlesAuth[i], driver.quit()

        time.sleep(2) # Имитация живого пользователя

        actionChain.double_click(driver.find_element(By.ID, 'username')).click_and_hold().send_keys(Keys.DELETE).perform()
        time.sleep(1)

    driver.quit()


def test_tg_chat(): # TK-013 Проверка перехода по ссылке, в чат Телеграм
    driver, wait = get_driver()
    actionChains = ActionChains(driver)
    chatTg = wait.until(EC.presence_of_element_located((By.ID, "widget_bar")))
    originalWindow = driver.current_window_handle
    actionChains.move_to_element(chatTg).perform()
    wait.until(EC.presence_of_element_located((By.XPATH, '//a[@class="alt-channel omnichat-theme-white svelte-1sezl8s"][2]'))).click()
    WebDriverWait(driver, 5).until(EC.number_of_windows_to_be(2))
    for window_handle in driver.window_handles:
        if window_handle != originalWindow:
            driver.switch_to.window(window_handle)
            break

    assert driver.current_url.__contains__('https://telegram.me/Rostelecom_ChatBot')
    time.sleep(3)  # Для наглядности - в реальности тестирования закоментировать
    driver.quit()


def test_viber_chat(): # TK-014 Проверка перехода по ссылке, в чат Viber
    driver, wait = get_driver()
    actionChains = ActionChains(driver)
    chatVb = wait.until(EC.presence_of_element_located((By.ID, "widget_bar")))
    originalWindow = driver.current_window_handle
    actionChains.move_to_element(chatVb).perform()
    wait.until(EC.presence_of_element_located((By.XPATH, '//a[@class="alt-channel omnichat-theme-white svelte-1sezl8s"][1]'))).click()
    WebDriverWait(driver, 5).until(EC.number_of_windows_to_be(2))
    for window_handle in driver.window_handles:
        if window_handle != originalWindow:
            driver.switch_to.window(window_handle)
            break
    assert driver.current_url.__contains__('https://chats.viber.com/Rostelecom')
    time.sleep(3)  # Для наглядности - в реальности тестирования закоментировать
    driver.quit()


def test_open_agreement(): # TK-015 Проверка функциональности всех ссылок Пользовательского соглажения
                                    # и Политики конфидециальности
    driver, wait = get_driver()
    originalWindow = driver.current_window_handle

    wait.until(EC.presence_of_element_located((By.LINK_TEXT, 'пользовательского соглашения'))).click()
    WebDriverWait(driver, 5).until(EC.number_of_windows_to_be(2))
    for window_handle in driver.window_handles:
        if window_handle != originalWindow:
            driver.switch_to.window(window_handle)
            break
    window_title = driver.execute_script("return window.document.title")
    time.sleep(3)  # Для наглядности - в реальности тестирования закоментировать
    assert window_title == 'User agreement'

    driver.close()

    driver.switch_to.window(originalWindow)
    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="rt-footer-agreement-link"]/span[1]'))).click()
    WebDriverWait(driver, 5).until(EC.number_of_windows_to_be(2))
    for window_handle in driver.window_handles:
        if window_handle != originalWindow:
            driver.switch_to.window(window_handle)
            break
    window_title = driver.execute_script("return window.document.title")
    time.sleep(3)  # Для наглядности - в реальности тестирования закоментировать
    assert window_title == 'User agreement'

    driver.close()

    driver.switch_to.window(originalWindow)
    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="rt-footer-agreement-link"]/span[2]'))).click()
    WebDriverWait(driver, 5).until(EC.number_of_windows_to_be(2))
    for window_handle in driver.window_handles:
        if window_handle != originalWindow:
            driver.switch_to.window(window_handle)
            break
    window_title = driver.execute_script("return window.document.title")
    time.sleep(3)  # Для наглядности - в реальности тестирования закоментировать
    assert window_title == 'User agreement'

    driver.quit()

# TK-016 Проверка перехода по ссылке, для авторизации через соц сеть Vk
def test_try_auth_with_vk():
    driver, wait = get_driver()
    wait.until(EC.presence_of_element_located((By.ID, 'oidc_vk'))).click()
    time.sleep(2)  # Для наглядности - в реальности тестирования закоментировать

    assert driver.current_url.__contains__('oauth.vk.com')
    driver.quit()

# TK-017 Проверка перехода по ссылке, для авторизации через соц сеть Ok
def test_try_auth_with_ok():
    driver, wait = get_driver()
    wait.until(EC.presence_of_element_located((By.ID, 'oidc_ok'))).click()
    time.sleep(2)  # Для наглядности - в реальности тестирования закоментировать

    assert driver.current_url.__contains__('connect.ok.ru')
    driver.quit()

# TK-018 Проверка перехода по ссылке, для авторизации через соц сеть Mail.ru
def test_try_auth_with_mail():
    driver, wait = get_driver()
    wait.until(EC.presence_of_element_located((By.ID, 'oidc_mail'))).click()
    time.sleep(2)  # Для наглядности - в реальности тестирования закоментировать

    assert driver.current_url.__contains__('connect.mail.ru')
    driver.quit()

# TK-019 Проверка перехода по ссылке, для авторизации через соц сеть Google
def test_try_auth_with_google():
    driver, wait = get_driver()
    wait.until(EC.presence_of_element_located((By.ID, 'oidc_google'))).click()
    time.sleep(2)  # Для наглядности - в реальности тестирования закоментировать

    assert driver.current_url.__contains__('accounts.google.com')
    driver.quit()

# TK-020 Проверка перехода по ссылке, для авторизации через соц сеть Yandex
def test_try_auth_with_yandex():
    driver, wait = get_driver()
    wait.until(EC.presence_of_element_located((By.ID, 'oidc_ya'))).click()
    time.sleep(2)  # Для наглядности - в реальности тестирования закоментировать

    assert driver.current_url.__contains__('oauth.yandex.ru')
    driver.quit()