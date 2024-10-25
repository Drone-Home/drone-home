document.addEventListener('DOMContentLoaded', function() {
    const leftButton = document.getElementById('left-btn');
    const rightButton = document.getElementById('right-btn');
    const lever = document.getElementById('lever');
    const leverContainer = document.querySelector('.lever-container');
    const statusDisplay = document.getElementById('lever-status');

    let isDragging = false;
    let leftKeyHeld = false;
    let rightKeyHeld = false;

    // Function to update lever status based on position
    function updateLeverStatus(currentPosition, maxHeight) {
        let positionPercentage = (currentPosition / maxHeight) * 100;
        if (positionPercentage > 60) {
            statusDisplay.textContent = "Accelerating";
        } else if (positionPercentage < 40) {
            statusDisplay.textContent = "Decelerating";
        } else {
            statusDisplay.textContent = "Neutral";
        }
    }

    // Adjust lever position for acceleration and deceleration
    function adjustLeverPosition(direction) {
        let containerRect = leverContainer.getBoundingClientRect();
        let leverHeight = lever.offsetHeight;
        let currentPosition = parseInt(lever.style.bottom) || 0;

        if (direction === 'up') {
            currentPosition = Math.min(containerRect.height - leverHeight, currentPosition + 20);
        } else if (direction === 'down') {
            currentPosition = Math.max(0, currentPosition - 20);
        }

        lever.style.bottom = currentPosition + 'px';
        updateLeverStatus(currentPosition, containerRect.height - leverHeight);
    }

    // Lever dragging logic
    lever.addEventListener('mousedown', function(event) {
        isDragging = true;
    });

    document.addEventListener('mousemove', function(event) {
        if (isDragging) {
            let containerRect = leverContainer.getBoundingClientRect();
            let leverHeight = lever.offsetHeight;

            let newY = event.clientY - containerRect.top - leverHeight / 2;

            if (newY < 0)