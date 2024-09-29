SELECT
    transaction_date,
    SUM(
        SUM(
            CASE 
                WHEN category = 'SELL' THEN quantity 
                WHEN category = 'BUY' THEN -quantity 
                ELSE 0
            END
        )
    ) OVER (ORDER BY transaction_date ASC) AS balance
FROM
    transactions
WHERE
    name = 'Amazon Echo Dot'
GROUP BY
    transaction_date;