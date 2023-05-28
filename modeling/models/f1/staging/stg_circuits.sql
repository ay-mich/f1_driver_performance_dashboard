-- stg_circuits.sql

SELECT 
    CAST("index" AS INT) AS "index",
    CAST("circuit_id" AS INT) AS "circuit_id",
    CAST("circuit_ref" AS TEXT) AS "circuit_ref",
    CAST("name" AS TEXT) AS "name",
    CAST("location" AS TEXT) AS "location",
    CAST("country" AS TEXT) AS "country",
    CAST("lat" AS FLOAT) AS "lat",
    CAST("lng" AS FLOAT) AS "lng",
    CAST("alt" AS TEXT) AS "alt",
    CAST("url" AS TEXT) AS "url"
FROM 
    {{ source('raw', 'circuits') }}
