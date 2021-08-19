# cv2(OpenCV)を利用する宣言を行う。
import cv2

class Paint:
    # 画像情報
    img = None
    # しきい値情報
    # しきい値とは? : https://wa3.i-3-i.info/word15002.html
    ret = None
    # 輪郭を形成する画素(点)情報
    contours = None
    # オブジェクト(物体)の階層構造情報
    # 階層構造とは? : https://wa3.i-3-i.info/word15200.html
    hierarchy = None

    # コンストラクタ
    # コンストラクタとは? : https://ja.wikipedia.org/wiki/%E3%82%B3%E3%83%B3%E3%82%B9%E3%83%88%E3%83%A9%E3%82%AF%E3%82%BF#:~:text=%E3%82%B3%E3%83%B3%E3%82%B9%E3%83%88%E3%83%A9%E3%82%AF%E3%82%BF%EF%BC%88%E8%8B%B1%3A%20constructor%EF%BC%89%E3%81%AF,%E5%AF%BE%E7%BE%A9%E8%AA%9E%E3%81%AF%E3%83%87%E3%82%B9%E3%83%88%E3%83%A9%E3%82%AF%E3%82%BF%E3%80%82
    # 画像の初期化
    def __init__(self, image=None):
        self.img = image

    # 画像をグレースケールに設定する関数
    # グレースケールとは? : https://www.shinkohsha.co.jp/blog/monochrome-shirokuro-grayscale/
    def setGray(self):
        # cvtColor : 画像の色を変更する関数
        # 第一引数 : 画像情報
        # 第二引数 : 画像の色を変更するタイプの指定
        # cv2.COLOR_BGR2GRAY : 画像をグレースケールへ変更する。
        # 画像の色を変更するタイプ一覧情報 : https://docs.opencv.org/4.2.0/d8/d01/group__imgproc__color__conversions.html#ga397ae87e1288a81d2363b61574eb8cab
        self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)

    # グレースケール画像を二値画像へ変更する関数
    def setBinaryImage(self):
        # threshold : しきい値を用いて画像を二値画像へ変更する関数。
        # 第一引数 : 画像情報(グレースケールでないといけない。二値画像へ変更できないため。)
        # 第二引数 : しきい値(しきい値の設定次第で、輪郭の検出の精度が変わります。何度もしきい値を変えて、生成される二値画像を確認し、しきい値を定めることをおすすめします。)
        # 第三引数 : しきい値を超えた画素(点)に対して、与える色の値を指定。黒色とする。
        # 第四引数 : 二値画像を判定する条件のタイプを設定する。
        # cv2.THRESH_BINARY : (画素(点)の値 <= 第二引数)の場合、画素(点)に対して、0(白色)の値を与える。(画素(点)の値 > 第二引数)の場合、画素(点)に対して、第三引数の値(黒色)を与える。
        # 二値画像を判定する条件のタイプ一覧情報 : https://pystyle.info/opencv-image-binarization/
        # 戻り値 #################
        # self.ret : しきい値を返す。
        # self.img : 二値画像情報を返す。
        #########################
        self.ret, self.img = cv2.threshold(self.img, 160, 255, cv2.THRESH_BINARY)

    # 輪郭の検出を行う関数
    def exeFindContours(self):
        # findContours : 輪郭の検出を行う関数
        # 第一引数(thresh) : 二値画像情報
        # 第二引数(mode) : 輪郭を検出するタイプを指定する。
        # 第三引数(method) : 輪郭を形成する、画素(点)を近似する方法のタイプを指定する。
        # 戻り値  ###########################################
        # self.img : 輪郭付き画像情報
        # self.contours : 輪郭を形成する画素(点)情報
        # self.hierarchy : オブジェクト(物体)の階層構造情報
        ####################################################

        # OpenCVのバージョンが4.0より小さい場合
        # self.img, self.contours, self.hierarchy = cv2.findContours(self.img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        # OpenCVのバージョンが4.0以上の場合
        self.contours, self.hierarchy = cv2.findContours(self.img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    # 輪郭の描画を行う関数
    def exeDrawContours(self):
        # drawContours : 輪郭の検出情報をもとに、輪郭の描画を行う関数
        # 第一引数 : 画像情報
        # 第二引数 : 輪郭を形成する画素(点)情報
        # 第三引数 : 輪郭を形成する画素(点)のインデックス番号を指定する。例えば0を指定すると、1番目の輪郭を形成する画素(点)のみを描画する。1を指定すると、2番目の輪郭を形成する画素(点)のみを描画する。輪郭を形成する画素(点)を全て描画したい場合は、-1を指定する。
        # 第四引数 : 輪郭を形成する画素(点)の色。
        # 第五引数(任意) : 輪郭を形成する画素(点)の大きさを設定。デフォルト1。
        # 戻り値 : 画像情報
        # drawContoursについて : https://kuroro.blog/python/xaw33ckABzGLiHDFWC3m/
        self.img = cv2.drawContours(self.img, self.contours, -1, 192, 5)

    # 画像情報を取得する関数
    def getImg(self):
        return self.img

    # 画像情報を書き込む関数
    def writeImg(self, filePath):
        # imwrite : 画像の書き出しを行う関数
        # 第一引数 : 書き出し先の画像ファイル名
        # 第二引数 : 画像情報
        cv2.imwrite(filePath, self.img)

# imread : 指定した画像ファイルパスを読み込んで、画像に対してcv2(OpenCV)を利用できるようにする。
# 第一引数 : 画像ファイルパス
ins = Paint(cv2.imread('./input.jpg'))
ins.setGray()
ins.setBinaryImage()
ins.exeFindContours()
ins.exeDrawContours()
ins.writeImg('./output.jpg')
