import logging as log

import pandas as pd

# Configure logger
log.basicConfig(level=log.INFO)


def get_data(query: str, driver_id: int, conn) -> pd.DataFrame:
    """
    Fetches data from database based on the query.

    Args:
        query (str): The query to fetch data.
        driver_id (str): The driver ID.
        conn: The database connection instance.

    Returns:
        df (DataFrame): Dataframe containing the fetched data.

    Raises:
        ValueError: If no data is returned from the query.
        Exception: If there is an issue executing the query.
    """
    df = None
    try:
        if query == "driver_comparison_query":
            q = driver_comparison_query(driver_id)
            df = pd.read_sql_query(q, conn)
    except Exception as e:
        log.error(f"Error executing query '{query}': {e}", exc_info=True)
        raise

    if df is not None:
        return df
    else:
        raise ValueError(f"No data returned from query '{query}'")


def driver_comparison_query(driver_id: int):
    """
    Creates the SQL query string for driver comparison.

    Args:
        driver_id (str): The driver ID.

    Returns:
        str: The SQL query string.

    Raises:
        Exception: If there is an issue creating the query string.
    """
    try:
        return f"""
        WITH main AS (
    SELECT 
        -- meta
        ra.date, 
        re.race_id,
        ra.name AS circuit_name,
        re.constructor_id,
        c.name AS constructor_name,
        
        -- main driver
        re.driver_id AS main_id, 
        d.driver_ref AS main_name,
        
        -- key stats
        CASE WHEN position::int = 1 THEN 1 ELSE 0 END AS main_wins, 
        position AS main_position,
        points AS main_points,
        grid AS main_grid,
        laps AS main_laps_completed,
        fastest_lap_time as main_lap_time

    FROM 
        public_staging.stg_results re
        JOIN public_staging.stg_races ra ON re.race_id = ra.race_id
        JOIN public_staging.stg_drivers d ON re.driver_id = d.driver_id
        JOIN public_staging.stg_constructors c ON re.constructor_id = c.constructor_id
    WHERE 
        re.driver_id = {driver_id}
),

team_mate AS (
    SELECT 
        -- meta
        ra.date, 
        re.race_id, 
        re.constructor_id, 
        
        -- team mate driver
        re.driver_id AS mate_id, 
        d.driver_ref AS mate_name,
        
        -- key stats
        CASE WHEN position::int = 1 THEN 1 ELSE 0 END AS mate_wins,
        position AS mate_position,
        points AS mate_points,
        grid AS mate_grid,
        laps AS mate_laps_completed,
        fastest_lap_time as mate_lap_time

    FROM 
        public_staging.stg_results re
        JOIN public_staging.stg_races ra ON re.race_id = ra.race_id
        JOIN public_staging.stg_drivers d ON re.driver_id = d.driver_id
    WHERE 
        re.driver_id != {driver_id} AND (ra.date, re.constructor_id) IN (SELECT date, constructor_id FROM main)
),

_final AS (
    SELECT 
        *, 
        CASE 
            WHEN main_lap_time < mate_lap_time THEN 1 
            ELSE 0 
        END AS main_fastest_lap,
        CASE 
            WHEN mate_lap_time < main_lap_time THEN 1 
            ELSE 0 
        END AS mate_fastest_lap
    FROM 
        main
        JOIN team_mate USING (date, constructor_id)
)
-- Main driver data
SELECT 
    -- meta
    date, 
    constructor_name,
    circuit_name,

    -- driver
    main_name AS driver_name, 
    main_wins AS wins, 
    main_position AS position, 
    main_points AS points, 
    main_grid AS grid, 
    main_laps_completed AS laps_completed,
    main_lap_time AS lap_time,
    main_fastest_lap AS fastest_lap,

    -- flag for main driver
    'main' AS driver_type

FROM 
    _final

UNION ALL

-- Team mate data
SELECT 
    -- meta
    date, 
    constructor_name,
    circuit_name,

    -- driver
    mate_name AS driver_name, 
    mate_wins AS wins, 
    mate_position AS position, 
    mate_points AS points, 
    mate_grid AS grid, 
    mate_laps_completed AS laps_completed,
    mate_lap_time AS lap_time,
    mate_fastest_lap AS fastest_lap,

    -- flag for team mate
    'mate' AS driver_type

FROM 
    _final

ORDER BY 
    date, driver_type;
        """
    except Exception as e:
        log.error(
            f"Error creating SQL query for driver '{driver_id}': {e}", exc_info=True
        )
        raise
