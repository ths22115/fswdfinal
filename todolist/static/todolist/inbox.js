document.addEventListener("DOMContentLoaded", function () {

  document
    .querySelector("#list")
    .addEventListener("click", () => load_page("list"));
  document
    .querySelector("#done")
    .addEventListener("click", () => load_page("done"));
  document.querySelector("#create").addEventListener("create", create_task);


  document
    .querySelector("#create-form")
    .addEventListener("submit", add_task_to_list);


  load_page("list");
});

function add_task_to_list(event) {

  event.preventDefault();


  const job = document.querySelector("#create-job").value;
  const category = document.querySelector("#create-category").value;
  const repeat = document.querySelector("#create-repeat").value;


  fetch("/tasks", {
    method: "POST",
    body: JSON.stringify({
      job: job,
      category: category,
      repeat: repeat,
    }),
  })

    .then((response) => response.json())
    .then((result) => {
      load_page("list", result);
    })
    .catch((error) => console.log(error));
}

function create_task() {
  document.querySelector("#list-view").style.display = "none";
  document.querySelector("#create-view").style.display = "block";


  document.querySelector("#create-job").value = "";
  document.querySelector("#create-category").value = "";
  document.querySelector("#create-repeat").value = "";
}

function load_page(page, message = "") {

  document.querySelector("#message-div").textContent = "";
  if (message !== "") {
    make_alert(message);
  }

  document.querySelector("#list-view").style.display = "block";
  document.querySelector("#create-view").style.display = "none";

  document.querySelector("#list-view").innerHTML = `<h3>${page.charAt(0).toUpperCase() + page.slice(1)
    }</h3>`;

  fetch(`/tasks/${page}`)
    .then((response) => response.json())
    .then((tasks) => {
      tasks.forEach((item) => {

        const parent_element = document.createElement("div");

        build_tasks(item, parent_element, page);

        document.querySelector("#list-view").appendChild(parent_element);

      });
    })
    .catch((error) => console.error(error));
}

function make_alert(message) {
  const element = document.createElement("div");
  element.classList.add("alert");

  if (message["message"]) {
    element.classList.add("alert-success");
    element.innerHTML = message["message"];
  } else if (message["error"]) {
    element.classList.add("alert-danger");
    element.innerHTML = message["error"];
  }

  document.querySelector("#message-div").appendChild(element);
}

function build_tasks(item, parent_element, page) {
//  const job = document.createElement("div");
//  const category = document.createElement("div");
//  const repeat = document.createElement("div");
//  const done = document.createElement("div");

  const content = document.createElement("div");

  content.innerHTML += item["job"];
  content.innerHTML += item["category"];
  content.innerHTML += item["repeat"];
  content.innerHTML += item["done"];

  if (item["done"]) {
    parent_element.style.backgroundColor = "grey";
  }
  content.style.padding = "10px";
  parent_element.appendChild(content);

  parent_element.style.borderStyle = "solid";
  parent_element.style.borderWidth = "3px";
  parent_element.style.margin = "10px";
}

function build_email(data) {
  const job = document.createElement("div");
  const category = document.createElement("div");
  const repeat = document.createElement("div");
  const done = document.createElement("div");

  job.innerHTML = `<strong>Task: </strong> ${data["job"]}`;
  category.innerHTML = `<strong>Category: </strong> ${data["category"]}`;
  repeat.innerHTML = `<strong>Repeats </strong> ${data["repeat"]}`;
 done.innerHTML = `<strong>Done: </strong> ${data["done"]}`;


  done_button.innerHTML = '<svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-archive-fill" fill="currentColor" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M12.643 15C13.979 15 15 13.845 15 12.5V5H1v7.5C1 13.845 2.021 15 3.357 15h9.286zM5.5 7a.5.5 0 0 0 0 1h5a.5.5 0 0 0 0-1h-5zM.8 1a.8.8 0 0 0-.8.8V3a.8.8 0 0 0 .8.8h14.4A.8.8 0 0 0 16 3V1.8a.8.8 0 0 0-.8-.8H.8z"/></svg>  ';
  if (data["done"]) {
    done_button.innerHTML += "Undone";
  } else {
    done_button.innerHTML += "Done";
  }
  done_button.classList = "btn btn-outline-primary m-2";
  done_button.addEventListener("click", () => {
    load_mailbox("list");
  });
  }
