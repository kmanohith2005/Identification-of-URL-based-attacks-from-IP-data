function checkURL() {
    const urlInput = document.getElementById("url").value;
    const output = document.getElementById("output");

    if (urlInput.trim() === "") {
        output.innerHTML = "Please enter a URL";
        output.className = "";
        return;
    }

    output.innerHTML = "Checking URL...";
    output.className = "";

    fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ url: urlInput })
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === "Safe") {
            output.innerHTML =
                "Status: SAFE<br>Attack Type: " + data.attack_type;
            output.className = "safe";
        } else {
            output.innerHTML =
                "Status: MALICIOUS<br>Attack Type: " + data.attack_type;
            output.className = "malicious";
        }
    })
    .catch(error => {
        output.innerHTML = "Error connecting to server";
        output.className = "";
        console.error(error);
    });
}
