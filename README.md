# Тестовое задание: Парсер Kaspi магазина  

## 📌 Описание проекта  
Кратко опишите, что делает программа:  
- что именно парсит (какие данные),  
- куда сохраняет (PostgreSQL, JSON),  
- какие дополнительные возможности реализованы (если есть).  

## 🚀 Установка и запуск  

### 1. Клонирование репозитория  
git clone https://github.com/<username>/<repo>.git  
cd <repo>  

### 2. Установка зависимостей  
pip install -r requirements.txt  

### 3. Настройка окружения  
Создайте файл `.env` и укажите:  
DB_HOST=localhost  
DB_PORT=5432  
DB_NAME=kaspi  
DB_USER=postgres  
DB_PASSWORD=postgres  

### 4. Запуск парсера  
python main.py  

## 📂 Структура проекта  
/project  
│── main.py  
│── seed.json  
│── export/  
│    ├── product.json  
│    ├── offers.jsonl  
│── db/  
│    ├── models.py  
│    ├── migrations/ (опционально)  
│── logs/  
│    ├── log.json  
│── README.md  

## 🗄️ PostgreSQL  
Пример таблиц:  

**products**  
- id  
- name  
- category  
- min_price  
- max_price  
- rating  
- reviews_count  

**offers** (опционально)  
- id  
- product_id  
- seller  
- price  

## 🔄 Обновления данных  
Если реализовано автообновление:  
- Интервал: 15 минут  
- Какие поля обновляются  

## 📝 Пример логов  
{"time": "2025-10-05T12:00:01", "status": "success", "action": "fetch_product", "url": "..."}  

## ✅ Что сделано  
- [x] Парсинг товара  
- [x] Сохранение в PostgreSQL  
- [x] Экспорт в JSON  
- [ ] Логирование  
- [ ] Docker  
- [ ] Alembic миграции  

## 📄 Дополнительно  
- На что ушло больше всего времени  
- Что можно улучшить  
