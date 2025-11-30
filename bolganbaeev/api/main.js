div = document.createElement("div")
fetch("http://0.0.0.0:8000/users")
.then(Response => Response.json())
.then(u => {
    u.forEach(u => {
        div.innerHTML += `${u.name} ${u.age} y.o. ${u.sex} <br>`
    });
})
document.body.append(div);
