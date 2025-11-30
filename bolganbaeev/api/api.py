
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class SimpleAPI(BaseHTTPRequestHandler):
    def save_users(self, users):
        with open("users.json", "w") as f:
            json.dump(users, f, indent=4)
    def send_json(self, data, status=200):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        if data is not None:
            self.wfile.write(json.dumps(data).encode())
    def load_users(self):
        with open("users.json", "r") as f:
            return json.load(f)
    def do_GET(self):
        users_data = self.load_users()
        if self.path == "/users":
            self.send_json(users_data)
        elif self.path.startswith("/users/"):
            try:
                user_id=int(self.path.split("/")[-1])
                user = next((u for u in users_data if u["id"] == user_id), None)
                if user:
                    self.send_json(user)
                else:
                    self.send_response(404)
                    self.end_headers()
            except:
                self.send_response(400)
                self.end_headers()
        
        else:
            self.send_response(404)
            self.end_headers()
    def do_POST(self):
        users = self.load_users()  # users.json ішінен оқу

        if self.path == "/users":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data)

            # 🟢 ең кішкентай бос ID табу
            existing_ids = [u["id"] for u in users]
            new_id = 1
            while new_id in existing_ids:
                new_id += 1
            data["id"] = new_id

            users.append(data)

            self.save_users(users)  # users.json қайта жазу

            self.send_response(201)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode())

        else:
            self.send_json({"error": "Not found"}, 404)

    def do_DELETE(self):
        users_data = self.load_users()
        if self.path.startswith("/users/"):
            try:
                user_id = int(self.path.split("/")[-1])
                new_users = [u for u in users_data if u ["id"] != user_id]

                if len(new_users) == len(users_data):
                    self.send_json({"error": "User not found"}, 404)
                else:
                    self.save_users(new_users)
                    self.send_json({"message": "User deleted"}, 200)

            except:
                self.send_json({"error": "Invalid ID"}, 400)
        else:
            self.send_json({"error": "Not found"}, 404)
                    

        



server = HTTPServer(("0.0.0.0", 8000), SimpleAPI)
print("Server running http://0.0.0.0:8000")
server.serve_forever()
