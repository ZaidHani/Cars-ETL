-- building a datamart about the dealers and their listing cars
CREATE DATABASE cars_sellers;
-- S C H E M A   B U I L D I N G
-- D E A L E R
CREATE TABLE cars_sellers.dim_dealer(
	dealer_surrogate_id INT
    ,dealer_id INT
    ,dealer_zip INT
    ,dealer VARCHAR(82)
    ,franchise_dealer BOOLEAN
    ,seller_rating FLOAT
    ,PRIMARY KEY(dealer_surrogate_id)
);
-- L O C A T I O N
CREATE TABLE cars_sellers.dim_location(
	location_id INT
    ,longitude FLOAT
	,latitude FLOAT
    ,city VARCHAR(30)
    ,PRIMARY KEY(location_id)
);
-- V E H I C L E
CREATE TABLE cars_sellers.dim_vehicle(
	vehicle_surrogate_id INT
    ,vin VARCHAR(17)
    ,model_name VARCHAR(30)
    ,year_of_make INT
    ,make_name VARCHAR(20)
    ,body_type VARCHAR(20)
    ,franchise_make VARCHAR(35)
    ,wheel_system VARCHAR(20)
    ,PRIMARY KEY(vehicle_surrogate_id)
);
-- L I S T I N G
CREATE TABLE cars_sellers.fact_listing(
	listing_id INT AUTO_INCREMENT
    ,dealer_surrogate_id INT
    ,location_id INT
    ,vehicle_surrogate_id INT
    ,saving_amount FLOAT
    ,days_on_market INT
    ,price FLOAT
    ,PRIMARY KEY(listing_id)
    ,CONSTRAINT fk_dealer FOREIGN KEY(dealer_surrogate_id) REFERENCES cars_sellers.dim_dealer(dealer_surrogate_id)
    ,CONSTRAINT fk_location FOREIGN KEY(location_id) REFERENCES cars_sellers.dim_location(location_id)
	,CONSTRAINT fk_vehicle FOREIGN KEY(vehicle_surrogate_id) REFERENCES cars_sellers.dim_vehicle(vehicle_surrogate_id)
);
-- POPULATE THE D-E-A-L-E-R TABLE
INSERT INTO 
	cars_sellers.dim_dealer(
		SELECT
			dealer_surrogate_id
			,dealer_id
            ,dealer_zip
			,dealer
			,franchise_dealer
			,seller_rating
		FROM
			cars.dim_dealer);
-- POPULATE THE L-O-C-A-T-I-O-N TALBE
INSERT INTO
	cars_sellers.dim_location(
		SELECT
			location_id
			,longitude
			,latitude
			,city
		FROM
			cars.dim_location);
-- POPULATE THE V-E-H-I-C-L-E TALBE
INSERT INTO 
	cars_sellers.dim_vehicle(
		SELECT 
			v.vehicle_surrogate_id
			,v.vin
			,model_name
			,year_of_make
			,make_name
			,body_type
			,franchise_make
			,wheel_system_display AS wheel_system
		FROM 
			cars.fact_listings fl
		LEFT JOIN
			cars.dim_vehicle v
		ON 
			v.vehicle_surrogate_id=fl.vehicle_surrogate_id
		LEFT JOIN
			cars.dim_vehicle_body vb
		ON 
			vb.body_id=v.body_id);
-- POPULATE THE L-I-S-T-I-N-G-S TABLE
INSERT INTO
	cars_sellers.fact_listing(
		dealer_surrogate_id
		,location_id
        ,vehicle_surrogate_id
        ,saving_amount
        ,days_on_market
        ,price)
(
		SELECT
			dealer_surrogate_id
			,location_id
			,vehicle_surrogate_id
			,savings_amount
			,daysonmarket AS days_on_market
			,price
		FROM
			cars.fact_listings);
            