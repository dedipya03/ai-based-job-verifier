document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");
    const textarea = document.querySelector("textarea");

    form.addEventListener("submit", function (e) {
        if (textarea.value.trim() === "") {
            alert("Please enter a job description before submitting.");
            e.preventDefault();
        }
    });
});
