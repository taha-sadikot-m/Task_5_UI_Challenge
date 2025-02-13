




window.addEventListener('load', function () {
    document.getElementById('show').addEventListener('click', function (event) {

        (async function connectToAPI() {
            try {
                const response = await fetch('/show', {
                    method: 'GET',
                });

                const result = await response.json();

                if (response.ok) {
                   
                    alert("SUCCESS");
                } else {
                    
                    alert("ERROR");
                }
            } catch (error) {
                
                alert("ERROR");
            }
        })(); 
    });
});


















setupEventListeners();
function setupEventListeners() {
    const submitButton = document.getElementById('submit');
    
    if (submitButton) {
        submitButton.addEventListener('click', function (event) {
            event.preventDefault(); // Prevent default form submission if inside a form
            
            const ip = document.getElementById('ip').value;
            const username = document.getElementById('username').value;
            const port = document.getElementById('port').value;
            const password = document.getElementById('password').value;
            const nodes = document.getElementById('nodes').value;

            const data = { ip, username, port, password, nodes };

            document.getElementById('status').innerText = 'Connecting...';

            (async function connectToAPI() {
                try {
                    const response = await fetch('/setup', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify(data),
                    });

                    const result = await response.json();

                    if (response.ok) {
                        document.getElementById('status').innerText = 'Connected';
                    } else {
                        document.getElementById('status').innerText = 'Failed to Connect';
                    }
                } catch (error) {
                    document.getElementById('status').innerText = 'Error occurred';
                }
            })(); 
        });
    }
}






    initMultiStepForm();
    function initMultiStepForm() {
        let currentpage = 1;
        const prev = document.querySelector('.prev');
        const next = document.querySelector('.next');
        const steps = document.querySelectorAll('.multi-step-form .form-step');
        const stepNodes = document.querySelectorAll('.multi-step .step');

        function movepage() {
            // Enable or disable buttons
            prev.disabled = currentpage === 1;
            next.disabled = currentpage === steps.length;

            // Remove active class from the current form step and step node
            document.querySelector('.multi-step-form .form-step.active')?.classList.remove('active');
            document.querySelector('.multi-step     .step.active')?.classList.remove('active');

            // Add active class to the current form step and step node
            steps[currentpage - 1]?.classList.add('active');
            stepNodes[currentpage - 1]?.classList.add('active');
        }

        prev.addEventListener('click', function () {
            if (currentpage > 1) {
                currentpage -= 1;
                movepage();
            }
        });

        next.addEventListener('click', function () {
            if (currentpage < steps.length) {
                currentpage += 1;
                movepage();
            }
        });

        // Initialize first step and step node as active
        steps[0].classList.add('active');
        stepNodes[0].classList.add('active');
    };

