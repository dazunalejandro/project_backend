# Sports Events Management Application

## Overview

The Sports Events Management Application is a web-based system designed to manage and organize sports events. It provides features for managing events, teams, venues, and sports. The application is built with a Python backend, MySQL for database management, and a user-friendly frontend for interaction.

### Key Features:

- Create, update, and view sports events.
- Manage sports, teams, and venues dynamically.
- Responsive web interface for users.
- Backend API for handling data operations and integration.

## Setup Instructions

### Prerequisites

Ensure the following software is installed on your system:

1. Python 3.8 or higher
2. MySQL Server

#### Backend Setup

1. **Clone the Repository**:

   ```bash
   git clone <repository-url>
   cd backend
   ```
2. **Start the Backend Server**:

   ```bash
   python server_app.py
   ```

   This will create the database schema and seed initial data if necessary. The server will run on `http://localhost:8000` by default.

   - MySQL database `sport_events` is created using `tools\db_setup`
   - Support functions for `server_app.py ` are included in `server_support.py`.

## Assumptions and Decisions

1. **Database Initialization**:

   - The application checks if the database `sport_events` exists before running setup scripts. If the database exists, setup scripts are skipped.

2. **Event Model Design**:

   - Each event is associated with a sport, venue, home team, and visitor team.
   - Event dates are stored in `YYYY-MM-DD` format, and times are stored in `HH:MM:SS` format.

3. **Dynamic Data Handling**:

   - Sports, venues, and teams are dynamically created in the database if they do not already exist during event creation.

4. **Error Handling**:

   - The application handles errors such as missing database connections or invalid input data.

## Folder Structure

```
backend/
  server_app.py       # Main application entry point
  server_support.py   # Support functions for database and API
  tools/              # database set up
      db_setup.py            
frontend/
  css/
      style.css                
  js/
     app.js
  index.html                 
database/
  erd.png             # ERD 
  schema.sql          # Database schema definition
  seed.sql            # Initial data for seeding the database
```

