-- stg_results.sql

SELECT 
    CAST("index" AS INT) AS "index",
    CAST("result_id" AS INT) AS "result_id",
    CAST("race_id" AS INT) AS "race_id",
    CAST("driver_id" AS INT) AS "driver_id",
    CAST("constructor_id" AS INT) AS "constructor_id",
    CAST("number" AS TEXT) AS "number",
    CAST("grid" AS INT) AS "grid",
    CAST("position" AS TEXT) AS "position",
    CAST("position_text" AS TEXT) AS "position_text",
    CAST("position_order" AS INT) AS "position_order",
    CAST("points" AS FLOAT) AS "points",
    CAST("laps" AS INT) AS "laps",
    CAST("time" AS TEXT) AS "time",
    CAST("milliseconds" AS TEXT) AS "milliseconds",
    CAST("fastest_lap" AS TEXT) AS "fastest_lap",
    CAST("rank" AS TEXT) AS "rank",
    CAST("fastest_lap_time" AS TEXT) AS "fastest_lap_time",
    CAST("fastest_lap_speed" AS TEXT) AS "fastest_lap_speed",
    CAST("status_id" AS INT) AS "status_id"
FROM 
    {{ source('raw', 'results') }}