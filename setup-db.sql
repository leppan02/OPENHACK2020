CREATE DATABASE hh;
CONNECT TO hh;
CREATE TABLE trades (id SERIAL PRIMARY KEY, country_from varchar(500), country_to varchar(500), thing varchar(500), amount INT, trade_start DATE, trade_end DATE);
INSERT INTO trades (country_from, country_to, thing, amount, trade_start, trade_end) VALUES ('Göteborg', 'Alfaganistan', 'bomb', 100, current_date - interval '20:00:00', current_date);
