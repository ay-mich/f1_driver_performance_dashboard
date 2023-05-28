-- stg_qualifying.sql

SELECT 
    CAST("index" AS INT) AS "index",
    CAST("qualify_id" AS INT) AS "qualify_id",
    CAST("race_id" AS INT) AS "race_id",
    CAST("driver_id" AS INT) AS "driver_id",
    CAST("constructor_id" AS INT) AS "constructor_id",
    CAST("number" AS INT) AS "number",
    CAST("position" AS INT) AS "position",
    CAST("q1" AS TEXT) AS "q1",
    CAST("q2" AS TEXT) AS "q2",
    CAST("q3" AS TEXT) AS "q3"
FROM 
    {{ source('raw', 'qualifying') }}