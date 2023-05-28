-- stg_races.sql

SELECT 
    CAST("index" AS INT) AS "index",
    CAST("race_id" AS INT) AS "race_id",
    CAST("year" AS INT) AS "year",
    CAST("round" AS INT) AS "round",
    CAST("circuit_id" AS INT) AS "circuit_id",
    CAST("name" AS TEXT) AS "name",
    CAST("date" AS TEXT) AS "date",
    CAST("time" AS TEXT) AS "time",
    CAST("url" AS TEXT) AS "url",
    CAST("fp1_date" AS TEXT) AS "fp1_date",
    CAST("fp1_time" AS TEXT) AS "fp1_time",
    CAST("fp2_date" AS TEXT) AS "fp2_date",
    CAST("fp2_time" AS TEXT) AS "fp2_time",
    CAST("fp3_date" AS TEXT) AS "fp3_date",
    CAST("fp3_time" AS TEXT) AS "fp3_time",
    CAST("quali_date" AS TEXT) AS "quali_date",
    CAST("quali_time" AS TEXT) AS "quali_time",
    CAST("sprint_date" AS TEXT) AS "sprint_date",
    CAST("sprint_time" AS TEXT) AS "sprint_time"
FROM 
    {{ source('raw', 'races') }}