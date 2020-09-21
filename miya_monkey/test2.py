import socket# 客户端 发送一个数据，再接收一个数据
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #声明socket类型，同时生成链接对象
#client.bind(('localhost',9091)) #绑定要监听的端口，这一步可以不需要，如果绑定了，
# 那么客户服务器就会用这个固定的端口发送消息，如果没绑定，端口就是随机的用
client.connect(('staging-s.miyachat.com',9090)) #建立一个链接，连接到本地的9090端口
msg = "来自请求服务器的--请求"
client.send(msg.encode('utf-8'))  #发送一条信息 python3 只接收btye流
data = client.recv(1024) #接收一个信息，并指定接收的大小 为1024字节
print('recv:',data.decode()) #输出接收到的信息