-- Stored procedure with multiple paramters
CREATE PROCEDURE customer.GetOrderInformationByYearAndCustomerID (@check_year AS INT, @check_customer_id AS INT)
AS
--Get all order information on customers by year
SELECT sod.[SalesOrderID]
      ,sod.[OrderQty]
      ,sod.[ProductID]
      ,sod.[SpecialOfferID]
      ,sod.[UnitPrice]
      ,sod.[UnitPriceDiscount]
      ,sod.[LineTotal]
	  ,soh.CustomerID
	  ,soh.OrderDate
FROM [AdventureWorks].[Sales].[SalesOrderDetail] AS sod
INNER JOIN sales.SalesOrderHeader AS soh ON soh.SalesOrderID=sod.SalesOrderID
WHERE YEAR(soh.OrderDate)= @check_year
AND soh.CustomerID=@check_customer_id
ORDER BY sod.LineTotal desc


USE test;
GO

-- if set to 0, then error
DECLARE @my_num varchar(20) = '0';
BEGIN TRY
	PRINT 10 / @my_num;
END TRY
BEGIN CATCH
	PRINT 'Er msg ' + CAST(ERROR_NUMBER() AS varchar(12)) + ';' + ERROR_MESSAGE();
END CATCH


IF EXISTS (SELECT * FROM tblGLUserAccess WHERE GLUserName ='xxxxxxxx') 
BEGIN
   SELECT 1 
END
ELSE
BEGIN
    SELECT 2
END