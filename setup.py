# this file contains the code to setup the data for this project
import requests
import sqlalchemy
import kaggle

# setting up the main cars dataset
# kaggle.api.authenticate()
# kaggle.api.dataset_download_files(dataset='ananaymital/us-used-cars-dataset', path='./data', unzip=True)

# setting up the dataset:

from mysql.connector import connect

mydb = connect(
  host='localhost',
  user='root',
  password='anon'
)

cursor = mydb.cursor()
cursor.execute('CREATE DATABASE IF NOT EXISTS cars;')
cursor.close()
mydb.close()

mydb = connect(
  host='localhost',
  user='root',
  password='anon',
  database='cars'
)
cursor = mydb.cursor()
cursor.execute('''-- begin-sql
                CREATE TABLE IF NOT EXISTS dim_vehicle_interior(
                 interior_id INT NOT NULL
                 ,front_legroom_inches FLOAT
                 ,interior_color VARCHAR(255)
                 ,maximum_seating INT
                 ,back_legroom_inches FLOAT
                 ,PRIMARY KEY(interior_id)); -- end-sql
                 
              -- begin-sql
               CREATE TABLE IF NOT EXISTS dim_vehicle_body(
                 body_id INT NOT NULL
                 ,trimId VARCHAR(255)
                 ,trim_name VARCHAR(255)
                 ,model_name VARCHAR(255)
                 ,make_name VARCHAR(255)
                 ,body_type VARCHAR(255)
                 ,wheel_system VARCHAR(3)
                 ,franchise_make VARCHAR(255)
                 ,wheel_system_display VARCHAR(255)
                 ,exterior_color VARCHAR(255)
                 ,listing_color VARCHAR(255)
                 ,wheelbase_inches FLOAT
                 ,height_inches FLOAT
                 ,length_inches FLOAT
                 ,width_inches FLOAT
                 ,PRIMARY KEY(body_id)); -- end-sql
                 
              -- begin-sql
               CREATE TABLE IF NOT EXISTS dim_vehicle_engine(
                 engine_id INT NOT NULL
                 ,engine_cylinders VARCHAR(255)
                 ,engine_displacement FLOAT
                 ,engine_type VARCHAR(255)
                 ,torque_lbft INT
                 ,torque_rpm INT
                 ,power_hp INT
                 ,power_rpm INT
                 ,PRIMARY KEY(engine_id)); -- end-sql
                 
              -- begin-sql
               CREATE TABLE IF NOT EXISTS dim_vehicle_transmission(
                 transmission_id INT NOT NULL
                 ,transmission CHAR
                 ,transmission_display VARCHAR(255)
                 ,PRIMARY KEY(transmission_id)
               ); -- end-sql
               
              -- begin-sql
               CREATE TABLE IF NOT EXISTS dim_vehicle_fuel(
                 fuel_id INT NOT NULL
                 ,fuel_tank_volume_gallons FLOAT
                 ,fuel_type VARCHAR(255)
                 ,city_fuel_economy FLOAT
                 ,highway_fuel_economy FLOAT
                 ,PRIMARY KEY(fuel_id)); -- end-sql
                 
              -- begin-sql
               CREATE TABLE IF NOT EXISTS dim_vehicle(
                 vehicle_surrogate_id INT NOT NULL
                 ,vin VARCHAR(17) NOT NULL
                 ,interior_id INT NOT NULL
                 ,body_id INT NOT NULL
                 ,engine_id INT NOT NULL
                 ,fuel_id INT NOT NULL
                 ,transmission_id INT NOT NULL
                 ,major_options VARCHAR(2550)
                 ,year_of_make INT(4)
                 ,description VARCHAR(25500)
                 ,PRIMARY KEY(vehicle_surrogate_id)
                 ,CONSTRAINT fk_interior FOREIGN KEY (interior_id) REFERENCES dim_vehicle_interior(interior_id)
                 ,CONSTRAINT fk_body FOREIGN KEY (body_id) REFERENCES dim_vehicle_body(body_id)
                 ,CONSTRAINT fk_engine FOREIGN KEY (engine_id) REFERENCES dim_vehicle_engine(engine_id)
                 ,CONSTRAINT fk_fuel FOREIGN KEY (fuel_id) REFERENCES dim_vehicle_fuel(fuel_id)
                 ,CONSTRAINT fk_transmission FOREIGN KEY (transmission_id) REFERENCES dim_vehicle_transmission(transmission_id) ); -- end-sql
               
              -- begin-sql
               CREATE TABLE IF NOT EXISTS dim_date(
                 date_id INT NOT NULL
                 ,listed_date DATE
                 ,year INT(4)
                 ,month INT(2)
                 ,day INT(2)
                 ,PRIMARY KEY(date_id)); -- end-sql
              
              -- begin-sql
               CREATE TABLE IF NOT EXISTS dim_dealer(
                 dealer_surrogate_id INT NOT NULL
                 ,dealer_id INT
                 ,dealer VARCHAR(255)
                 ,dealer_zip INT
                 ,franchise_dealer BOOLEAN
                 ,seller_rating FLOAT
                 ,PRIMARY KEY(dealer_surrogate_id)); -- end-sql
                 
              -- begin-sql
               CREATE TABLE IF NOT EXISTS dim_location(
                 location_id INT NOT NULL
                 ,longitude FLOAT
                 ,latitude FLOAT
                 ,city VARCHAR(255)
                 ,PRIMARY KEY(location_id)); -- end-sql
                 
              -- begin-sql
               CREATE TABLE IF NOT EXISTS dim_ownership_status(
                 ownership_status_id INT NOT NULL
                 ,owner_count INT
                 ,fleet BOOLEAN
                 ,frame_damaged BOOLEAN
                 ,has_accidents BOOLEAN
                 ,isCab BOOLEAN
                 ,is_cpo BOOLEAN
                 ,is_oemcpo BOOLEAN
                 ,salvage BOOLEAN
                 ,theft_title BOOLEAN
                 ,PRIMARY KEY(ownership_status_id));  -- end-sql
              
              -- begin-sql
               CREATE TABLE IF NOT EXISTS fact_listings(
                 listing_surrogate_id INT NOT NULL
                 ,listing_id INT NOT NULL
                 ,dealer_surrogate_id INT NOT NULL
                 ,location_id INT NOT NULL
                 ,date_id INT NOT NULL
                 ,vehicle_surrogate_id INT NOT NULL
                 ,ownership_status_id INT NOT NULL
                 ,savings_amount FLOAT
                 ,mileage FLOAT
                 ,daysonmarket INT
                 ,price FLOAT
                 ,PRIMARY KEY(listing_surrogate_id)
                 ,CONSTRAINT fk_location FOREIGN KEY (location_id) REFERENCES dim_location(location_id)
                 ,CONSTRAINT fk_dealer FOREIGN KEY (dealer_surrogate_id) REFERENCES dim_dealer(dealer_surrogate_id)
                 ,CONSTRAINT fk_date FOREIGN KEY (date_id) REFERENCES dim_date(date_id)
                 ,CONSTRAINT fk_vehicle FOREIGN KEY (vehicle_surrogate_id) REFERENCES dim_vehicle(vehicle_surrogate_id)
                 ,CONSTRAINT fk_owner FOREIGN KEY (ownership_status_id) REFERENCES dim_ownership_status(ownership_status_id)); -- end-sql''')
cursor.close()