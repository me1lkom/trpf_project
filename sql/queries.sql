-- 1. Получение списка всех products
SELECT
    product_id,
    name,
    description,
    country
FROM products
ORDER BY product_id;

-- 2. Получение списка всех suppliers
SELECT
    supplier_id,
    name,
    inn,
    phone,
    email
FROM suppliers
ORDER BY name;

-- 3. Получение конкретный product по id с заказчиком
SELECT
    products.product_id,
    products.name,
    products.description,
    products.country,
    COALESCE(users.name, suppliers.name) as buyers_name,
    CASE
        WHEN product_buyers.user_id IS NOT NULL
            THEN 'Физ лицо'
        WHEN product_buyers.supplier_id IS NOT NULL
            THEN 'Организация'
    END AS buyers_type
FROM products
LEFT JOIN product_buyers ON product_buyers.product_id = products.product_id
LEFT JOIN users ON product_buyers.user_id = users.user_id
LEFT JOIN suppliers ON product_buyers.supplier_id = suppliers.supplier_id
WHERE products.product_id = 1;

-- 4. Получение конкретный supplier по id
SELECT
    supplier_id,
    name,
    inn,
    phone,
    email
FROM suppliers
WHERE supplier_id = 1;

-- 5. Получение всех offers к product
SELECT
    offers.offer_id,
    offers.price,
    offers.min_lots,
    offers.delivery_time_days,
    products.name as product_name,
    suppliers.name as supplier_name,
    suppliers.phone as supplier_phone
FROM offers
JOIN products ON products.product_id = offers.product_id
JOIN suppliers ON suppliers.supplier_id = offers.supplier_id
WHERE offers.product_id = 1;

-- 6. Получение всех offers к product, с сортировкой по цене
SELECT
    offers.offer_id,
    offers.price,
    offers.min_lots,
    offers.delivery_time_days,
    products.name as product_name,
    suppliers.name as supplier_name,
    suppliers.phone as supplier_phone
FROM offers
JOIN products ON products.product_id = offers.product_id
JOIN suppliers ON suppliers.supplier_id = offers.supplier_id
WHERE offers.product_id = 1
ORDER BY offers.price;

-- 7. Получение всех offers к product, с сортировкой по сроку доставки
SELECT
    offers.offer_id,
    offers.price,
    offers.min_lots,
    offers.delivery_time_days,
    products.name as product_name,
    suppliers.name as supplier_name,
    suppliers.phone as supplier_phone
FROM offers
JOIN products ON products.product_id = offers.product_id
JOIN suppliers ON suppliers.supplier_id = offers.supplier_id
WHERE offers.product_id = 1
ORDER BY offers.delivery_time_days;

-- 8. Получение количества всех offers
SELECT
    COUNT(*) as count_offers
FROM offers;

-- 9. Получение минимальной, максимальной и средней цены offers к product
SELECT
    MIN(price) as min_price,
    MAX(price) as max_price,
    ROUND(AVG(price), 2) as avg_price
FROM offers
WHERE offers.product_id = 1;

-- 10. Получение количества offers к каждому product
SELECT
    products.product_id,
    products.name,
    COUNT(offers.offer_id) as count_offers
FROM products
LEFT JOIN offers ON products.product_id = offers.product_id
GROUP BY products.product_id, products.name
ORDER BY products.product_id;

-- 11. Получение количества offers к каждому supplier
SELECT
    suppliers.supplier_id,
    suppliers.name,
    COUNT(offers.offer_id) as count_offers
FROM suppliers
LEFT JOIN offers ON suppliers.supplier_id = offers.supplier_id
GROUP BY suppliers.supplier_id, suppliers.name
ORDER BY suppliers.supplier_id;

-- 12. Получение products, у которых больше одного offer
SELECT
    products.product_id,
    products.name,
    COUNT(offers.offer_id) AS count_offers
FROM products
JOIN offers ON offers.product_id = products.product_id
GROUP BY products.product_id, products.name
HAVING COUNT(offers.offer_id) > 1;

-- 13. Получение всех offers к supplier
SELECT
    offers.offer_id,
    offers.price,
    offers.min_lots,
    offers.delivery_time_days,
    products.name as product_name,
    products.description as product_description,
    products.country as product_country,
    COALESCE(users.name, suppliers.name) as buyers_name,
    CASE
        WHEN product_buyers.user_id IS NOT NULL
            THEN 'Физ лицо'
        WHEN product_buyers.supplier_id IS NOT NULL
            THEN 'Организация'
    END AS buyers_type
FROM offers
JOIN products ON products.product_id = offers.product_id
LEFT JOIN product_buyers ON product_buyers.product_id = products.product_id
LEFT JOIN users ON product_buyers.user_id = users.user_id
LEFT JOIN suppliers ON product_buyers.supplier_id = suppliers.supplier_id
WHERE offers.supplier_id = 1;

-- 14. Получение всех offers
SELECT
    offers.offer_id,
    offers.price,
    offers.min_lots,
    offers.delivery_time_days,
    products.name as product_name,
    suppliers.name as supplier_name
FROM offers
JOIN products ON products.product_id = offers.product_id
JOIN suppliers ON suppliers.supplier_id = offers.supplier_id
ORDER BY offers.offer_id;

-- 15. Получение конкректного offers по offer_id
SELECT
    offers.offer_id,
    offers.price,
    offers.min_lots,
    offers.delivery_time_days,
    products.name as product_name,
    products.description as product_description,
    products.country as product_country,
    suppliers.name as supplier_name,
    suppliers.inn as supplier_inn,
    suppliers.phone as supplier_phone,
    suppliers.email as supplier_email,
    COALESCE(buyers_users.name, buyers_suppliers.name) as buyers_name,
    CASE
        WHEN product_buyers.user_id IS NOT NULL
            THEN 'Физ лицо'
        WHEN product_buyers.supplier_id IS NOT NULL
            THEN 'Организация'
    END AS buyers_type
FROM offers
JOIN products ON products.product_id = offers.product_id
JOIN suppliers ON suppliers.supplier_id = offers.supplier_id
LEFT JOIN product_buyers ON product_buyers.product_id = products.product_id
LEFT JOIN users AS buyers_users ON product_buyers.user_id = buyers_users.user_id
LEFT JOIN suppliers AS buyers_suppliers ON product_buyers.supplier_id = buyers_suppliers.supplier_id
WHERE offers.offer_id = 1;

-- 16. Получение количества всех suppliers
SELECT
    COUNT(*) as count_suppliers
FROM suppliers;

-- 17. Получение количества всех users
SELECT
    COUNT(*) as count_users
FROM users;

-- 18. Получение количества всех products
SELECT
    COUNT(*) as count_products
FROM products;