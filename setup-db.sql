CREATE TABLE trades (
    id SERIAL PRIMARY KEY,
    country_from varchar(500) NOT NULL,
    country_to varchar(500) NOT NULL,
    weapon_name varchar(500),
    amount INT,
    trade_start DATE,
    trade_end DATE,
    is_verified boolean NOT NULL DEFAULT false,
    source varchar(500) NOT NULL
);

CREATE TABLE weapons (
    weapon_name varchar(500) PRIMARY KEY NOT NULL,
    category varchar(500)
);

CREATE TABLE conflicts (
    id SERIAL PRIMARY KEY,
    country varchar(500) NOT NULL,
    info varchar(5000) NOT NULL,
    date_start DATE,
    date_end DATE,
    picture_url varchar(5000),
    verified boolean NOT NULL DEFAULT false,
    source varchar(500) NOT NULL
);
