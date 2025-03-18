// function for ingecting url content
function ingestData() {
    const urls = document.getElementById("urls").value.split('\n').map(url => url.trim()).filter(url => url);
    
    if (urls.length === 0) {
        alert("Please enter at least one valid URL.");
        return;
    }
    alert("Please Wait.....");
    fetch("/ingest", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ urls })
    })
    .then(response => response.json())
    .then(data => {
        showMessage("Data ingested successfully!", "bot-message");
        document.getElementById("urls").value = "";

        let modalElement = document.getElementById('ingestModal');
        let modalInstance = bootstrap.Modal.getInstance(modalElement);
        modalInstance.hide();
    })
    .catch(error => console.error("Error:", error));
}

// upon adding data succesfully message generated on the chat section - data inserted succesfully
function showMessage(text, className) {
    const chatBox = document.getElementById("chat-box");
    const message = document.createElement("div");
    message.className = `message ${className}`;
    message.textContent = text;
    chatBox.appendChild(message);
    chatBox.scrollTop = chatBox.scrollHeight;
}

// function for asking question 
function askQuestion() {
    const query = document.getElementById("query").value.trim();
    if (!query) return;
    
    const chatBox = document.getElementById("chat-box");
    const userMessage = document.createElement("div");
    userMessage.className = "message user-message";
    userMessage.textContent = query;
    chatBox.appendChild(userMessage);

    fetch("/ask", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ query })
    })
    .then(response => response.json())
    .then(data => {
        const botMessage = document.createElement("div");
        botMessage.className = "message bot-message";
        botMessage.textContent = data.answer || "Error fetching response.";
        chatBox.appendChild(botMessage);
        chatBox.scrollTop = chatBox.scrollHeight;
    })
    .catch(error => console.error("Error:", error));
    
    document.getElementById("query").value = "";
}
