function sendPrompt() {
    let userInput = document.getElementById("user-input").value;
    document.getElementById("response").innerHTML = "Thinking...";

    fetch("/ask", {
        method: "POST",
        body: JSON.stringify({ prompt: userInput }),
        headers: { "Content-Type": "application/json" }
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("response").innerHTML = data.response || "Error: " + data.error;
    })
    .catch(error => {
        console.error("Error:", error);
        document.getElementById("response").innerHTML = "An error occurred.";
    });
}

function sendFeedback(feedback) {
    alert("Feedback received: " + feedback);
}
