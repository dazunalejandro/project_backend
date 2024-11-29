from datetime import timedelta

def format_event_dates_and_times(events):
    """
    Converts the event_date to a string format (YYYY-MM-DD) and formats event_time to HH:MM:SS.

    Args:
        events (list): A list of dictionaries where each dictionary represents an event.

    Returns:
        list: The same list of events with formatted event_date and event_time.
    """
    for event in events:
        # Convert event_date to string (YYYY-MM-DD)
        if 'event_date' in event and hasattr(event['event_date'], 'strftime'):
            event['event_date'] = event['event_date'].strftime('%Y-%m-%d')
        
        # Handle event_time formatting
        if 'event_time' in event:
            if isinstance(event['event_time'], timedelta):
                total_seconds = event['event_time'].total_seconds()
                hours = int(total_seconds // 3600)
                minutes = int((total_seconds % 3600) // 60)
                seconds = int(total_seconds % 60)
                event['event_time'] = f"{hours:02}:{minutes:02}:{seconds:02}"  # Format as HH:MM:SS
            else:
                event['event_time'] = str(event['event_time'])  # Fallback if it's not a timedelta

    return events


def ensure_attribute_exists(cursor, table, column, value, connection=None):
    """
    Ensures that a specific attribute exists in the database. If it doesn't, it inserts the value
    and returns the corresponding ID.

    Args:
        cursor (object): The database cursor for executing queries.
        table (str): The name of the table to check and insert into.
        column (str): The column name to check for the value.
        value (str): The value to check and insert if it doesn't exist.
        connection (object, optional): The database connection object for committing changes. Default is None.

    Returns:
        int: The ID of the existing or newly inserted row.
    """
    # Check if the value exists in the table
    query = f"SELECT {table}_id FROM {table} WHERE {column} = %s"
    cursor.execute(query, (value,))
    result = cursor.fetchone()

    # If it doesn't exist, insert the value
    if not result:
        insert_query = f"INSERT INTO {table} ({column}) VALUES (%s)"
        cursor.execute(insert_query, (value,))
        if connection:
            connection.commit()  # Commit the transaction if connection is provided
        return cursor.lastrowid  # Return the ID of the newly inserted row
    else:
        return result[0]  # Return the ID of the existing row
