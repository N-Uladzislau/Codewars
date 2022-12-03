SELECT ProductName, sum(Price * Quantity) Total FROM Products join OrderDetails on Products.ProductID=OrderDetails.ProductID group by ProductName order by Total desc limit 1;


IF(Quantity > 30, 'The quantity is greater than 30', IF(Quantity = 30, 'The quantity is 30', 'The quantity is under 30')) as QuantityTextIF,
  CASE
    WHEN Quantity > 30 THEN 'The quantity is greater than 30'
    WHEN Quantity = 30 THEN 'The quantity is 30'
    ELSE 'The quantity is under 30'
  END AS QuantityText

