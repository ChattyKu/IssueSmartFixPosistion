
from UtilsFunction import *


class SSHConnect:
    def __init__(self):
        self.host = '47.92.50.193'
        self.user_name = 'root'
        self.password = 'aLi_Well'
        self.ssh_client = None
        self.channel = None

    def connect(self):
        self.ssh_client = paramiko.SSHClient()
        self.ssh_client.load_system_host_keys()
        self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh_client.connect(hostname=self.host, username=self.user_name, password=self.password)
        self.channel = self.ssh_client.invoke_shell()
        return True

    def send_comm(self, comm):
        if self.channel is None:
            self.connect()
        while True:
            if self.channel.send_ready():
                break
            time.sleep(receive_step_time)
        print("wait ready")
        self.channel.send(comm + "\n")
        recv = Util.channel_recv(self.channel)
        print(recv)


if __name__ == '__main__':
    ssh = SSHConnect()
    ssh.send_comm("cd /tmp; ls -lrt")
    ssh.send_comm("cd /opt; ls -lrt")
