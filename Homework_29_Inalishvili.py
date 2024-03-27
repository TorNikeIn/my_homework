# მოიძიე ინტერნეტში, გაუშვი და დააკომენტარე ჩათის კოდი, რომელიც ფუნქციონირებს UDP-ის გამოყენებით.


# სერვერის ფაილის კოდი
import socket

localIP = "127.0.0.1"

localPort = 20001

bufferSize = 1024

msgFromServer = "Hello UDP Client"

bytesToSend = str.encode(msgFromServer)

# იუ დი პი სოკეტის შექმნა

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# ლოკალური აი პის და პორტის ბაინდინგი

UDPServerSocket.bind((localIP, localPort))

print("UDP server up and listening")

# მიღებული მონაცემების "მოსმენა"

while (True):
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

    message = bytesAddressPair[0]

    address = bytesAddressPair[1]

    clientMsg = "Message from Client:{}".format(message)
    clientIP = "Client IP Address:{}".format(address)

    print(clientMsg)
    print(clientIP)

    # პასუხის გაგზავნა კლიენტისთვის

    UDPServerSocket.sendto(bytesToSend, address)






# კლიენტის ფაილის კოდი

import socket

msgFromClient = "Hello UDP Server"

bytesToSend = str.encode(msgFromClient)

serverAddressPort = ("127.0.0.1", 20001)

bufferSize = 1024

#სოკეტი კლიენტის მხარეს

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# სერვერისთვის გაგზავნა სოკეტის გამოყენებით

UDPClientSocket.sendto(bytesToSend, serverAddressPort)

msgFromServer = UDPClientSocket.recvfrom(bufferSize)

msg = "Message from Server {}".format(msgFromServer[0])

print(msg)