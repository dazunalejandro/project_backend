// Fetch and display events
function fetchEvents() {
    console.log("Fetching events...");
    fetch("/api/events") // Correct GET endpoint
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json(); // Parse JSON response
        })
        .then(data => {
            const tableBody = document.getElementById("events-table");
            tableBody.innerHTML = ""; // Clear table

            // Populate table with data
            data.forEach(event => {
                const row = `
                    <tr>
                        <td>${event.event_date}</td>
                        <td>${event.event_time}</td>
                        <td>${event.sport_name}</td>
                        <td>${event.venue_name}</td>
                        <td>${event.home_team_name}</td>
                        <td>${event.visitor_team_name}</td>
                        <td>${event.description}</td>
                    </tr>
                `;
                tableBody.innerHTML += row; // Append row
            });
        })
        .catch(error => console.error("Error fetching events:", error));
}

// Handle form submission
document.getElementById("add-event-form").addEventListener("submit", function (event) {
    event.preventDefault();

    // Collect form data
    const newEvent = {
        date: document.getElementById("event-date").value,
        time: document.getElementById("event-time").value,
        sport: document.getElementById("sport").value,
        venue: document.getElementById("venue").value,
        home_team: document.getElementById("home-team").value, // Use home_team name
        visitor_team: document.getElementById("visitor-team").value, // Use visitor_team name
        description: document.getElementById("description").value
    };

    // Send the data to the backend
    fetch("/api/events", { // Ensure the correct endpoint is used
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(newEvent)
    })
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json(); // Parse JSON response
        })
        .then(message => {
            document.getElementById("add-event-form").reset(); // Reset the form after success
            fetchEvents(); // Refresh events
        })
        .catch(error => {
            console.error("Error adding event:", error);
            alert("Failed to add the event. Please try again.");
        });
});


// Load events when the page loads
document.addEventListener("DOMContentLoaded", fetchEvents);


