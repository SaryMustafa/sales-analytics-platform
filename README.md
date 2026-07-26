# 📊 Sales Analytics Platform

![Python](https://img.shields.io/badge/Python-3.11-blue)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)
![SQL](https://img.shields.io/badge/SQL-Analytics-orange)
Аналитическая платформа для анализа продаж интернет-магазина.

Проект реализует полный цикл работы Data Analyst:

- загрузка и подготовка данных
- хранение данных в PostgreSQL
- SQL-аналитика бизнес-метрик
- анализ клиентов и товаров
- сегментация пользователей
- когортный анализ
- визуализация результатов в Streamlit Dashboard


## 🚀 Возможности


## 📈 Sales Analytics

Расчёт основных бизнес-метрик:

- Total Revenue
- Number of Orders
- Average Check
- Monthly Sales Dynamics


## 👥 Customer Analytics

Анализ клиентской активности:

- количество клиентов
- топ клиентов по выручке
- покупательская активность
- RFM-сегментация


## 📦 Product Analytics

Анализ товаров:

- топ товаров по выручке
- количество продаж
- категории товаров


## 📊 Retention Analysis

Когортный анализ клиентов:

- определение первой покупки
- анализ удержания пользователей
- retention heatmap


## 🖥 Dashboard

Интерактивный дашборд создан с использованием Streamlit.

Возможности:

- KPI показатели
- графики продаж
- анализ клиентов
- анализ товаров
- RFM сегментация
- Cohort retention


## 🏗 Структура проекта

sales-analytics-platform/
├── dashboard/
│ └── app.py
├── database/
│ ├── schema.sql
│ └── load_data.py
├── data/
│ ├── generate_data.py
│ ├── customers.csv
│ ├── products.csv
│ ├── orders.csv
│ └── order_items.csv
├── sql/
│ ├── revenue.sql
│ ├── monthly_sales.sql
│ ├── customers.sql
│ ├── rfm.sql
│ └── cohorts.sql
├── images/
├── requirements.txt
└── README.md



## ⚙️ Установка


Клонирование проекта:

```bash
git clone <repository-url>

Создание виртуального окружения:
python3 -m venv .venv

Активация:
source .venv/bin/activate

Установка зависимостей:
pip install -r requirements.txt

🗄 База данных
Используется PostgreSQL.
Создание базы:

CREATE DATABASE sales_analytics;
Создание таблиц:

psql sales_analytics < database/schema.sql
Загрузка данных:

python database/load_data.py

▶️ Запуск Dashboard
streamlit run dashboard/app.py
```

После запуска:
http://localhost:8501

🛠 Использованные технологии
Python
Pandas
NumPy
Streamlit
Plotly
Database
PostgreSQL
SQL
Analytics
Revenue analysis
Customer segmentation
RFM analysis
Cohort analysis

🎯 Цель проекта
Создание аналитической платформы, которая помогает бизнесу:
анализировать продажи
находить наиболее ценных клиентов
оценивать удержание пользователей
принимать решения на основе данных


## 📸 Dashboard Preview

### Main Dashboard

![Dashboard](https://raw.githubusercontent.com/SaryMustafa/sales-analytics-platform/main/images/dashboard.png)


### Products Analytics

![Products](https://raw.githubusercontent.com/SaryMustafa/sales-analytics-platform/main/images/products.png)


### Customer Analytics

![Analytics](https://raw.githubusercontent.com/SaryMustafa/sales-analytics-platform/main/images/analytics.png)



