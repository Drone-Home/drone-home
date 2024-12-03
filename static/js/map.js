document.addEventListener('DOMContentLoaded', function () {
    // Initialize the map
    const map = L.map('map').setView([0, 0], 2); // Default center (to be updated)

    // Add a satellite tile layer (e.g., Mapbox or ESRI)
    L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
        attribution: '© Esri, Maxar, Earthstar Geographics, and the GIS User Community'
    }).addTo(map);

    // Function to add a marker for a given location
    function addMarker(lat, lon, popupText) {
        L.marker([lat, lon]).addTo(map).bindPopup(popupText).openPopup();
    }

    // Get the user's current location
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
            function (position) {
                const lat = position.coords.latitude;
                const lon = position.coords.longitude;

                // Center the map on the user's location
                map.setView([lat, lon], 15);

                // Add a marker for the user's current location
                addMarker(lat, lon, "Host Location");
            },
            function (error) {
                console.error("Geolocation error: ", error);
                alert("Unable to fetch your location.");
            }
        );
    } else {
        alert("Geolocation is not supported by your browser.");
    }

    // Example: Add another object's location
    // Replace these coordinates with your object's actual location
    const objectLat = 37.7749; // Example latitude
    const objectLon = -122.4194; // Example longitude
    addMarker(objectLat, objectLon, "Tracked Object's Location");
});