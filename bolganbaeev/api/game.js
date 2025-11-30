screen = document.createElement("div");
player_1 = document.createElement("div");
screen.classList.add("screen");
player_1.classList.add("player");
screen.append(player_1);
remote = document.createElement("div");
remote.classList.add("remote")
up = document.createElement("div")
up.classList.add("rem")
up.style = "margin: 0 0px; background: black"
left = document.createElement("div")
left.classList.add("rem")
down = document.createElement("div")
down.classList.add("rem")
right = document.createElement("div")
right.classList.add("rem")
remote.append(up, left, down, right)
document.body.append(screen, remote);