-- stg_driver_standings.sql

SELECT 
    CAST("index" AS INT) AS "index",
    CAST("driver_standings_id" AS INT) AS "driver_standings_id",
    CAST("race_id" AS INT) AS "race_id",
    CAST("driver_id" AS INT) AS "driver_id",
    CAST("points" AS FLOAT) AS "points",
    CAST("position" AS INT) AS "position",
    CAST("position_text" AS TEXT) AS "position_text",
    CAST("wins" AS INT) AS "wins"
FROM 
    {{ source('raw', 'driver_standings') }}