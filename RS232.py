import serial  # 导入串口通信库
from time import sleep

ser = serial.Serial()


def port_open_recv():  # 对串口的参数进行配置
    ser.port = 'com3'  # 设置串口号
    ser.baudrate = 9600  # 波特率
    ser.bytesize = 8  # 数据位数
    ser.stopbits = 1  # 停止位
    ser.parity = "N"  # 奇偶校验位
    ser.open()
    if (ser.isOpen()):
        print("串口打开成功！")
    else:
        print("串口打开失败！")


# isOpen()函数来查看串口的开闭状态


def port_close():
    ser.close()
    if (ser.isOpen()):
        print("串口关闭失败！")
    else:
        print("串口关闭成功！")


def send(send_data):
    if (ser.isOpen()):
        ser.write(send_data.encode('utf-8'))  # 编码
        print("发送成功", send_data)
    else:
        print("发送失败！")


if __name__ == '__main__':
    # 网址：https://blog.csdn.net/weixin_43217958/article/details/109782000#:~:text=ser.isOpen%28%29%EF%BC%9A%E6%9F%A5%E7%9C%8B%E7%AB%AF%E5%8F%A3%E6%98%AF%E5%90%A6%E8%A2%AB%E6%89%93%E5%BC%80%E3%80%82%20ser.open%28%29%20%EF%BC%9A%E6%89%93%E5%BC%80%E7%AB%AF%E5%8F%A3%E2%80%98%E3%80%82%20ser.close%28%29%EF%BC%9A%E5%85%B3%E9%97%AD%E7%AB%AF%E5%8F%A3%E3%80%82,ser.read%28%29%EF%BC%9A%E4%BB%8E%E7%AB%AF%E5%8F%A3%E8%AF%BB%E5%AD%97%E8%8A%82%E6%95%B0%E6%8D%AE%E3%80%82%20%E9%BB%98%E8%AE%A41%E4%B8%AA%E5%AD%97%E8%8A%82%E3%80%82%20ser.read_all%28%29%3A%E4%BB%8E%E7%AB%AF%E5%8F%A3%E6%8E%A5%E6%94%B6%E5%85%A8%E9%83%A8%E6%95%B0%E6%8D%AE%E3%80%82%20ser.write%28%22hello%22%29%EF%BC%9A%E5%90%91%E7%AB%AF%E5%8F%A3%E5%86%99%E6%95%B0%E6%8D%AE%E3%80%82
    port_open_recv()
    while True:
        a = input("输入要发送的数据：")
        send(a)
        sleep(0.5)  # 起到一个延时的效果，这里如果不加上一个while True，程序执行一次就自动跳出了
