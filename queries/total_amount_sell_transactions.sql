SELECT  
    SUM(amount_inc_tax) AS total_amount_sell_transactions
FROM 
    transactions
WHERE 
    category = 'SELL';