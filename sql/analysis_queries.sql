--Top categories by revenue

SELECT category, SUM(purchaseamount) AS Revenue
FROM CustomerShopping
GROUP BY category
ORDER BY Revenue DESC

--Average spend by gender

SELECT gender, AVG(purchaseamount)
FROM CustomerShopping
GROUP BY gender

--Most popular payment method

SELECT paymentmethod, COUNT(*) AS count_customer
FROM CustomerShopping
GROUP BY paymentmethod
ORDER BY count_customer DESC

--Seasonal Sales Trend

SELECT season, SUM(purchaseamount) AS sales
FROM CustomerShopping
GROUP BY season
ORDER BY sales

--Subscription vs Non-subscription spending

SELECT subscriptionstatus, AVG(purchaseamount) AS sales
FROM CustomerShopping
GROUP BY subscriptionstatus

--Top locations by sales

SELECT location, SUM(purchaseamount) AS sales
FROM CustomerShopping
GROUP BY location
ORDER BY sales DESC

--Repeat customers
SELECT LoyaltySeg, COUNT(*)
FROM(
SELECT *,
CASE
WHEN previouspurchases >=20 THEN 'Loyal Customers'
ELSE 'Regular'
END AS LoyaltySeg
FROM CustomerShopping
)
GROUP BY LoyaltySeg

SELECT *
FROM CustomerShopping