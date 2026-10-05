<div align="center">

# 🕊️ FarewellHub

### End-to-End Funeral Services Data & Analytics Project

**Website → Google Sheets → Data Studio → Databricks → SQL → Business Insights**

<p>
  Turning collected funeral-service information into organised data, analysis, visual reporting and business insights.
</p>

</div>

---

<p align="center">
  <img src="images/FarewellHub-Banner.png" alt="FarewellHub Banner" width="100%">
</p>

---

# 📌 Project Overview

FarewellHub is an end-to-end data analytics project built around a funeral services platform.

The project demonstrates how information can be collected from a website, organised into a structured dataset, connected to reporting tools, processed in Databricks and analysed using SQL.

The objective was not only to create a dashboard, but to demonstrate the **complete journey of data from collection to decision-making**.

### 🔄 End-to-End Data Flow

```text
┌─────────────────┐
│     WEBSITE     │
│                 │
│ Information     │
│ Collection      │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  GOOGLE SHEETS  │
│                 │
│ Data Collection │
│ & Organisation  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   DATA STUDIO   │
│                 │
│ Visual Reporting│
│ & Exploration   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│    DATABRICKS   │
│                 │
│ Data Processing │
│ & Preparation   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│       SQL       │
│                 │
│ Business        │
│ Analysis        │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│    INSIGHTS     │
│                 │
│ Findings &      │
│ Recommendations │
└─────────────────┘
#🎯 Business Objective

The purpose of the project was to demonstrate how raw information can be transformed into useful business information.

The project focused on:

Collecting information from a website
Organising the information into a structured format
Connecting the dataset to a visual reporting platform
Bringing the data into Databricks
Performing data preparation and transformation
Using SQL to answer business questions
Creating meaningful visualisations
Turning analysis into business insights

#🌐 1. Website

The website represents the starting point of the data journey.

Information was collected through the FarewellHub platform and prepared for further analysis.

Website → Data
Website
   ↓
Information captured
   ↓
Structured records
   ↓
Google Sheets

The website provides the front-end environment where information can be collected before being transferred into the analytical workflow.

#📊 2. Google Sheets — Data Collection

Google Sheets was used as the initial structured data collection environment.

The information collected from the website was organised into rows and columns so that it could be used for reporting and further processing.

Data workflow
Website Information
        ↓
Google Sheets
        ↓
Structured Dataset
        ↓
Data Validation

This stage helped establish a consistent dataset before moving into the analytical environment.

#📈 3. Google Data Studio — Visual Reporting

The Google Sheets dataset was connected to Google Data Studio to create visual reporting.

This allowed the information to be explored through:

Charts
Tables
Filters
Summary views
Interactive reporting
Reporting workflow
Google Sheets
      ↓
Google Data Studio
      ↓
Interactive Reporting
      ↓
Business Understanding

The dashboard provided an initial visual view of the information before deeper SQL analysis was performed.

#🧱 4. Databricks — Data Processing

Databricks was used as the analytical environment for working with the dataset.

The data was brought into Databricks so that it could be examined, prepared and queried using SQL.

Databricks workflow
Raw Dataset
     ↓
Data Inspection
     ↓
Data Quality Checks
     ↓
Cleaning
     ↓
Transformation
     ↓
SQL Analysis

The Databricks stage allowed the project to move from simple reporting into a more structured analytical workflow.

#🔍 5. Data Understanding

Before analysing the information, the dataset was reviewed to understand:

Available fields
Data types
Missing information
Duplicate records
Inconsistent values
Relationships between fields
Available business dimensions
Potential analytical questions

The aim was to understand the data before making conclusions from it.

#🧹 6. Data Preparation

Data preparation was an important part of the project.

The workflow included reviewing the data for potential quality issues and preparing it for analysis.

Preparation process
Raw Data
   ↓
Check Structure
   ↓
Check Missing Values
   ↓
Check Duplicates
   ↓
Check Consistency
   ↓
Clean / Transform
   ↓
Analysis-Ready Data

This ensured that the analysis was based on a structured dataset rather than simply querying unprepared information.

#🧮 7. SQL Analysis

SQL was used in Databricks to answer business questions from the prepared dataset.

The analysis followed a simple approach:

Business Question
       ↓
SQL Query
       ↓
Result
       ↓
Interpretation
       ↓
Business Insight
Example SQL workflow
SELECT
    *
FROM farewellhub_data
LIMIT 10;

The initial queries were used to understand the available data before moving into more detailed analysis.

#💡 8. Business Questions

The SQL analysis was structured around business questions rather than simply writing queries.

Examples include:

Data Overview
SELECT
    COUNT(*) AS total_records
FROM farewellhub_data;
Category Analysis
SELECT
    category,
    COUNT(*) AS total_records
FROM farewellhub_data
GROUP BY category
ORDER BY total_records DESC;
Location Analysis
SELECT
    location,
    COUNT(*) AS total_records
FROM farewellhub_data
GROUP BY location
ORDER BY total_records DESC;
Trend Analysis
SELECT
    date,
    COUNT(*) AS total_records
FROM farewellhub_data
GROUP BY date
ORDER BY date;

Note: The final SQL queries were developed according to the actual fields available in the FarewellHub dataset.

#📊 9. Analysis & Visualisation

The project used two complementary approaches to reporting.

Google Data Studio

Used for interactive visual exploration and dashboard reporting.

Databricks SQL

Used for deeper querying, analysis and validation.

Together, they created the following workflow:

Data
 ↓
Visual Exploration
 ↓
SQL Analysis
 ↓
Business Questions
 ↓
Insights

#💡 10. From Data to Business Insights

The objective of the project was not simply to produce charts.

The analysis followed the principle:

Data → Finding → Meaning → Action

For every important finding, the following questions were considered:

What happened?

What does the data show?

Why does it matter?

Why is the finding important to the business?

What should happen next?

What action could be considered based on the finding?

#📌 11. Key Analytical Areas

The project can be used to analyse areas such as:

Area	Purpose
Service Information	Understand available funeral-related services
Location	Understand geographical distribution
Categories	Compare different service categories
Trends	Identify changes over time
Records	Monitor volumes and activity
Customer Information	Understand available customer-related data
Business Performance	Identify areas requiring attention

#🏗️ Project Architecture
                    FAREWELLHUB
                         │
                         ▼
                ┌─────────────────┐
                │     WEBSITE     │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │  GOOGLE SHEETS  │
                │                 │
                │ Data Collection │
                └────────┬────────┘
                         │
              ┌──────────┴──────────┐
              ▼                     ▼
     ┌─────────────────┐   ┌─────────────────┐
     │   DATA STUDIO   │   │    DATABRICKS   │
     │                 │   │                 │
     │ Visual Reporting│   │ Data Processing │
     └─────────────────┘   └────────┬────────┘
                                    │
                                    ▼
                           ┌─────────────────┐
                           │       SQL       │
                           │                 │
                           │ Data Analysis   │
                           └────────┬────────┘
                                    │
                                    ▼
                           ┌─────────────────┐
                           │    INSIGHTS     │
                           │                 │
                           │ Recommendations │
                           └─────────────────┘
#🛠️ Technology Stack
Tool	Purpose
🌐 Website	Information collection
📊 Google Sheets	Data collection and organisation
📈 Google Data Studio	Interactive visual reporting
🧱 Databricks	Data processing and analysis
🧮 SQL	Data querying and business analysis
🐙 GitHub	Project documentation and portfolio
📁 Project Structure
FarewellHub/
│
├── README.md
│
├── 1. Website/
│   ├── Screenshots/
│   └── Website Documentation
│
├── 2. Data Collection/
│   └── Google Sheets/
│
├── 3. Data Visualisation/
│   ├── Data Studio/
│   └── Dashboard Screenshots/
│
├── 4. Data Processing/
│   ├── Data Quality Checks.sql
│   ├── Data Cleaning.sql
│   └── Data Transformation.sql
│
├── 5. SQL Analysis/
│   ├── Business Questions.sql
│   ├── Service Analysis.sql
│   ├── Customer Analysis.sql
│   └── Trend Analysis.sql
│
├── 6. Insights/
│   └── Business Insights.md
│
└── 7. Presentation/
    └── FarewellHub Presentation

#📸 Project Screenshots
🌐 Website
<p align="center"> <img src="images/website.png" alt="FarewellHub Website" width="90%"> </p>
📊 Google Sheets
<p align="center"> <img src="images/google-sheets.png" alt="FarewellHub Google Sheets Dataset" width="90%"> </p>
📈 Google Data Studio
<p align="center"> <img src="images/data-studio.png" alt="FarewellHub Data Studio Dashboard" width="90%"> </p>
🧱 Databricks
<p align="center"> <img src="images/databricks.png" alt="FarewellHub Databricks Analysis" width="90%"> </p>
📋 Project Workflow

The complete project followed this workflow:

1. Build / use FarewellHub website
             ↓
2. Collect information
             ↓
3. Organise information in Google Sheets
             ↓
4. Connect dataset to Google Data Studio
             ↓
5. Explore information visually
             ↓
6. Bring data into Databricks
             ↓
7. Inspect and prepare the data
             ↓
8. Write SQL queries
             ↓
9. Answer business questions
             ↓
10. Identify insights
             ↓
11. Develop recommendations
             ↓
12. Document the complete project on GitHub

#🎓 What I Learned

This project helped me practise the complete data analytics process rather than focusing on SQL alone.

Technical Skills
Data collection
Data organisation
Data preparation
Data quality checking
SQL querying
Databricks
Google Sheets
Google Data Studio
Data visualisation
GitHub documentation
Analytical Skills
Translating business needs into questions
Understanding a dataset before analysing it
Identifying patterns
Comparing categories
Looking for trends
Communicating findings
Turning findings into recommendations

#🎯 The Business Analyst Approach

One of the main lessons from this project was that analytics is not simply about writing code.

The workflow is:

BUSINESS PROBLEM
       ↓
BUSINESS QUESTION
       ↓
DATA
       ↓
ANALYSIS
       ↓
FINDING
       ↓
INSIGHT
       ↓
RECOMMENDATION
       ↓
BUSINESS ACTION

The tools support the process, but the final objective is to help people make better decisions.

#🚀 Future Improvements

Future versions of FarewellHub could include:

Automated data collection
Automated data pipelines
Additional business KPIs
More advanced SQL analysis
Customer segmentation
Geographic analysis
Automated dashboard refreshes
Predictive analytics
Additional Power BI reporting
Automated data-quality monitoring

#👩‍💻 Author
Alice

Data Analyst | Business Analysis | SQL | Python | Excel | Power BI | Databricks

This project forms part of my data analytics portfolio and demonstrates my ability to take a project from data collection through to analysis, visualisation and business insight.

<div align="center">
🕊️ FarewellHub

From information → to data → to insight → to better decisions.

</div> ```
