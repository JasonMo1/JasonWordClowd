from absl import app
from absl import flags
import random

import _jwcCore as jwcCore
import _jwcVer as jwcVer

FLAGS = flags.FLAGS
flags.DEFINE_string('B', None, 'Background of the wordcloud.')
flags.DEFINE_string('W', None, 'Width of the wordcloud.')
flags.DEFINE_string('H', None, 'Height of the wordcloud.')
flags.DEFINE_string('C', None, 'Background color of the wordcloud.')
flags.DEFINE_string('F', None, 'Font of the wordcloud.')
flags.DEFINE_string('D', None, 'Input document(should be txt) name.')
flags.DEFINE_string('E', None, 'Document encoding plan.')
flags.DEFINE_bool('h', None, 'Help.')
flags.DEFINE_bool('ver', None, 'Version.')
flags.DEFINE_string('o', None, 'Output name.')

def main(argv):
    del argv

    flagbag = FLAGS.B if FLAGS.B else None
    flagwid = FLAGS.W if FLAGS.W else 2000
    flaghei = FLAGS.H if FLAGS.H else 1200
    flagbac = FLAGS.C if FLAGS.C else "white"
    flagfon = FLAGS.F if FLAGS.F else "font\\dyh.ttf"
    flagdoc = FLAGS.D if FLAGS.D else "text\\LICENSE.txt"
    flagenc = FLAGS.E if FLAGS.E else "utf-8"
    flagh = True if FLAGS.h else False
    flagver = True if FLAGS.ver else False
    flagout = "output\\"+FLAGS.o+".png" if FLAGS.o else "output\\"+str(random.randint(0,99))+str(random.randint(0,99))+str(random.randint(0,99))+str(random.randint(0,99))+".png"

    if flagh == False:
        if flagver == False:
            args = [flagbag, flagwid, flaghei, flagbac, flagfon, flagdoc, flagenc, flagout]
            jwcCore.jwcCore_Main(args)
            
        else:
            print("Jasonwordcloud(CLI) version:"+"       "+jwcVer.jwcCLI_version)
            print("Jasonwordcloud(Core) version:"+"      "+jwcVer.Core_version)
            print("Last update(CLI):"+"                  "+jwcVer.jwcCLI_update)

    else:
        print('\nusage:\npywordcloud [-B] [-W] [-H] [-C] [-F] [-D] [-E] [-h]\n')
        print('-B:    Background of the wordcloud')
        print('-W:    Width of the wordcloud')
        print('-H:    Height of the wordcloud')
        print('-C:    Background color of the wordcloud')
        print('-F:    Font of the wordcloud')
        print('-D:    Input document(should be txt) name')
        print('-E:    Document encoding plan')
        print('-h:    Help')
        print('-ver:  Version')
        print('-o     Outputfile name')
        print('\n\n-----ABOUT-----\nSoftware by Jasonmo <jasonmo2009@hotmail.com>\n\nOpen Source licence: Apache2.0\n\nUse "-ver" flag for version and realeases.')

if __name__ == '__main__':
    app.run(main)