



class JukeBox:

    def __init__(self):
        self.songRequestQueue = []


    def play(self):
        for i in range(len(self.songRequestQueue)):
            print(self.songRequestQueue.pop(0))


    def add(self):
        songRq = SongRequest()
        self.songRequestQueue = songRq.getPlayList()



    def remove(self, nameOrTitle):
        tmpList = []
        for row in self.songRequestQueue:
            if nameOrTitle in row:
                del row
            else:
                tmpList.append(row)

        self.songRequestQueue = tmpList

class StackJukeBox(JukeBox):
    def __init__(self):
        super().__init__()

    def play(self):
        for i in range(len(self.songRequestQueue)):
            print(self.songRequestQueue.pop())

class GenreJukeBox(JukeBox):
    def __init__(self):
        super().__init__()

    def play(self, genre):
        for row in self.songRequestQueue:
            if genre in row:
                print(row)

class SingerJukeBox(JukeBox):
    def __init__(self):
        super().__init__()

    def play(self, singerName):
        for row in self.songRequestQueue:
            if singerName in row:
                print(row)


class SongRequest:
    def __init__(self):
        # 직접 입력하려면 밑에 두줄 주석 해제후 세번쨰 코드 주석 빠른 실행은 그대로 실행하시면 됩니다.
        # self.playList = []
        # self.inputPlayList()
        self.playList = [['choi', 'pop', 'blinding light', 'weeknd'],
                         ['young', 'hiphop', 'who that b', 'jessi'],
                         ['min', 'hiphop', 'no heart', '21 savage'], ]


    def inputPlayList(self):
        while True:
            name = input('고객이름 입력 (0 입력시 종료): ')
            if name == '0':
                break
            addSong = Song()
            addSong.inputData()
            gerne, title, singer = addSong.getData()
            tmpList = [name, gerne, title, singer]
            self.playList.append(tmpList)


    def getPlayList(self):
        return self.playList



class Song:
    def __init__(self):
        self.genre = None
        self.title = None
        self.singer = None


    def inputData(self):
        self.genre = input("장르 입력:")
        self.title = input('타이틀 입력:')
        self.singer = input('가수 입력:')

    def getData(self):
        return self.genre, self.title, self.singer


if __name__ == '__main__':
    # 삭제 구현 확인
    jk = JukeBox()
    jk.add()
    jk.remove(nameOrTitle='choi')
    jk.play()

    # 나중에 들어간 노래부터 재생 확인
    jk1 = StackJukeBox()
    jk1.add()
    jk1.play()

    # 특정 장르 노래만 재생 확인
    jk2 = GenreJukeBox()
    jk2.add()
    jk2.play(genre='hiphop')

    # 특정 가수 노래만 재생 확인
    jk3 = SingerJukeBox()
    jk3.add()
    jk3.play(singerName='jessi')