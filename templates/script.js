document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("rag-form");
    const inputText = document.getElementById("input-text");
    const outputDiv = document.getElementById("output");

    form.addEventListener("submit", function(event) {
        event.preventDefault();

        // Get the input text from the form
        const query = inputText.value.trim();

        // Make the API call to your backend
        fetch("/api/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ query: query })
        })
        .then(response => {
            if (!response.ok) {
                throw new Error("Network response was not ok");
            }
            return response.json();
        })
        .then(data => {
            // Display the response in the output div
            outputDiv.textContent = data.response;
        })
        .catch(error => {
            console.error("There was a problem with the fetch operation:", error);
            outputDiv.textContent = "An error occurred. Please try again later.";
        });
    });
});

