-- stg_status.sql

SELECT 
    CAST("index" AS INT) AS "index",
    CAST("status_id" AS INT) AS "status_id",
    CAST("status" AS TEXT) AS "status"
FROM 
    {{ source('raw', 'status') }}