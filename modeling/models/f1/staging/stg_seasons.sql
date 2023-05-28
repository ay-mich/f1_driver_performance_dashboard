-- stg_seasons.sql

SELECT 
    CAST("index" AS INT) AS "index",
    CAST("year" AS INT) AS "year",
    CAST("url" AS TEXT) AS "url"
FROM 
    {{ source('raw', 'seasons') }}