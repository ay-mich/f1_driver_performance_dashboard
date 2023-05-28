-- stg_constructors.sql

SELECT 
    CAST("index" AS INT) AS "index",
    CAST("constructor_id" AS INT) AS "constructor_id",
    CAST("constructor_ref" AS TEXT) AS "constructor_ref",
    CAST("name" AS TEXT) AS "name",
    CAST("nationality" AS TEXT) AS "nationality",
    CAST("url" AS TEXT) AS "url"
FROM 
    {{ source('raw', 'constructors') }}
