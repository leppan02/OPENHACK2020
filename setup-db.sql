CREATE TABLE trades (
    id SERIAL PRIMARY KEY,
    country_from varchar(500) NOT NULL,
    country_to varchar(500) NOT NULL,
    weapon_name varchar(500),
    amount INT,
    trade_start DATE,
    trade_end DATE
);

CREATE TABLE weapons (
    weapon_name varchar(500) PRIMARY KEY NOT NULL,
    category varchar(500)
);
