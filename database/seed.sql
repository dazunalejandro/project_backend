-- Insert data into Sport table
INSERT INTO Sport (sport_id, name) VALUES 
(1, 'Soccer'),
(2, 'Basketball'),
(3, 'Tennis'),
(4, 'Cricket'),
(5, 'Volleyball');

-- Insert data into Venue table
INSERT INTO Venue (venue_id, name, location) VALUES 
(1, 'City Stadium', 'Downtown'),
(2, 'Sports Arena', 'Uptown'),
(3, 'Community Park', 'Suburbs'),
(4, 'National Gym', 'Capital City'),
(5, 'Beachside Court', 'Coastal Area');

-- Insert data into Team table
INSERT INTO Team (team_id, name, sport_id) VALUES 
(1, 'Red Hawks', 1),
(2, 'Blue Whales', 1),
(3, 'Green Giants', 2),
(4, 'Yellow Tigers', 3),
(5, 'Purple Panthers', 1),
(6, 'Orange Owls', 2),
(7, 'White Wolves', 3),
(8, 'Black Bears', 1),
(9, 'Golden Eagles', 2),
(10, 'Silver Sharks', 3),
(11, 'Crimson Cobras', 4),
(12, 'Emerald Elephants', 5),
(13, 'Sapphire Snakes', 4),
(14, 'Ruby Rhinos', 5),
(15, 'Indigo Iguanas', 3),
(16, 'Amber Ants', 2),
(17, 'Turquoise Turtles', 4),
(18, 'Violet Vultures', 5),
(19, 'Teal Tigers', 1),
(20, 'Lavender Leopards', 3);

-- Insert data into Event table
INSERT INTO Event (event_id, event_date, event_time, sport_id, venue_id, description, home_team_id, visitor_team_id) VALUES 
(1, '2024-12-01', '15:00:00', 1, 1, 'Local Soccer Tournament', 1, 2),
(2, '2024-12-02', '18:00:00', 2, 2, 'Regional Basketball Game', 3, 6),
(3, '2024-12-03', '10:00:00', 3, 3, 'Tennis Match Finals', 4, 7),
(4, '2024-12-04', '12:00:00', 4, 4, 'National Cricket Championship', 11, 17),
(5, '2024-12-05', '17:30:00', 5, 5, 'Beach Volleyball Open', 12, 14),
(6, '2024-12-06', '14:00:00', 1, 1, 'Soccer Semi-Finals', 5, 8),
(7, '2024-12-07', '16:00:00', 2, 2, 'Basketball League Game', 9, 16),
(8, '2024-12-08', '09:00:00', 3, 3, 'Friendly Tennis Match', 7, 15),
(9, '2024-12-09', '11:00:00', 4, 4, 'Junior Cricket League', 13, 17),
(10, '2024-12-10', '18:30:00', 5, 5, 'Coastal Volleyball Cup', 14, 18),
(11, '2024-12-11', '15:00:00', 1, 1, 'City Soccer Derby', 8, 19),
(12, '2024-12-12', '19:00:00', 2, 2, 'All-Star Basketball Night', 6, 3),
(13, '2024-12-13', '13:00:00', 3, 3, 'Tennis Club Match', 10, 4),
(14, '2024-12-14', '14:30:00', 4, 4, 'Cricket Super Series', 17, 11),
(15, '2024-12-15', '10:00:00', 5, 5, 'International Volleyball Match', 18, 12),
(16, '2024-12-16', '17:00:00', 1, 1, 'Soccer Charity Match', 1, 5),
(17, '2024-12-17', '16:00:00', 2, 2, 'Regional Basketball Finals', 3, 9),
(18, '2024-12-18', '09:30:00', 3, 3, 'Tennis Doubles Tournament', 7, 15),
(19, '2024-12-19', '11:30:00', 4, 4, 'Cricket World Cup Qualifiers', 13, 11),
(20, '2024-12-20', '20:00:00', 5, 5, 'Beach Volleyball Night Show', 14, 18);
