document.addEventListener("DOMContentLoaded", function () {
    const updateHeaderButton = document.getElementById("update_header");
    const headerElement = document.querySelector("header");
  
    updateHeaderButton.addEventListener("click", function () {
      headerElement.textContent = "New Header!!!";
    });
  });