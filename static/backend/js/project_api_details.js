const fetchProjectDetails = (data) => {
  fetch('/api_project/project_detail/')
  .then(res => res.json())
  .then(data => {
    console.log(data)
  })
    // displayProjectDetails())
}


const displayProjectDetails = (list) => {
  const div = document.getElementById("project_detail")
  console.log(div)
}

fetchProjectDetails(id)
