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

            if (newY < 0) newY = 0;
            if (newY > containerRect.height - leverHeight) newY = containerRect.height - leverHeight;

            lever.style.bottom = (containerRect.height - newY - leverHeight) + 'px';

            let positionPercentage = ((containerRect.height - newY - leverHeight) / (containerRect.height - leverHeight)) * 100;
            updateLeverStatus(containerRect.height - newY - leverHeight, containerRect.height - leverHeight);
        }
    });

    document.addEventListener('mouseup', function() {
        isDragging = false;
    });

    // Keydown and keyup events for continuous left and right button press
    document.addEventListener('keydown', function(event) {
        if (!isDragging) {  // Ensure dragging takes priority over key events
            switch(event.key) {
                case 'ArrowLeft':
                    if (!leftKeyHeld) {
                        leftButton.classList.add('clicked');
                        leftKeyHeld = true;
                        console.log("Left command sent");
                    }
                    break;
                case 'ArrowRight':
                    if (!rightKeyHeld) {
                        rightButton.classList.add('clicked');
                        rightKeyHeld = true;
                        console.log("Right command sent");
                    }
                    break;
                case 'ArrowUp':
                    adjustLeverPosition('up');
                    console.log("Accelerate command sent");
                    break;
                case 'ArrowDown':
                    adjustLeverPosition('down');
                    console.log("Decelerate command sent");
                    break;
            }
        }
    });

    document.addEventListener('keyup', function(event) {
        switch(event.key) {
            case 'ArrowLeft':
                leftButton.classList.remove('clicked');
                leftKeyHeld = false;
                break;
            case 'ArrowRight':
                rightButton.classList.remove('clicked');
                rightKeyHeld = false;
                break;
        }
    });
});
