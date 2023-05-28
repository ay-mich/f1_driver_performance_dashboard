-- stg_pit_stops.sql

SELECT 
    CAST("index" AS INT) AS "index",
    CAST("race_id" AS INT) AS "race_id",
    CAST("driver_id" AS INT) AS "driver_id",
    CAST("stop" AS INT) AS "stop",
    CAST("lap" AS INT) AS "lap",
    CAST("time" AS TEXT) AS "time",
    CAST("duration" AS TEXT) AS "duration",
    CAST("milliseconds" AS INT) AS "milliseconds"
FROM 
    {{ source('raw', 'pit_stops') }}