const form = document.getElementById("task-form");
const input = document.getElementById("task-input");
const list = document.getElementById("task-list");

form.addEventListener("submit", (event) => {
    event.preventDefault();
    if (input.value.trim()) {
        const task = document.createElement("li");
        task.innerHTML = `
            ${input.value.trim()}
            <button class="delete-btn">Delete</button>
        `;
        list.appendChild(task);
        input.value = "";
    }
});

list.addEventListener("click", (event) => {
    if (event.target.classList.contains("delete-btn")) {
        event.target.parentNode.remove();
    }
});