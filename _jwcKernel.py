import wordcloud
import imageio
import jieba

def jwcKernel_Invoke(inptbag, inptwid, inpthei, inptbac, inptfon, inptdoc, inptenc, inptout):
    jwcKernel_Main(inptbag, inptwid, inpthei, inptbac, inptfon, inptdoc, inptenc, inptout)

def jwcKernel_Main(kernbag, kernwid, kernhei, kernbac, kernfon, kerndoc, kernenc, kernout):
    
    if kernbag == None:
        imiomsk = kernbag
    elif kernbag != None:
        imiomsk = imageio.imread(kernbag)

    wcldker = wordcloud.WordCloud(
        mask=imiomsk, 
        width=int(kernwid), 
        height=int(kernhei), 
        background_color=kernbac, 
        font_path=kernfon,
        stopwords=["的","了","在","有","人"]
    )

    docuopn = open(kerndoc, encoding=kernenc)
    docured = docuopn.read()
    jiebcut = jieba.lcut(docured)
    jiebjon = " ".join(jiebcut)
    wcldker.generate(jiebjon)
    wcldker.to_file(kernout)

    

