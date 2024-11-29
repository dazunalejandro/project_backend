from http.server import BaseHTTPRequestHandler, HTTPServer
from tools.db_setup import execute_db_setup_files
from server_support import format_event_dates_and_times, ensure_attribute_exists
import mysql.connector
import json

execute_db_setup_files()

# MySQL Database Configuration
DB_CONFIG = {
    "host": "localhost",
    "user": "root",  # Replace with your MySQL username
    "password": "Quantum27?",  # Replace with your MySQL password
    "database": "sports_calendar"
}

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            # Serve the main HTML file
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            with open("frontend/index.html", "rb") as file:
                self.wfile.write(file.read())
        elif self.path == "/js/app.js":
            # Serve the JavaScript file
            self.send_response(200)
            self.send_header("Content-Type", "application/javascript")
            self.end_headers()
            with open("frontend/js/app.js", "rb") as file:
                self.wfile.write(file.read())
        elif self.path == "/css/style.css":
            # Serve the CSS file
            self.send_response(200)
            self.send_header("Content-Type", "text/css")
            self.end_headers()
            with open("frontend/css/style.css", "rb") as file:
                self.wfile.write(file.read())
        elif self.path == "/api/events":
            # Fetch events from the database
            connection = mysql.connector.connect(**DB_CONFIG)
            cursor = connection.cursor(dictionary=True)
            
            try:
                query = """
                    SELECT 
                        e.event_id,
                        e.event_date,
                        e.event_time,
                        s.name AS sport_name,
                        v.name AS venue_name,
                        ht.name AS home_team_name,
                        vt.name AS visitor_team_name,
                        e.description
                    FROM Event e
                    JOIN Sport s ON e.sport_id = s.sport_id
                    JOIN Venue v ON e.venue_id = v.venue_id
                    LEFT JOIN Team ht ON e.home_team_id = ht.team_id
                    LEFT JOIN Team vt ON e.visitor_team_id = vt.team_id
                    ORDER BY e.event_date, e.event_time
                    """

                cursor.execute(query)
                events = cursor.fetchall()
                events = format_event_dates_and_times(events)
            
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps(events).encode())
            except Exception as e:
                self.send_response(500)
                self.end_headers()
                self.wfile.write(f"Error fetching events: {str(e)}".encode())
            finally:
                cursor.close()
                connection.close()

    def do_POST(self):
        if self.path == "/api/events":
            # Handle adding a new event
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            new_event = json.loads(post_data)
            connection = mysql.connector.connect(**DB_CONFIG)
            cursor = connection.cursor()

            try:
                # Ensure sport exists in the database
                sport_id = ensure_attribute_exists(
                            cursor=cursor,
                            table="Sport",
                            column="name",
                            value=new_event["sport"],
                            connection=connection
                        )
                
                # Ensure venue exists
                venue_id = ensure_attribute_exists(
                            cursor=cursor,
                            table="Venue",
                            column="name",
                            value=new_event["venue"],
                            connection=connection
                        )
                 # Ensure home team exists
                home_team_id = ensure_attribute_exists(
                            cursor=cursor,
                            table="Team",
                            column="name",
                            value=new_event["home_team"],
                            connection=connection
                        )
                
                # Ensure visitor team exists in the database
                visitor_team_id = ensure_attribute_exists(
                                cursor=cursor,
                                table="Team",
                                column="name",
                                value=new_event["visitor_team"],
                                connection=connection
                            )
                
                query_event = """
                INSERT INTO Event (event_date, event_time, sport_id, venue_id, home_team_id, visitor_team_id, description)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """
                cursor.execute(query_event, (
                    new_event["date"],
                    new_event["time"],
                    sport_id,
                    venue_id,
                    home_team_id,
                    visitor_team_id,
                    new_event["description"]
                ))
                connection.commit()

                # Send success response
                self.send_response(201)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"message": "Event added successfully!"}).encode())

            except Exception as e:
                connection.rollback()
                self.send_response(500)
                self.end_headers()
                self.wfile.write(f"Error adding event: {str(e)}".encode())
            finally:
                cursor.close()
                connection.close()



def run(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Server running at http://localhost:{port}/")
    httpd.serve_forever()

if __name__ == "__main__":
    run()

