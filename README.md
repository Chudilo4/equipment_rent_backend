# Бэкэнд для сайта визитки
[![Django CI](https://github.com/Chudilo4/equipment_rent_backend/actions/workflows/django.yml/badge.svg)](https://github.com/Chudilo4/equipment_rent_backend/actions/workflows/django.yml)
# Создаём виртуальное окружение
## venv
```bash
python -m venv venv
```
# Устанавливаем зависимости
```bash
make installrequirements
# устанавливаем пакеты
```
# Собираем статические файлы
```bash
python manage.py collectstatic
# Собираем статические файлы в папку static
```
# Установка supervisor
```bash
sudo apt-get install supervisor
# Нужен для автоматического запуска gunicorn
```
# Создаём конфигурационный файл для supervisor
```bash
sudo nano /etc/supervisor/conf.d/equipment_rent_backend.conf
# Создаём конфигурационный файл для supervisor
```
# Создаём директорию для логов
```bash
sudo mkdir /home/твой путь до логов/logs/equipment_rent_backend.log
# Создаём конфигурационный файл для supervisor
```
# Создаём конфиг для переменных gunicorn
```bash
sudo nano /home/твой путь до проекта/equipment_rent_backend/venv/gunicorn.conf.py
# Создаём конфигурационный файл для gunicorn
```
# Перезапускаем supervisor
```bash
sudo service supervisor restart
# Создаём конфигурационный файл для gunicorn
```
# Устанавливаем Nginx
```bash
sudo apt-get install nginx
# Устанавливаем Nginx
```
# Прописываем новое имя для нашего сайта в Host
```bash
sudo sudo nano /etc/hosts
# Прописываем новое имя для нашего сайта в Host пример #127.0.0.1    equipment_rent_backend.loc
```
# Прописываем новый конфиг для Nginx
```bash
sudo sudo nano /etc/nginx/sites-available/equipment_rent_backend
# Прописываем новый конфиг для Nginx из equipment_rent_backend
```
# Проверяем синтаксис
```bash
sudo nginx -t
# Проверяем что всё написано без ошибок
```
# Копируем конфиг в продакшен
```bash
sudo ln -s /etc/nginx/sites-available/equipment_rent_backend /etc/nginx/sites-enabled/
# Прописываем новый конфиг для Nginx из equipment_rent_backend
```
# Перезагружаем Nginx и supervisor
```bash
sudo service nginx restart
sudo service supervisor restart
# Прописываем новый конфиг для Nginx из equipment_rent_backend
```