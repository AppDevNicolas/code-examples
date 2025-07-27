
--  Load Slowly Changing Dimension Type 2 using Oracle Merge Statement
-- https://databobjr.blogspot.com/2011/04/load-slowly-changing-dimension-type-2.html

--Product dimension table

CREATE TABLE DIM_PRODUCT
(
PRODUCT_SID NUMBER NOT NULL,
PRODUCT_ID NUMBER NOT NULL,
PRODUCT_CATEGORY_ID NUMBER,
PRODUCT_NAME VARCHAR2(50 CHAR),
PRODUCT_DESCRIPTION VARCHAR2(200 CHAR),
PRICE NUMBER(8,2),
PRICE_EFFECTIVE_DATE DATE,
LAST_MODIFIED_DATE DATE,
EFFECTIVE_START_DATE DATE,
EFFECTIVE_END_DATE DATE,
IS_CURRENT_ROW VARCHAR2(1 CHAR)
CREATED_DATE DATE,
UPDATED_DATE DATE
);

-- Source stage table: stg_product.
-- This is a stage table use to store the newly modified product records from the product table.

CREATE TABLE STG_PRODUCT
(
PRODUCT_ID NUMBER NOT NULL,
PRODUCT_CATEGORY_ID NUMBER,
PRODUCT_NAME VARCHAR2(50 CHAR),
PRODUCT_DESCRIPTION VARCHAR2(200 CHAR),
PRICE NUMBER(8,2),
PRICE_EFFECTIVE_DATE DATE,
LAST_MODIFIED_DATE DATE,
CREATED_DATE DATE
);

-- Sequence to use for the dim_product dimension table ‘s surrogate keys.

CREATE SEQUENCE s_dim_product
START WITH 1
MAXVALUE 9999999999999999999999999999
MINVALUE 1
NOCYCLE
CACHE 20
NOORDER;

-- Utility table: scd_row_type.

CREATE TABLE SCD_ROW_TYPE
(
SCD_ROW_TYPE_ID NUMBER NOT NULL,
SCD_ROW_TYPE_DESCRIPTION VARCHAR2(20 CHAR)
);

-- Data:

TRUNCATE TABLE stg_product;

INSERT INTO stg_product ( PRODUCT_ID, PRODUCT_CATEGORY_ID,  PRODUCT_NAME,PRODUCT_DESCRIPTION,PRICE,PRICE_EFFECTIVE_DATE,  LAST_MODIFIED_DATE,  CREATED_DATE)
        values (1,8,'Apple iPad 36 GB','Apple iPad 36 GB with case', 800,sysdate,sysdate,sysdate);

INSERT INTO stg_product ( PRODUCT_ID, PRODUCT_CATEGORY_ID,  PRODUCT_NAME,PRODUCT_DESCRIPTION,PRICE,PRICE_EFFECTIVE_DATE,  LAST_MODIFIED_DATE,CREATED_DATE)
         values (2,7,'Canon 12 MPIX Digital Camera','Canon 12 MPIX Digital Camera, Zoon Len, Case', 150,sysdate,sysdate,sysdate);

COMMIT;



-- Query:

MERGE INTO dim_product p
USING ( SELECT DECODE(s.scd_row_type_id,1,-6789,m.product_sid) as product_sid,
                   PRODUCT_ID,
                   PRODUCT_CATEGORY_ID,
                   PRODUCT_NAME,
                   PRODUCT_DESCRIPTION,
                   PRICE,
                   PRICE_EFFECTIVE_DATE,
                   LAST_MODIFIED_DATE,
                   CREATED_DATE,
                   m.scd_row_type_id
              FROM    (SELECT dp.product_sid,
                              sp.PRODUCT_ID,
                              sp.PRODUCT_CATEGORY_ID,
                              sp.PRODUCT_NAME,
                              sp.PRODUCT_DESCRIPTION,
                              sp.PRICE,
                              sp.PRICE_EFFECTIVE_DATE,
                              sp.LAST_MODIFIED_DATE,
                              sp.CREATED_DATE,
                              CASE
                                 WHEN dp.product_id IS NULL
                                 THEN
                                    1
                                 WHEN (dp.product_category_id !=
                                          sp.product_category_id
                                       OR dp.product_name != sp.product_name
                                       OR DP.PRODUCT_DESCRIPTION !=
                                             sp.product_description
                                       OR dp.price != sp.price
                                       OR dp.price_effective_date !=
                                             sp.price_effective_date)
                                 THEN
                                    2
                                 ELSE
                                    0
                              END
                                 AS scd_row_type_id
                         FROM    stg_product sp
                              LEFT JOIN
                                 Dim_product dp
                              ON (sp.product_id = dp.product_id and  dp.is_current_row = 'Y')
                     ) m
                   JOIN  scd_row_type s
                   ON (s.scd_row_type_id <= m.scd_row_type_id)
                   ) mp
        ON  (p.product_sid = mp.product_sid)
when matched then
   update set P.EFFECTIVE_END_DATE = mp.LAST_MODIFIED_DATE, is_current_row = 'N', updated_date = sysdate
when NOT matched then
insert (P.PRODUCT_SID,P.PRODUCT_ID,P.PRODUCT_CATEGORY_ID, P.PRODUCT_NAME, P.PRODUCT_DESCRIPTION, P.PRICE, p.PRICE_EFFECTIVE_DATE,P.LAST_MODIFIED_DATE,
 p.effective_start_date,P.EFFECTIVE_END_DATE,is_current_row, created_date,
 updated_date )
 values (s_dim_product.nextval,mp.PRODUCT_ID,mp.PRODUCT_CATEGORY_ID,mp.PRODUCT_NAME,
 mp.PRODUCT_DESCRIPTION, mp.PRICE,mp.price_effective_date,
mp.LAST_MODIFIED_DATE,mp.last_modified_date,
 to_date('2099-12-31 00:00:00','YYYY-MM-DD HH24:MI:SS'),'Y', sysdate,sysdate);
  commit;