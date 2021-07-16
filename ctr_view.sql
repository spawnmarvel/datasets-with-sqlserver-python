--Inner join
SELECT
                        a.a_id
	                    ,a.a_name
                        ,b.b_id
                        ,b.b_name
                        ,b.b_rating
                        ,b.b_reviews
                        ,b.b_price
                        ,b.b_year
                        ,b.b_genre
                        ,b.author_b_id
                        FROM DataSetsDb.test.Authors as a
                        INNER JOIN DataSetsDb.test.BestSellers as b
                        ON a.a_id = b.author_b_id;

-- Create view
CREATE VIEW test.BestsellersAndAuthors as
                        SELECT
                        a.a_id
	                    ,a.a_name
                        ,b.b_id
                        ,b.b_name
                        ,b.b_rating
                        ,b.b_reviews
                        ,b.b_price
                        ,b.b_year
                        ,b.b_genre
                        ,b.author_b_id
                        FROM DataSetsDb.test.Authors as a
                        INNER JOIN DataSetsDb.test.BestSellers as b
                        ON a.a_id = b.author_b_id;

-- Check view
SELECT * FROM sys.views WHERE OBJECT_ID=OBJECT_ID('test.BestsellersAndAuthors');