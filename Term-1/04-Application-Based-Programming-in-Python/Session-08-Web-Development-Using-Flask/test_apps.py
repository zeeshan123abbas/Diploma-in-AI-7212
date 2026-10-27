# test_apps.py
# Test the Flask apps WITHOUT starting a server, using Flask's test client.
from app_routes import app as routes_app
from app_templates import app as templates_app

client = routes_app.test_client()
print(client.get("/hello/ali").get_data(as_text=True))
print(client.get("/square/7").get_data(as_text=True))
print(client.get("/api/courses").get_json())

client = templates_app.test_client()
page = client.get("/").get_data(as_text=True)
print("Student list page contains 'Sara'?", "Sara" in page)
response = client.post("/add", data={"name": "Hina", "marks": "88"})
print("After POST:", "Hina added successfully." in response.get_data(as_text=True))
