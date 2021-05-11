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
    // fetch('https://jsonplaceholder.typicode.com/users')
    fetch('http://127.0.0.1:8000/project-list/')
        .then(res => res.json())
        .then(data => displayProducts(data))
}

const displayProducts = (list) => {
	const root = document.getElementById('getApi');
	root.innerHTML ='';
	for(i in list){
		let text = document.createElement('h2');
		text.innerHTML = list[i].name

		root.appendChild(text)
	}
}
  fetchData()








//   .then(res =>
//     if(res.ok) {
//       console.log('SUCCESS')
//     } else {
//       console.log("Not successful")
//     }
//     res.json())
//   .then(data => console.log(data))
//   .catch(err => console.log('ERROR'))
