# SF_module_28
Итоговый проект
Вводные данные: Ссылка на требования по проекту --- https://docs.google.com/document/d/14TRuoYG8JXlLCMXuesBXrbNK7OefVxMW/edit?usp=share_link&ouid=102111731768085493149&rtpof=true&sd=true Объект тестирования: --- страницы Авторизации/Регистрации/Восстановления пароля личного кабинета Росстелеком. Ссылка на ЛК Ростелеком: --- https://b2c.passport.rt.ru

По заданию тестирования необходимо:
Протестировать требования.
Разработать тест-кейсы (не менее 15).
Провести автоматизированное тестирование продукта (не менее 15 автотестов). Заказчик ожидает по одному автотесту на каждый написанный тест-кейс. Оформите свой набор автотестов в GitHub.
Оформить описание обнаруженных дефектов ( составить баг-репорты). Во время обучения вы работали с разными сервисами и шаблонами, используйте их для оформления тест-кейсов и обнаруженных дефектов. (если дефекты не будут обнаружены, то составить описание трех дефектов).
С тест-кейсами и описанными багами/дефектами/недостатками можно ознакомиться по ссылке: https://docs.google.com/spreadsheets/d/1CU5Xmf_Fw2S5FCXEk7YSDiR-fN6AT1trSg8YaqBxQAE/edit?usp=sharing

Проект выполнен с помощью библиотек Pytest и Selenium

Все тесты находятся в папке tests, файл test_rostelecom.py

Так же в папке tests находится файл consts.py, содержащий тестовые данные и локаторы

Для работы автотестов необходимы библиотеки Pytest и Selenium и webdriver Selenium для Chrome 108 версии Запустить тесты можно через прописав:
python -m pytest -v --driver Chrome --driver-path <Путь до вебдрайвера>\chromedriver.exe test_rostelecom.py Или средствами PyCharm через Run.
