
from UtilsFunction import *
from UtilSystemFunction import *


class SSHConnect:
    def __init__(self):
        self.host = '47.92.50.193'
        self.host = '192.168.1.190'
        self.user_name = 'pi'
        self.password = '198516xl'
        self.port = 22
        self.ssh_client = None
        self.channel = None
        self.sftp_client = None

    def connect(self):
        self.ssh_client = paramiko.SSHClient()
        self.ssh_client.load_system_host_keys()
        self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh_client.connect(hostname=self.host, username=self.user_name, password=self.password)
        self.channel = self.ssh_client.invoke_shell()
        transport = paramiko.Transport((self.host, self.port))
        transport.connect(username=self.user_name, password=self.password)
        self.sftp_client = paramiko.SFTPClient.from_transport(transport)
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

    def down_load_file(self, src_path_name, des_path):
        """
        将文件下载到指定的目录
        :param src_path_name: 源文件的路径及名称
        :param des_path: 需要保存的目标路径，名称将从src_path_name中获取
        :return:
        """
        file_name = os.path.basename(src_path_name)
        try:
            self.sftp_client.get(src_path_name, des_path + sep_char + file_name)  # 该函数可能产生IOError
        except IOError as e:
            print("down_load_file operation failed, " + src_path_name
                  + ":code(" + str(e.errno) + "),msg:" + e.strerror)


if __name__ == '__main__':
    ssh = SSHConnect()
    ssh.send_comm("cd /tmp; ls -lrt")
    ssh.send_comm("cd /opt; ls -lrt")
    print("current path is:" + current_process_path())
    ssh.down_load_file("/usb_mobile_disk_1T/MyFiles/piTmp/aria2/log/aria2.log2", current_process_path())
    # ssh.send_comm("cd /usb_mobile_disk_1T/MyFiles/piTmp/aria2/log;cat aria2.log")
