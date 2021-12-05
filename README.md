# Сокращение ссылок с помощью сервиса Bitly

Данная программа, используя сервис Bitly, позволяет:

- сокращать обычные ссылки пользователя до коротких ссылок вида [bit.ly/3k7Ybkj]
- показывать количество переходов по коротким ссылкам

## Требование к окружению

Программа написана на Python 3.8.

Программа использует следующие зависимости:

- python-dotenv==0.19.2
- requests==2.22.0

Для установки зависимостей запустите `pip`:

``` python
pip install -r requirements.txt
```

## Переменные окружения

Для запуска программы необходимо настроить переменные окружения. Для этого в папке проекта создайте файл `.env`, куда поместите чувствительные данные (ключи API) в формате `ПЕРЕМЕННАЯ=значение`.

Образец создания переменной окружения (значения вымышленные):

``` python
BITLY_API_TOKEN = 'c4e3b33aff5368e83bbcf6be66125ee22sd77s87ds7ss7d'
```

Действующий TOKEN для работы с API можно бесплатно получить на сайте [bitly](https://dev.bitly.com/).

## Как запустить программу

В терминале или программной среде разработки Python запустите файл `main.py` с указанием длинной или короткой ссылки, в зависимости от того, какой результат хотите получить:

- запуск программы для получения короткой ссылки
  
``` python
python3 main.py https://dvmn.org/modules/
```

- запуск программы для получения количества переходов по короткой ссылке

``` python
python3 main.py https://bit.ly/3k7Ybkj
```

В ответ будут показаны либо сокращённая ссылка, либо количество переходов, соответственно.

## Примеры использования

Если, например, в терминале ввести `python3 main.py https://dvmn.org/modules/`, то программа сократит ссылку до '<https://bit.ly/3k7Ybkj>`:

![long-argparse](https://user-images.githubusercontent.com/37913906/144381019-3b1aebed-72da-408f-a4de-127d5b5af077.png)

Если в терминале ввести 'python3 main.py <https://bit.ly/3k7Ybkj>', то программа покажет количество переходов по ней:

![short-argparse](https://user-images.githubusercontent.com/37913906/144381060-794db373-6ffd-4a78-bf10-1a9866a8d522.png)

## Цель проекта

Программа написана в образовательных целях в рамках обучения на курсе python-разработки [dvmn.org](https://dvmn.org/).
