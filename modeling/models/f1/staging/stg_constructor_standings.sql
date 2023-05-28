-- stg_constructor_standings.sql

SELECT 
    CAST("index" AS INT) AS "index",
    CAST("constructor_standings_id" AS INT) AS "constructor_standings_id",
    CAST("race_id" AS INT) AS "race_id",
    CAST("constructor_id" AS INT) AS "constructor_id",
    CAST("points" AS FLOAT) AS "points",
    CAST("position" AS INT) AS "position",
    CAST("position_text" AS TEXT) AS "position_text",
    CAST("wins" AS INT) AS "wins"
FROM 
    {{ source('raw', 'constructor_standings') }}
