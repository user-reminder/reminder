# Сервис напоминаний

Запустить базу данных mysql
```bash
docker-compose up -d db
```
После создания базы данных запустить миграции
```bash
docker-compose up migrations
```
Затем запустить приложение
```bash
docker-compose up -d app
```
- Приложение будет доступно по адресу: <http://localhost:8000> 

- Время наступления указывать UTC+0

