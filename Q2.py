from flask import Flask
import datetime
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Get system info
    top_output = subprocess.check_output(["top", "-b", "-n", "1"]).decode("utf-8")
    username = subprocess.check_output(["whoami"]).decode().strip()
    ist_time = datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=30)

    # Simplify output
    return f"""
    Name: Your Full Name<br>
    Username: {username}<br>
    Server Time (IST): {ist_time.strftime('%Y-%m-%d %H:%M:%S')}<br>
    <pre>{top_output}</pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
