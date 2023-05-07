function showInfo(event) {
  if (event == null || event.currentTarget == null) return;
  event.currentTarget.querySelector(".poem").style.display = "none";
  event.currentTarget.querySelector(".info").style.display = "block";
  event.currentTarget.style.border = "2px solid black";
}

function hideInfo(event) {
  if (event == null || event.currentTarget == null) return;
  event.currentTarget.querySelector(".info").style.display = "none";
  event.currentTarget.querySelector(".poem").style.display = "block";
  event.currentTarget.style.border = "0px solid black";
}

document.addEventListener("DOMContentLoaded", function () {
  const poemContainers = document.querySelectorAll(".poem-container");

  poemContainers.forEach((container) => {
    container.addEventListener("mouseover", showInfo);
    container.addEventListener("mouseout", hideInfo);
  });
});
