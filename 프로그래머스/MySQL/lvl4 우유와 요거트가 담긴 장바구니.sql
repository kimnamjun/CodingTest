SELECT a.cart_id
FROM cart_products a INNER JOIN cart_products b ON a.cart_id = b.cart_id
WHERE a.name = '우유' AND b.name = '요거트'
ORDER BY a.cart_id;