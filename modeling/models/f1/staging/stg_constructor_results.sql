-- stg_constructor_results.sql

SELECT 
    CAST("index" AS INT) AS "index",
    CAST("constructor_results_id" AS INT) AS "constructor_results_id",
    CAST("race_id" AS INT) AS "race_id",
    CAST("constructor_id" AS INT) AS "constructor_id",
    CAST("points" AS FLOAT) AS "points",
    CAST("status" AS TEXT) AS "status"
FROM 
    {{ source('raw', 'constructor_results') }}

