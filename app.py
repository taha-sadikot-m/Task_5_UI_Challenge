from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
import paramiko

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('index.html') 

@app.route('/connect')
def connect():
    return render_template('connect.html')  

@app.route('/voice')
def voice():
    return render_template('google_voice.html')  

@app.route('/model')
def model():
    return render_template('kml_models.html')  

@app.route('/diwali')
def diwali():
    return render_template('kml_knight.html')  

@app.route('/gemini')
def gemini():
    return render_template('google_geini.html')  

@app.route('/setup',methods=['POST'])
def setup():
    
    data = request.get_json()
    print(data)
    ip = data.get('ip')
    username = data.get('username')
    port = data.get('port')
    password = data.get('password')
    nodes = data.get('nodes')
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip,username=username,password=password)
    ssh.exec_command("echo 'hello'")
    try:
        return jsonify({"status": "Connected"}), 200
    except Exception as e:
        return jsonify({"status": "Error occurred"}), 500


@app.route('/show')
def show():
    try:
        ip = "192.168.56.102"
        username="lg"
        password = "123"
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip,username=username,password=password)

        
        # Create an SFTP session
        sftp = ssh.open_sftp()

        # Upload the file
        sftp.put("./static/kmls/MackyBldg.kmz", "/var/www/html/kmls/MackyBldg.kmz")
        print(f"File  has been uploaded to .")

        stdin,stdout,stderr = ssh.exec_command("echo 'http://lg1:81/kmls/MackyBldg.kmz' > /var/www/html/kmls.txt")
        print(stderr.readlines())
        print(stdout.readlines())

        command = 'echo "flytoview=<LookAt><longitude>-105.2727379358738</longitude><latitude>40.01000594412381</latitude><heading>0</heading><tilt>45</tilt><range>127.2393107680517</range><tilt>65.74454495876547</tilt><heading>-27.70337734057933</heading><altitudeMode>relativeToGround</altitudeMode></LookAt>" > /tmp/query.txt'
        stdin,stdout,stderr = ssh.exec_command(command=command);
        print(stderr.readlines())
        print(stdout.readlines())
        # Optionally, you can also download a file
        # sftp.get(remote_file, "downloaded_file.txt")

        # Close SFTP session and SSH connection
        sftp.close()
        ssh.close()
        return jsonify({"status": "Connected"}), 200
    except Exception as e:
        return jsonify({"status": "Error occurred"}), 500


@app.route('/diwali_show')
def diwali_show():
    try:
        ip = "192.168.56.102"
        username="lg"
        password = "123"
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip,username=username,password=password)

        
        # Create an SFTP session
        sftp = ssh.open_sftp()

        # Upload the file
        sftp.put("./static/kmls/Custom_Background_India_Country.kml", "/var/www/html/kmls/Custom_Background_India_Country.kml")
        print(f"File  has been uploaded to 1")


        # Upload the file
        sftp.put("./static/kmls/Custom_Background_Final_Rest_Of_Country.kml", "/var/www/html/kmls/Custom_Background_Final_Rest_Of_Country.kml")
        print(f"File  has been uploaded to 2")


        # Upload the file
        sftp.put("./static/kmls/Finalized_Data_Points.kml", "/var/www/html/kmls/Finalized_Data_Points.kml")
        print(f"File  has been uploaded to 3")

        # Upload the file
        sftp.put("./static/kmls/Custom_Load_Multiple.kml", "/var/www/html/kmls/Custom_Load_Multiple.kml")
        print(f"File  has been uploaded to 4")


        stdin,stdout,stderr = ssh.exec_command(f"echo 'http://lg1:81/kmls/Custom_Load_Multiple.kml' > /var/www/html/kmls.txt")
        print(stderr.readlines())
        print(stdout.readlines())

        command = "echo 'search=india' > /tmp/query.txt"
        stdin,stdout,stderr = ssh.exec_command(command=command);
        print(stderr.readlines())
        print(stdout.readlines())
        
        sftp.close()
        ssh.close()
        return jsonify({"status": "Connected"}), 200
    except Exception as e:
        return jsonify({"status": "Error occurred"}), 500
    

if __name__ == '__main__':
    app.run(debug=True)
