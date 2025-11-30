loginScreen = document.createElement("div");
loginScreen.innerHTML = `
    <input type="text" id="userLogin"> <br>
    <input type="password" name="userPass" id="userPass"> <br><br>
    <input type="button" value="Login" onclick="UserSubmit()"> <br>
    <textarea name="Console" id="userMessage"></textarea>
`;
document.body.append(loginScreen);
function UserSubmit() {
    fetch("base.json")
    .then(Response => Response.json())
    .then(data => {
        typeLogin = document.getElementById("userLogin").value;
        typePass = document.getElementById("userPass").value;
        sendMessage = document.getElementById("userMessage");
        logined = false;
        data.forEach(user => {
            if (typeLogin == user.login) {
                if (typePass == user.password) {
                    logined = true;
                    loginScreen.style = "display: none;";
                    userScreen = document.createElement("div");
                    userScreen.innerHTML = `
                        <h1>Hello Mr.${user.login}</h1>
                        <p>Your point: ${user.point}</p>
                    `;
                    document.body.append(userScreen);
                    sendMessage.value = `Hello Mr.${user.login}`;
                }
            }
            if (!logined) {
                sendMessage.value = "Wrong login or password! Please try again"
            }
        });

    })
}