# 作者: 王道 龙哥
# 2026年02月12日09时47分47秒
# xxx@qq.com
# object  基类，一切类的父类
#未掌握不影响
class MusicPlayer:
    instance = None  # 始终指向唯一的音乐播放器对象

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance=super().__new__(cls)
        return cls.instance

    def __init__(self, music_name):
        self.music_name = music_name

    def play(self):
        print(f'播放 {self.music_name} 音乐')


player1 = MusicPlayer('青花瓷')
player2 = MusicPlayer('如愿')
player1.play()
player2.play()
