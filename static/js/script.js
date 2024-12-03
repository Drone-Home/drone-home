document.addEventListener('DOMContentLoaded', function () {
    const leftButton = document.getElementById('left-btn');
    const rightButton = document.getElementById('right-btn');
    const lever = document.getElementById('lever');
    const leverContainer = document.querySelector('.lever-container');
    const statusDisplay = document.getElementById('lever-status');

    // Set the initial lever position to "Neutral"
    const containerHeight = leverContainer.offsetHeight;
    const leverHeight = lever.offsetHeight;
    const neutralPosition = (containerHeight - leverHeight) / 2;

    lever.style.bottom = `${neutralPosition}px`;
    statusDisplay.textContent = "Neutral";

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
    
        // Lever dragging logic
        let isDragging = false;

    // Function to send actions to the server
    function sendActionToServer(action) {
        fetch('/control', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ action: action }),
        })
            .then(response => response.json())
            .then(data => {
                console.log('Server response:', data);
            })
            .catch(error => {
                console.error('Error sending action to server:', error);
            });
    }

    // Function to adjust lever position
    function adjustLeverPosition(direction) {
        const containerRect = leverContainer.getBoundingClientRect();
        const leverHeight = lever.offsetHeight;
        let currentPosition = parseInt(lever.style.bottom) || 0;

        if (direction === 'up') {
            currentPosition = Math.min(containerRect.height - leverHeight, currentPosition + 20);
            sendActionToServer('accelerate');
        } else if (direction === 'down') {
            currentPosition = Math.max(0, currentPosition - 20);
            sendActionToServer('decelerate');
        }

        lever.style.bottom = `${currentPosition}px`;
        updateLeverStatus(currentPosition, containerRect.height - leverHeight);
    }

    // Keydown and keyup event listeners
    document.addEventListener('keydown', function (event) {
        if (!isDragging) {
            switch (event.key) {
                case 'ArrowLeft':
                    leftButton.classList.add('clicked');
                    sendActionToServer('left');
                    break;
                case 'ArrowRight':
                    rightButton.classList.add('clicked');
                    sendActionToServer('right');
                    break;
                case 'ArrowUp':
                    adjustLeverPosition('up');
                    break;
                case 'ArrowDown':
                    adjustLeverPosition('down');
                    break;
            }
        };
    });

    document.addEventListener('keyup', function (event) {
        switch (event.key) {
            case 'ArrowLeft':
                leftButton.classList.remove('clicked');
                break;
            case 'ArrowRight':
                rightButton.classList.remove('clicked');
                break;
        }
    });

    // Lever dragging logic
    lever.addEventListener('mousedown', function () {
        isDragging = true;
    });

    document.addEventListener('mousemove', function (event) {
        if (isDragging) {
            const containerRect = leverContainer.getBoundingClientRect();
            const leverHeight = lever.offsetHeight;

            let newY = event.clientY - containerRect.top - leverHeight / 2;

            if (newY < 0) newY = 0;
            if (newY > containerRect.height - leverHeight) newY = containerRect.height - leverHeight;

            lever.style.bottom = `${containerRect.height - newY - leverHeight}px`;

            const positionPercentage = ((containerRect.height - newY - leverHeight) / (containerRect.height - leverHeight)) * 100;
            updateLeverStatus(containerRect.height - newY - leverHeight, containerRect.height - leverHeight);
        }
    });

    document.addEventListener('mouseup', function () {
        isDragging = false;
    });
});