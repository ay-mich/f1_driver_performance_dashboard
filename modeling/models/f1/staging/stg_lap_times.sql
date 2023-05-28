-- stg_lap_times.sql

SELECT 
    CAST("index" AS INT) AS "index",
    CAST("race_id" AS INT) AS "race_id",
    CAST("driver_id" AS INT) AS "driver_id",
    CAST("lap" AS INT) AS "lap",
    CAST("position" AS INT) AS "position",
    CAST("time" AS TEXT) AS "time",
    CAST("milliseconds" AS INT) AS "milliseconds"
FROM 
    {{ source('raw', 'lap_times') }}