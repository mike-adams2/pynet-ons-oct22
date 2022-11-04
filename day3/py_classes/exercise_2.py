
    
class NetworkDevice:
    def __init__(self, ip_addr, username, password):
        self.ip_addr = ip_addr
        self.username = username
        self.password = password

rtr1 = NetworkDevice('1.1.1.1', username='admin', password='admin123')
rtr2 = NetworkDevice('1.1.1.2', username='admin', password='admin123')
rtr3 = NetworkDevice('1.1.1.3', username='admin', password='admin123')
rtr4 = NetworkDevice('1.1.1.4', username='admin', password='admin123')

print(f"ip addr: {rtr4.ip_addr}")