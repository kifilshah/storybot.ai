function sendMessage() {
    const userInput = document.getElementById("userInput");
    const chatHistory = document.getElementById("chatHistory");

    // Add the user's message to the chat history
    chatHistory.innerHTML += "You: " + userInput.value + "<br />";
    userInput.value = "";

    // Show loader
    const loader = document.getElementById("loader");
    loader.classList.remove("d-none");

    // Make API call
    fetch("/ask", {
        method: "POST",
        body: new URLSearchParams({ message: userInput.value }),
    })
        .then((response) => response.json())
        .then((data) => {
            chatHistory.innerHTML += "Bot: " + data.response + "<br />";
        })
        .catch((error) => {
            chatHistory.innerHTML += "Bot: Error" + "<br />";
            console.error(error);
        })
        .finally(() => {
            // Hide loader
            loader.classList.add("d-none");
        });
}