# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "6"
# ///
import pandas as pd

# Google Sheets "Publish to web" CSV link — pulling from the "submissions" tab (gid=1309034753)
csv_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSdhz5TT6ZF4dXvwz58wsAGkvcb45ZDuzolpJnm9vensgr-bGuL88gjWgRgGxERGkKk3eS-10LrCfzm/pub?output=csv&gid=1309034753"

# Read live data using Pandas and convert it to a Spark DataFrame
pandas_df = pd.read_csv(csv_url)
spark_df = spark.createDataFrame(pandas_df)

# View your data inside Databricks
display(spark_df)


# COMMAND ----------

# Register the Spark DataFrame as a temp view for SQL queries
spark_df.createOrReplaceTempView("farewellhub_data")

display(spark.sql("""
-- QUERY 1: Find which Consulates take the longest to approve permits
-- NOTE: The submissions tab does not have Consulate Submission Date or Consulate Approval Date.
-- Adapted to show case count per destination country where consulate services are requested.
SELECT 
    destinationCountry,
    COUNT(*) AS Total_Cases
FROM farewellhub_data
WHERE destinationCountry IS NOT NULL
  AND servicesRequested LIKE '%Consulate%'
GROUP BY destinationCountry
ORDER BY Total_Cases DESC;
"""))


# COMMAND ----------

# MAGIC %sql
# MAGIC -- QUERY 2: Calculate average storage costs accumulating at different mortuaries
# MAGIC SELECT 
# MAGIC     mortuaryLocation,
# MAGIC     COUNT(deceasedFullName) AS Total_Active_Cases,
# MAGIC     SUM(dailyStorageCost * DATEDIFF(day, try_cast(dateOfDeath AS DATE), CURRENT_DATE())) AS Total_Accumulated_Storage_Cost
# MAGIC FROM farewellhub_data
# MAGIC WHERE clientPath != 'Completed'
# MAGIC GROUP BY mortuaryLocation;
# MAGIC