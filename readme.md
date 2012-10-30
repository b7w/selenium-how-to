Selenium How To
===============

It is simple web application for testing purpose with selenium tool [Selenium](http://seleniumhq.org/).
Plus [how to](https://bitbucket.org/B7W/seleniumhowto/src/default/docs) with explaining of code, in russian.
It is written with python [bottle](http://bottlepy.org/) mini framework,
and twitter [bootstrap](http://twitter.github.com/bootstrap/) front-end framework.

Dependencies are already included. All code running on python 3.
*Note, selenium library is ported to third version.*

Run
---

You can esay run web server by calling *cd src*; *python server.py*. And tests *python tests/example[123].py*.
Or just run *python runner.py* - simle gui app. *Need tkinter lib on linux.*

Описание
--------

[docs/intro.md](https://bitbucket.org/B7W/seleniumhowto/src/default/docs/intro.md)
 - вступление

[docs/setup.md](https://bitbucket.org/B7W/seleniumhowto/src/default/docs/setup.md)
 - настройка среды и запуск

[docs/html.md](https://bitbucket.org/B7W/seleniumhowto/src/default/docs/html.md)
 - базовые понятия HTML

Разбор тестов
-------------

[docs/tests/base.md](https://bitbucket.org/B7W/seleniumhowto/src/default/docs/tests/base.md)
 - абстрактный тестовый случай

[docs/tests/example1.md](https://bitbucket.org/B7W/seleniumhowto/src/default/docs/tests/example1.md)
 - обход ссылок на странице

[docs/tests/example2.md](https://bitbucket.org/B7W/seleniumhowto/src/default/docs/tests/example2.md)
 - работа с базовыми контролами

[docs/tests/example3.md](https://bitbucket.org/B7W/seleniumhowto/src/default/docs/tests/example3.md)
 - некоторое подобие [twitter.com](https://twitter.com)