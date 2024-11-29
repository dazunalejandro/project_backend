CREATE DATABASE IF NOT EXISTS sports_calendar;
USE sports_calendar;

CREATE TABLE IF NOT EXISTS Sport (
    sport_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS Venue (
    venue_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    location VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS Team (
    team_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    sport_id INT,
    FOREIGN KEY (sport_id) REFERENCES Sport(sport_id) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS Event (
    event_id INT AUTO_INCREMENT PRIMARY KEY,
    event_date DATE NOT NULL,
    event_time TIME NOT NULL,
    sport_id INT,
    venue_id INT,
    home_team_id INT,
    visitor_team_id INT,
    description VARCHAR(255),
    FOREIGN KEY (sport_id) REFERENCES Sport(sport_id) ON DELETE SET NULL,
    FOREIGN KEY (venue_id) REFERENCES Venue(venue_id) ON DELETE SET NULL,
    FOREIGN KEY (home_team_id) REFERENCES Team(team_id) ON DELETE SET NULL,
    FOREIGN KEY (visitor_team_id) REFERENCES Team(team_id) ON DELETE SET NULL
);

