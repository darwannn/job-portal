document
  .querySelector("#dropdownIcon")
  .addEventListener("click", function (event) {
    event.preventDefault();
    document.querySelector("#dropdownContent").classList.toggle("hidden");
  });
document
  .querySelector("#notifIcon")
  .addEventListener("click", function (event) {
    event.preventDefault();
    document.querySelector("#notifContent").classList.toggle("hidden");
  });

window.addEventListener("click", function (event) {
  if (
    !document.querySelector("#notifContent").contains(event.target) &&
    !document.querySelector("#notifIcon").contains(event.target)
  ) {
    document.querySelector("#notifContent").classList.add("hidden");
  }
  if (
    !document.querySelector("#dropdownIcon").contains(event.target) &&
    !document.querySelector("#dropdownContent").contains(event.target)
  ) {
    document.querySelector("#dropdownContent").classList.add("hidden");
  }
});
