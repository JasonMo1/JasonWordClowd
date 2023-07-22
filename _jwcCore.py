import wordcloud
import imageio
import jieba

def jwcCore_Main(args:list=[None, 2000, 1200, "white", "font\\dyh.ttf", "doc\\LICENSE.txt", "utf-8"]):

    imiomsk = imageio.imread(args[0]) if args[0] else None

    wcldker = wordcloud.WordCloud(
        mask=imiomsk,
        width=int(args[1]),
        height=int(args[2]),
        background_color=args[3],
        font_path=args[4],
        stopwords=["的", "了", "在", "有", "人"]
    )

    with open(args[5], encoding=args[6]) as docuopn:
        docured = docuopn.read()
    jiebjon = " ".join(jieba.lcut(docured))
    wcldker.generate(jiebjon)
    wcldker.to_file(args[7])