
import tkinter as tk
import socket
global inp # global variable
# Top level window
frame = tk.Tk()
frame.title("TextBox Input")
frame.geometry('400x200')
# Function for getting Input
# from textbox and printing it 
# at label widget
# SOcket tcp/ip
# Create a TCP/IP socket


# client socket function
def client_socket():
    global inp
    inp = inputtxt.get(1.0, "end-1c")
    lbl.config(text = "Message to send: "+inp)
    print("the message to send is: "+inp)
    print(inp)
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('192.168.2.2',4242))
    s = socket.socket()
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect the socket to the port where the server is listening
    server_address = ('localhost', 4242)
    sock.connect(server_address)
    # Send data
    message = inp
    sock.sendall(message.encode())
    # Close the socket
    sock.close()    

def printInput():
    global inp
    inp = inputtxt.get(1.0, "end-1c")
    lbl.config(text = "Message to send: "+inp)
  
# TextBox Creation
inputtxt = tk.Text(frame,
                   height = 5,
                   width = 20)
  
inputtxt.pack()
  
# Button Creation
printButton = tk.Button(frame,
                        text = "Send", 
                        command = printInput)
printButton.pack()
# Button to send message
sendButton = tk.Button(frame,
                        text = "Send to tcp",
                        command = client_socket)
sendButton.pack()
# Label Creation
lbl = tk.Label(frame, text = "")
lbl.pack()
frame.mainloop()
