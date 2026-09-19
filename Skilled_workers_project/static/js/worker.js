document.addEventListener("DOMContentLoaded", function() {
    let popup = document.getElementById("popup");
    if (popup) {
        popup.classList.add("show");
        setTimeout(() => {
            popup.classList.remove("show");
        }, 3000); // hide after 3 seconds
    }
});