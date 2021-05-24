console.log('Is this page working?')
//
// async function catchAPI() {
//   const response = await fetch('https://pokeapi.co/api/v2/pokemon/');
//   console.log(response.status)
//   if(response.status === 200) {
//     let data =  await response.json()
//     console.log(data)
//     // let diva = document.getElementById('getApi');
//     // diva.innerHTML = data.name + "," + data.url
//   }
// }
// catchAPI()
const fetchData = (data) => {
    fetch('/api_project/project_list/')
// fetch('/api_project/project_update/{id}/')
        .then(res => res.json())
        .then(data =>
          // {
          //   console.log(data)
          // })
          displayProducts(data))
}


const displayProducts = (list) => {
// if (list.comleted == false){
  const diva = document.getElementById('getData');
  console.log(diva)

	const table = document.createElement("table");
  table.className = "table table-striped"
  let row = document.createElement("tr");
  let table_head = document.createElement("thead")



  diva.appendChild(table);
  table.appendChild(table_head);
  table_head.appendChild(row);
  let thead = document.createElement("th");
  let thead1 = document.createElement("th");
  let thead2 = document.createElement("th");

  row.appendChild(thead)
  row.appendChild(thead1)
  row.appendChild(thead2)
  let text = document.createTextNode(' project name ')
  let text1 = document.createTextNode(' speaker name ')
  let text2 = document.createTextNode(' time to complete ')
  thead.appendChild(text)
  thead1.appendChild(text1)
  thead2.appendChild(text2)

  let tbody = document.createElement("tbody");
  table.appendChild(tbody);

	for(i in list){

    let row1 = document.createElement("tr")
	   let tableData = document.createElement("td")
     let tableData1 = document.createElement("td")
     let tableData2 = document.createElement("td")
     let link = document.createElement("a")
     let text_link = document.createTextNode(list[i].name)
     let text_link1 = document.createTextNode(list[i].speaker)
     let text_link2 = document.createTextNode(list[i].time_to_complet)

     tbody.appendChild(row1)
     row1.appendChild(tableData)
     row1.appendChild(tableData1)
     row1.appendChild(tableData2)
     tableData.appendChild(link)
     link.appendChild(text_link)
     tableData1.appendChild(text_link1)
     tableData2.appendChild(text_link2)
     let url = '/project-detail/' + list[i].id
     // url.searchParams.set('id', )
     link.setAttribute("href", url )
     link.setAttribute("style", "color:black;")
	}
// } else {

}

  fetchData()

// let but = document.getElementById("createProject")
// console.log(but)
// let create_buttom = document.createElement("button")
// let create_project = document.createElement("a")
// let textButton = document.createTextNode(' Create project ')
// create_project.setAttribute("href", "/create_project/" )
// but.appendChild(create_buttom)
// create_buttom.appendChild(create_project)
// create_project.appendChild(textButton)
// create_project.className ="btn"


// const displayProjects = (list) =>{
//   const root = document.getElementById('getData');
//   root.innerHTML ='';
// 	for(i in list){
// 		let text = document.createElement('h2');
// 		text.innerHTML = list[i].acquried_skills
//     let text1 = document.createElement('input');
// 		text.innerHTML = list[i].speaker
//
// 		root.appendChild(text)
//     root.appendChild(text1)
// 	}
// }
// fetchCreateData()




// fetchProjectDetails()

//  TASK-CREATE
// let myDiv = document.getElementById('addTask')
// console.log(myDiv)
// const fetchTask = (data) => {
//   fetch('/todo/task_create/', {
//     method: 'POST',
//     headers: {
//       'Content-Type': 'application/json',
//     },
//     body: JSON.stringify(data),
//   })
//   .then(res => res.json())
//   .then(data1 => {
//     console.log(data1)
//   })
// }
// fetchTask()
