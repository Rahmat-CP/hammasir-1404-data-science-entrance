SELECT
    COALESCE(SUM(s.units * p.price) / SUM(s.units), 0) AS avg_sell_price,
    p.product_id
FROM
    product_prices AS p
LEFT JOIN
    product_sales AS s
    ON p.product_id = s.product_id
    AND s.sold_date BETWEEN p.start_date AND p.end_date
GROUP BY
    p.product_id
ORDER BY
    p.product_id;

