CREATE SCHEMA IF NOT EXISTS raw;

CREATE TABLE IF NOT EXISTS raw.customers (
    customer_id INTEGER PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    signup_date DATE
);

CREATE TABLE IF NOT EXISTS raw.marketing_campaigns (
    campaign_id INTEGER PRIMARY KEY,
    campaign_name VARCHAR(100),
    channel VARCHAR(50),
    start_date DATE,
    budget DOUBLE PRECISION
);

CREATE TABLE IF NOT EXISTS raw.sales (
    sale_id INTEGER PRIMARY KEY,
    product_id INTEGER,
    customer_id INTEGER,
    amount DOUBLE PRECISION,
    date DATE,
    FOREIGN KEY (customer_id) REFERENCES raw.customers(customer_id)
);
