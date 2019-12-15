import paramiko
import time

ends_in_channel = ['# ', '$ ']  # 终端接收完成判断字符

buffer_size = 1024  # 终端消息接收缓冲区尺寸

receive_step_time = 0.2  # 接收消息的重读时间间隔，单位（秒）

check_state_step_time = 0.2  # 检查终端状态的时间间隔，单位（秒）


class Util:
    @staticmethod
    def __check_end(in_str):
        """
        检查接收到的消息尾部是否在预定范围内
        :param in_str: 需要被检查的字符串
        :return: 尾部为预定值则返回true，否则返回false
        """
        check_obj = str(in_str)
        for end in ends_in_channel:
            if check_obj.endswith(end):
                return True
        return False

    @staticmethod
    def channel_recv(channel):
        """
        接收终端的消息，并且返回本次的执行结果
        :param channel: 终端对象
        :return:
        """
        if not isinstance(channel, paramiko.Channel):
            raise Exception("param type is error")
        res_str = ''
        while True:
            res_str += str(channel.recv(buffer_size), encoding='utf-8')
            if Util.__check_end(res_str):
                return res_str
            time.sleep(receive_step_time)

