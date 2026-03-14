-- =====================================================
-- Création de la table analytique category_metrics
-- Agrégation des indicateurs par catégorie
-- Source : products
-- Objectif : préparer les données pour le dashboard
-- =====================================================

CREATE OR REPLACE TABLE `burnished-ether-490123-c8.ecommerce_analytics.category_metrics`
AS
SELECT
  category,
  COUNT(*) AS product_count,
  AVG(price) AS avg_price,
  AVG(rating) AS avg_rating,
  SUM(stock) AS total_stock
FROM `burnished-ether-490123-c8.ecommerce_analytics.products`
GROUP BY category;