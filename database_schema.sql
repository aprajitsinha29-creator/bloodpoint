-- =====================================================
-- BloodPoint Database Schema
-- Author: Aprajit Shankar Sinha
-- Description: Schema for Blood Point application
-- Note: Contains table structure and award master data only
-- =====================================================

CREATE DATABASE IF NOT EXISTS bloodpoint;
USE bloodpoint;

-- =========================
-- Donor Table
-- =========================
CREATE TABLE donor (
    ID VARCHAR(20) PRIMARY KEY,
    Name VARCHAR(22) DEFAULT 'Anonymous',
    Mail VARCHAR(35),
    Phone CHAR(10) NOT NULL,
    DOB DATE NOT NULL,
    Password VARCHAR(20) NOT NULL,
    DOR DATE NOT NULL,
    no_donations INT,
    Awards VARCHAR(40),
    city VARCHAR(20) NOT NULL,
    last_date_of_donation DATE NOT NULL,
    Credit INT,
    Blood_group VARCHAR(3) NOT NULL,
    Age INT
);

-- =========================
-- Request Table
-- =========================
CREATE TABLE request (
    request_id VARCHAR(30) PRIMARY KEY,
    name VARCHAR(20) DEFAULT 'Anonymous',
    phone CHAR(10) NOT NULL,
    city VARCHAR(20) NOT NULL,
    bloodgrp VARCHAR(3) NOT NULL,
    date_of_request DATE,
    id VARCHAR(20)
);

-- =========================
-- Award Table
-- =========================
CREATE TABLE Award (
    Title VARCHAR(20) PRIMARY KEY,
    No_donation INT,
    Prize INT
);

-- =========================
-- Award Table Default Data
-- =========================
INSERT INTO Award (Title, No_donation, Prize) VALUES
('None', 0, 0),
('Lets Begin!', 1, 50),
('The Donater', 2, 100),
('Walking Blood Point', 3, 150),
('Saviour', 4, 200);
