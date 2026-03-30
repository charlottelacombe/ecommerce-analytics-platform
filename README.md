# Ecommerce Analytics Platform

## Project Overview
This project is an end-to-end ecommerce analytics pipeline designed to transform raw product API data into actionable business insights.

It focuses on product-level analytics, including inventory value, pricing, discount strategy, and category performance.

The project was built iteratively through sprints, from API ingestion to dashboarding and automation.

---

## Business Objective
The goal of this project is to simulate how an ecommerce company can turn raw product data into structured insights for business decision-making.

This project helps answer questions such as:
- Which categories contain the most products?
- Which categories generate the highest inventory value?
- Which products represent the highest stock value?
- How do pricing, discounts, and ratings vary across categories?

---

## Project Scope
This first version of the project is intentionally focused on a single product dataset.

The objective was to build a clean and complete end-to-end pipeline first:
- data ingestion
- data cleaning
- cloud storage
- SQL modeling
- dashboarding
- workflow automation

Rather than expanding too early into multiple entities, I chose to validate the full analytics workflow on one coherent source.

---

## Tech Stack
- Python (`requests`, `pandas`)
- SQL
- Google Cloud Platform (BigQuery)
- Power BI
- Apache Airflow (in progress)
- Docker (in progress)
- Git / GitHub

---

## Data Pipeline Architecture

### Data Flow
API → Python → BigQuery → SQL → Power BI
-- The CSV import into BigQuery and the Power BI refresh are currently done manually.

### Orchestration & Environment
- Airflow wil orchestrate the pipeline steps
- Docker will containerize the project environment

---

## Sprint-Based Project Management
I structured the project myself into epics, sprints, backlogs, and deliverables to simulate a real project workflow.

### Sprint 1 — Foundations & API Ingestion
- project setup
- Git/GitHub setup
- API exploration
- raw JSON ingestion

### Sprint 2 — Data Processing & Cleaning
- JSON exploration
- pandas transformation
- clean CSV generation

### Sprint 3 — BigQuery & Cloud Setup
- GCP project creation
- BigQuery dataset creation
- cloud data loading
- first SQL analysis

### Sprint 4 — Data Modeling & KPIs
- analytical category table
- KPI generation in SQL
- modeling for BI usage

### Sprint 5 — BI Dashboard
- interactive Power BI dashboard
- Overview page
- Business Analysis page
- KPI cards and category-based insights

### Sprint 6 — Automation & Docker  (in progress)
- Airflow DAG orchestration
- Dockerized environment
- architecture documentation

---

## Dashboard Overview

### Page 1 — E-commerce Overview
This page provides a high-level snapshot of the catalog through:
- Total Inventory Value
- Average Product Rating
- Total Number of Products
- Total Inventory Units
- Average Product Price
- Product Count by Category
- Inventory Value by Category
- Top Products by Inventory Value

**Purpose:** provide a quick overview of catalog size, value, and distribution.

### Page 2 — Business Analysis & Category Performance
This page focuses on category-level business analysis through:
- Average Discount by Category
- Average Product Price by Category
- Customer Satisfaction by Category
- Category Performance Summary

**Purpose:** compare category performance across pricing, promotions, and satisfaction.

---

## Key Insights
- A small number of categories contribute disproportionately to total inventory value
- Inventory value and product count do not always follow the same pattern
- Discount strategy varies across categories
- Customer satisfaction differs by category and can support prioritization decisions

---

## Why This Project Matters
This project demonstrates my ability to:
- ingest data from an external API
- transform raw data into analysis-ready datasets
- work with BigQuery and SQL analytical modeling
- build interactive BI dashboards
- structure a project with sprint planning
- move toward automation and reproducibility with Airflow and Docker

---

## Dataset Boundaries
This project focuses on product and category analytics rather than customer behavior analytics.

The source dataset does not include:
- customer profiles
- transaction history
- purchase timestamps
- demographic segmentation

Because of that, the analysis is intentionally centered on:
- catalog structure
- inventory value
- pricing
- discounting
- customer ratings

---

## Future Improvements
- Connect Power BI directly to BigQuery
- Automate the pipeline with Airflow (Sprint 6 — in progress)
- Extend the data model with additional entities
- Add richer monitoring around orchestration
- Expand the project toward customer-level analytics with transaction data

---

##  Dashboard Preview

<img width="1277" height="790" alt="Capture d’écran 2026-03-27 à 01 49 18" src="https://github.com/user-attachments/assets/ae897471-6f6b-4784-9699-99523b251d34" />


<img width="1277" height="790" alt="Capture d’écran 2026-03-27 à 01 49 30" src="https://github.com/user-attachments/assets/6813c35e-075d-4948-8a68-5c9f7f8df4ff" />


## Repository Structure

<img width="265" height="526" alt="Capture d’écran 2026-03-30 à 16 56 37" src="https://github.com/user-attachments/assets/64ac2b85-22b5-4d43-a691-7539a62045ab" />

