SELECT
    transaction_date,
    SUM(
        CASE 
            WHEN category = 'SELL' THEN quantity 
            WHEN category = 'BUY' THEN -quantity 
            ELSE 0
        END
    )AS balance
FROM
    transactions
WHERE
    name = 'Amazon Echo Dot'
GROUP BY
    transaction_date;