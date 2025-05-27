from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        age = request.form.get("age")
        
        return f"""
            <div style='font-family: Arial; padding: 30px; max-width: 500px; margin: auto;'>
                <h2>Submission Received!</h2>
                <p><strong>Name:</strong> {name}</p>
                <p><strong>Email:</strong> {email}</p>
                <p><strong>Age:</strong> {age}</p>
                <br><a href="/" style="color: #007BFF; text-decoration: none;">Go Back</a>
            </div>
        """
    
    return render_template_string('''
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f0f2f5;
                padding: 40px;
            }
            .form-container {
                background-color: white;
                padding: 30px;
                border-radius: 10px;
                max-width: 500px;
                margin: auto;
                box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
            }
            input[type="text"],
            input[type="email"],
            input[type="number"] {
                width: 100%;
                padding: 10px;
                margin-top: 8px;
                margin-bottom: 16px;
                border: 1px solid #ccc;
                border-radius: 5px;
            }
            input[type="submit"] {
                background-color: #007BFF;
                color: white;
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            }
            input[type="submit"]:hover {
                background-color: #0056b3;
            }
        </style>

        <div class="form-container">
            <h2>Simple Info Form</h2>
            <form method="POST">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required>

                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>

                <label for="age">Age:</label>
                <input type="number" id="age" name="age" required>

                <input type="submit" value="Submit">
            </form>
        </div>
    ''')

if __name__ == "__main__":
    app.run(debug=True)