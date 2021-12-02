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
```
pip install -r requirements.txt
```
Для изоляции чувствительных данных (ключей API) они убраны в переменную окружения `.env`.

## Как запустить программу

В программной среде разработки Python запустите файл:
```
python3 main.py
```
В ответ на предложение ввести ссылку, введите короткую или длинную (обычную) ссылку.

## Примеры использования

Если, например, при старте программы ввести длинную ссылку `https://dvmn.org/modules/`, то программа сократит её до 'https://bit.ly/3k7Ybkj`:


Если ввести короткую ссылку, то программа покажет количество переходов по ней:


## Цель проекта

Программа написана в образовательных целях в рамках обучения на курсе python-разработки [dvmn.org](https://dvmn.org/). 
