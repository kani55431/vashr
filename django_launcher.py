import subprocess
import os
import webview
import threading
import time

# Function to start the Django server in the background
def start_django_server():
    # Change to your Django project directory
    os.chdir('E:/SOFTWARE/SKY LAB HRM/master')

    # Run the Django development server
    subprocess.Popen(['python', 'manage.py', 'runserver'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Function to run the webview window after the server starts
def open_webview():
    # Wait for the server to start up
    time.sleep(2)

    # Open the webview window with the Django app loaded
    webview.create_window('HRM APP', 'http://127.0.0.1:8000', width=800, height=600)
    webview.start()

# Run the Django server and the webview in parallel
if __name__ == "__main__":
    # Start Django server in a separate thread
    django_thread = threading.Thread(target=start_django_server)
    django_thread.daemon = True
    django_thread.start()

    # Open the webview
    open_webview()
