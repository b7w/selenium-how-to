Selenium How To
===============

It is simple web application for testing purpose with selenium tool [Selenium](http://seleniumhq.org/). Plus [how to](docs) with explaining of code, in russian. It is written with python [bottle](http://bottlepy.org/) mini framework, and twitter [bootstrap](http://twitter.github.com/bootstrap/) front-end framework.

Dependencies are already included. All code running on python 3. *Note, selenium library is ported to third version.*


Run
---
You can esay run web server by calling *cd src*; *python server.py*. And tests *python tests/example[123].py*. Or just run *python runner.py* - simle gui app. *Need tkinter lib on linux.*


Обратная связь
---------------
Вы всегда можете задать вопрос по электронной почте [black7white@ya.ru](mailto:black7white@ya.ru).
Если вы нашли какую-то ошибку, не поленитесь, добавьте ее в [issue tracker](https://github.com/b7w/selenium-how-to/issues).


Описание
--------
[docs/intro.md](docs/intro.md)
 - вступление

[docs/setup.md](docs/setup.md)
 - настройка среды и запуск

[docs/html.md](docs/html.md)
 - базовые понятия HTML

[docs/conclusion.md](docs/conclusion.md)
 - заключение


Разбор тестов
-------------
[docs/tests/base.md](docs/tests/base.md)
 - абстрактный тестовый случай

[docs/tests/example1.md](docs/tests/example1.md)
 - обход ссылок на странице

[docs/tests/example2.md](docs/tests/example2.md)
 - работа с базовыми контролами

[docs/tests/example3.md](docs/tests/example3.md)
 - некоторое подобие [twitter.com](https://twitter.com)


Лабораторные работы
-------------------
[docs/labs.md](docs/labs.md)
 - Немного заданий для выполнения


Дополнительно
-------------
В проект встроены библиотеки selenium driver и bottle.py распространяющиеся под лицензиями Apache license 2.0 и MIT License.