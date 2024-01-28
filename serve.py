from flask import Flask, redirect, url_for, request
import socket
import subprocess
app = Flask(__name__)

@app.route('/')
def success():
   return 'Hello World'

@app.route('/getIP',methods = ['GET'])
def getIP():
    print(f"IP of EC2 instance ={socket.gethostname()}")
    return socket.gethostname()

@app.route('/stressCpu',methods = ['POST'])
def stressCpu():
    print(f"stressing the CPU to 100% utilization")
    subprocess.Popen("python3 stress_cpu.py", shell=True, stdout=subprocess.PIPE)
    return "invoked stress_cpu function"


if __name__ == '__main__':
   app.run(host='0.0.0.0', port =8000)
