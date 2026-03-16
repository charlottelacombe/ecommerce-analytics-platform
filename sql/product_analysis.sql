/* ============================================================
   ECOMMERCE ANALYTICS PLATFORM
   SQL ANALYSIS - PRODUCTS DATA
   Dataset: ecommerce_analytics.products
   Project: burnished-ether-490123-c8

   This file contains exploratory and analytical SQL queries
   used to analyze the product dataset loaded into BigQuery.
   ============================================================ */


/* ------------------------------------------------------------
1. Total number of products
Purpose:
Measure the total volume of products available in the dataset.
------------------------------------------------------------- */

SELECT COUNT(*) AS total_products
FROM `burnished-ether-490123-c8.ecommerce_analytics.products`;



/* ------------------------------------------------------------
2. Number of products by category
Purpose:
Understand how products are distributed across categories.
------------------------------------------------------------- */

SELECT category, COUNT(*) AS product_count
FROM `burnished-ether-490123-c8.ecommerce_analytics.products`
GROUP BY category
ORDER BY product_count DESC;



/* ------------------------------------------------------------
3. Average price by category
Purpose:
Compare the pricing level of different product categories.
------------------------------------------------------------- */

SELECT category, ROUND(AVG(price), 2) AS avg_price
FROM `burnished-ether-490123-c8.ecommerce_analytics.products`
GROUP BY category
ORDER BY avg_price DESC;



/* ------------------------------------------------------------
4. Average rating by category
Purpose:
Measure customer satisfaction across product categories.
------------------------------------------------------------- */

SELECT
    category,
    ROUND(AVG(rating), 2) AS avg_rating
FROM `burnished-ether-490123-c8.ecommerce_analytics.products`
GROUP BY category
ORDER BY avg_rating DESC;



/* ------------------------------------------------------------
5. Total stock by category
Purpose:
Evaluate product availability by category.
------------------------------------------------------------- */

SELECT category, SUM(stock) AS total_stock
FROM `burnished-ether-490123-c8.ecommerce_analytics.products`
GROUP BY category
ORDER BY total_stock DESC;



/* ------------------------------------------------------------
6. Inventory value by category
Purpose:
Estimate the potential value of inventory if all stock were sold
at the listed product price.
------------------------------------------------------------- */

SELECT category, SUM(price * stock) AS inventory_value
FROM `burnished-ether-490123-c8.ecommerce_analytics.products`
GROUP BY category
ORDER BY inventory_value DESC;



/* ------------------------------------------------------------
7. Top 10 most expensive products
Purpose:
Identify premium products in the catalog.
------------------------------------------------------------- */

SELECT title, brand, category, price
FROM `burnished-ether-490123-c8.ecommerce_analytics.products`
ORDER BY price DESC
LIMIT 10;



/* ------------------------------------------------------------
8. Top 10 highest rated products
Purpose:
Highlight the best-rated products based on customer ratings.
------------------------------------------------------------- */

SELECT title, brand,category,rating
FROM `burnished-ether-490123-c8.ecommerce_analytics.products`
ORDER BY rating DESC
LIMIT 10;

/* ------------------------------------------------------------
Table: category_metrics

Objectif :
Créer une table analytique qui résume les données produits
par catégorie.

Métriques calculées :

product_count = nombre de produits dans la catégorie

avg_price =  prix moyen des produits

avg_rating = note moyenne des produits

total_stock = quantité totale de produits en stock

inventory_value = valeur totale du stock (price * stock)
------------------------------------------------------------ */

CREATE OR REPLACE TABLE `burnished-ether-490123-c8.ecommerce_analytics.category_metrics` AS
SELECT
  category,
  COUNT(*) AS product_count,
  ROUND(AVG(price),2) AS avg_price,
  ROUND(AVG(rating),2) AS avg_rating,
  SUM(stock) AS total_stock,
  ROUND(SUM(price * stock),2) AS inventory_value
FROM `burnished-ether-490123-c8.ecommerce_analytics.products`
GROUP BY category;