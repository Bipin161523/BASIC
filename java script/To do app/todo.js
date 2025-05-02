const input = document.getElementById("todoInput");
const addButton = document.getElementById("addBtn");
const todoList = document.getElementById("todoList");

addButton.addEventListener("click", () => {
  const taskText = input.value.trim();

  if (taskText !== "") {
    const li = document.createElement("li");
    li.textContent = taskText;

    // Add delete button
    const delBtn = document.createElement("button");
    delBtn.textContent = "❌";
    delBtn.style.marginLeft = "10px";
    delBtn.onclick = () => li.remove();

    li.appendChild(delBtn);
    todoList.appendChild(li);

    input.value = ""; // Clear input after adding
  }
});



