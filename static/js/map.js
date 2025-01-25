document.addEventListener('DOMContentLoaded', function () {
    // Initialize the map
    const map = L.map('map').setView([0, 0], 15); // Default center (to be updated)

    // Add a satellite tile layer
    L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
        attribution: '© Esri, Maxar, Earthstar Geographics, and the GIS User Community'
    }).addTo(map);

    // Function to add a marker for a given location
    function addMarker(lat, lon, popupText) {
        L.marker([lat, lon]).addTo(map).bindPopup(popupText);
    }

    // Get the user's current location (Computer GPS)
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
            function (position) {
                const lat = position.coords.latitude;
                const lon = position.coords.longitude;

                // Center the map on the user's location
                map.setView([lat, lon], 15);

                // Set computer GPS dynamically
                const computerGPS = { lat, lon };
                addMarker(computerGPS.lat, computerGPS.lon, "Computer GPS");

                // Define fixed offsets for Drone and R/C Car
                const droneGPS = { lat: 29.655748701497817, lon: -82.33801363758273 }; // 50m from Computer GPS
                const carGPS = { lat: 29.656, lon: -82.337 };   // 125m from Computer GPS

                // Add markers for Drone & R/C Car
                addMarker(droneGPS.lat, droneGPS.lon, "Drone GPS");
                addMarker(carGPS.lat, carGPS.lon, "R/C Car GPS");

                // Send GPS data to script.js
                window.dispatchEvent(new CustomEvent("gpsLocationUpdate", {
                    detail: { computer_gps: computerGPS, drone_gps: droneGPS, car_gps: carGPS }
                }));
            },
            function (error) {
                console.error("Geolocation error: ", error);
                alert("Unable to fetch your location.");
            }
        );
    } else {
        alert("Geolocation is not supported by your browser.");
    }
});