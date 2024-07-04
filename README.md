# TurboInsights

### Project Overview
TurboInsights is a data engineering project that focuses on analyzing car listing data from CarGurus.com. This project leverages PySpark for data ingestion, transformation, and loading, MySQL for data warehousing and data mart creation, and Power BI for visualization and reporting. TurboInsights aims to provide insightful analytics on the car listing data, facilitating informed decision-making. Check out the final dashboard using this link: https://drive.google.com/drive/folders/1L5o1xxy59sc7M3tpxK4-GHPQzI0QDB7b?usp=drive_link

### Project Structure
The project is structured into several key components:

1. Data Ingestion: Extracting data from Kaggle and loading it into a staging area.
2. Data Transformation: Cleaning, transforming, and enriching the data using PySpark.
3. Data Storage: Storing the transformed data in a MySQL data warehouse.
4. Data Mart Creation: Building a data mart from the data warehouse for efficient querying and analysis.
5. Visualization: Creating interactive dashboards in Power BI to visualize and report the data insights.

### Technologies Used
* PySpark: For data ingestion, transformation, and enrichment.
* MySQL: For data warehousing and data mart creation.
* Power BI: For data visualization and reporting.

### Data Pipeline
The data pipeline consists of the following steps:

1. Data Extraction: The Data was extracted from CarGurus.com using a webscraping code and saved as a CSV file on Kaggle. Kaggle API was used to download the data and unzip it.
2. Data Loading: The CSV file is loaded into a staging area using PySpark. -- put image here --
3. Data Transformation:
    * Dropping unrelevant columns from the dataset.
    * Cleaning null values.
    * Filtering wrong data.
    * Changing columns data types.
    * Parsing columns that contains numerical values.
    * Transforming the data into fact & dimension tables.
    * Joining & merging dataframes to fit into a snowflake schema.
4. Data Storage: The transformed data is stored in a MySQL data warehouse.
5. Data Mart Creation: A data mart focused on dealers perforamnce is created from the data warehouse for optimized analytical queries.

### Data Warehouse Schema
The data warehouse is designed using a snowflake schema to handle the large and complex car listings data efficiently. The snowflake schema ensures that data is normalized, reducing redundancy and improving query performance. This structure allows for detailed and accurate analysis of the car listings data. -- put image here--

### Data Mart
The data mart is focused on dealer performance metrics, providing a streamlined subset of the data warehouse tailored for analytical queries related to dealers, making it easier to perform specific analytical queries related to dealer performance. This structure supports efficient reporting and visualization in Power BI.

### Dashboard
The Power BI dashboard is built using the data from the data mart. It provides a comprehensive view of dealer performance, offering insights such as:
* **Dealer Activity**
* **Price Distribution**
* **Distribution of Cars Vendors**

### Conclusion
TurboInsights provides a robust framework for analyzing car listings data, from data ingestion and transformation to storage and visualization. By leveraging PySpark, MySQL, and Power BI, this project demonstrates how to build a scalable and efficient data engineering solution for real-world data analysis.

- - - -
Feel free to reach out for any questions or further improvements!

Happy Analyzing!
- - - -

**Author:** Zaid Hani Allwansah

**Contact:** allwazaid1@gmail.com

**LinkedIn:** https://www.linkedin.com/in/zaid-allwansah/
