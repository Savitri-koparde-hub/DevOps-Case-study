from flask import Flask, send_from_directory

app = Flask(__name__)

# Serve files (like image)
@app.route('/<path:filename>')
def serve_file(filename):
    return send_from_directory('.', filename)

@app.route('/')
def home():
    return """
    <html>
    <head>
        <title>Savitri Koparde</title>
        <style>
            body {
                margin: 0;
                font-family: Arial;
                display: flex;
                height: 100vh;
            }

            .left {
                width: 50%;
                background: #f4f4f4;
                padding: 60px;
            }

            .right {
                width: 50%;
                background: black;
                display: flex;
                justify-content: center;
                align-items: center;
            }

            .right img {
                width: 300px;
                border-radius: 10px;
            }

            .nav {
                position: absolute;
                top: 20px;
                right: 50px;
            }

            .nav button {
                margin: 5px;
                padding: 10px;
                cursor: pointer;
                border: none;
                background: white;
                border-radius: 5px;
            }

            .section {
                display: none;
                margin-top: 30px;
            }

            .active {
                display: block;
            }

            h1 {
                font-size: 40px;
            }
        </style>

        <script>
            function showSection(id) {
                document.getElementById('about').style.display = 'none';
                document.getElementById('skills').style.display = 'none';
                document.getElementById('contact').style.display = 'none';

                document.getElementById(id).style.display = 'block';
            }
        </script>
    </head>

    <body>

        <div class="nav">
            <button onclick="showSection('about')">About</button>
            <button onclick="showSection('skills')">Skills</button>
            <button onclick="showSection('contact')">Contact</button>
        </div>

        <div class="left">
            <h3>Hi, I am</h3>
            <h1>Savitri Koparde</h1>
            <p><b>Aspiring DevOps Intern at FinacPlus</b></p>

            <div id="about" class="section active">
                <h2>About Me</h2>
                <p>I am passionate about DevOps, cloud computing, and automation. I enjoy working with Docker, Kubernetes, and CI/CD pipelines.</p>
            </div>

            <div id="skills" class="section">
                <h2>Skills</h2>
                <ul>
                    <li>Docker</li>
                    <li>Kubernetes</li>
                    <li>Jenkins</li>
                    <li>Git & GitHub</li>
                    <li>Python</li>
                </ul>
            </div>

            <div id="contact" class="section">
                <h2>Contact</h2>
                <p>Email: savitrikoparde612@email.com</p>
                <p>
                    LinkedIn: 
                    <a href="https://www.linkedin.com/in/savitri-koparde-7b0b8221a" target="_blank">
                        linkedin.com/in/savitri-koparde
                    </a>
                </p>
            </div>
        </div>

        <div class="right">
            <img src="/profile.jpeg" />
        </div>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)