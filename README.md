# Ecommerce Analytics Platform

##  Project Overview

This project builds an end-to-end ecommerce data pipeline and dashboard to analyze product performance, inventory value, and customer behavior.

The goal is to transform raw API data into actionable business insights.

---

##  Business Objective

E-commerce companies need to:

* monitor product performance
* track inventory value
* optimize pricing and discount strategies
* understand customer satisfaction (ratings)

This project provides a solution to support data-driven decisions.

---

##  Tech Stack

* Python (requests, pandas)
* Google Cloud Platform (GCS, BigQuery)
* SQL (data transformation)
* Power BI (dashboard & visualization)
* Airflow (pipeline orchestration - optional)
* Docker (environment setup)

---

## Data Pipeline Architecture

API → Python → GCS → BigQuery → SQL → Power BI → Airflow → Docker

---

## Dashboard Overview

### Page 1 — Overview

* Global KPIs (Inventory Value, Avg Rating, Total Products, Total Stock, Avg Price)
* Product distribution by category
* Inventory value by category
* Top products by inventory value

-- Purpose: provide a quick snapshot of business performance

---

### Page 2 — Category Performance Analysis

* Average discount by category
* Customer satisfaction (ratings) by category
* Inventory distribution insights
* Category performance table (KPIs combined)

-- Purpose: deeper analysis to support business decisions

---

##  Key Insights

* A small number of products generate most of the inventory value
* Some categories have high stock but lower customer satisfaction
* Discount strategies vary significantly across categories

---

##  Future Improvements

* Connect Power BI directly to BigQuery
* Automate pipeline with Airflow
* Add real-time data ingestion
* Improve data modeling (star schema)

---

##  Dashboard Preview

<img width="1277" height="790" alt="Capture d’écran 2026-03-27 à 01 49 18" src="https://github.com/user-attachments/assets/ae897471-6f6b-4784-9699-99523b251d34" />


<img width="1277" height="790" alt="Capture d’écran 2026-03-27 à 01 49 30" src="https://github.com/user-attachments/assets/6813c35e-075d-4948-8a68-5c9f7f8df4ff" />

