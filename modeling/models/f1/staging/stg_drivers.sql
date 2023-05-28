-- stg_drivers.sql

SELECT 
    CAST("index" AS INT) AS "index",
    CAST("driver_id" AS INT) AS "driver_id",
    CAST("driver_ref" AS TEXT) AS "driver_ref",
    CAST("number" AS TEXT) AS "number",
    CAST("code" AS TEXT) AS "code",
    CAST("forename" AS TEXT) AS "forename",
    CAST("surname" AS TEXT) AS "surname",
    CAST("dob" AS DATE) AS "dob",
    CAST("nationality" AS TEXT) AS "nationality",
    CAST("url" AS TEXT) AS "url"
FROM 
    {{ source('raw', 'drivers') }}
