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