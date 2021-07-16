-- Insert from table.t1 to table.t2
INSERT prod.BestSellers
                (b_name
                    ,b_rating
                    ,b_reviews
                    ,b_price
                    ,b_year
                    ,b_genre
                    ,author_b_id)
                    SELECT
                         b_name
                        ,b_rating
                        ,b_reviews
                        ,b_price
                        ,b_year
                        ,b_genre
                        ,author_b_id
                        FROM test.BestSellers
                        WHERE NOT EXISTS (SELECT b_id FROM prod.BestSellers po WHERE po.b_id = test.BestSellers.b_id);


-- Merge from table.t1 to table.t2
MERGE prod.BestSellers AS target
                 USING test.BestSellers AS source
                 ON source.b_id = target.b_id
                 
                 WHEN NOT MATCHED BY target THEN
                    INSERT (b_name
                        ,b_rating
                        ,b_reviews
                        ,b_price
                        ,b_year
                        ,b_genre)
                        VALUES(source.b_name
                        ,source.b_rating
                        ,source.b_reviews
                        ,source.b_price
                        ,source.b_year
                        ,source.b_genre)

                WHEN MATCHED THEN UPDATE SET
                        target.b_name=source.b_name
                        ,target.b_rating=source.b_rating
                        ,target.b_reviews=source.b_reviews
                        ,target.b_price=source.b_price
                        ,target.b_year=source.b_year
                        ,target.b_genre=source.b_genre
                
                WHEN NOT MATCHED BY source THEN
                    DELETE;