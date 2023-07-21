from absl import app
from absl import flags
import random

import _jwcKernel as jwcKernel
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

    if FLAGS.B:
        flagbag = FLAGS.B        
    else:
        flagbag = None

    if FLAGS.W:
        flagwid = FLAGS.W
    else:
        flagwid = 2000

    if FLAGS.H:
        flaghei = FLAGS.H
    else:
        flaghei = 1200

    if FLAGS.C:
        flagbac = FLAGS.C
    else:
        flagbac = "white"

    if FLAGS.F:
        flagfon = FLAGS.F
    else:
        flagfon = "font\\dyh.ttf"

    if FLAGS.D:
        flagdoc = FLAGS.D
    else:
        flagdoc = "doc\\LICENSE.txt"

    if FLAGS.E:
        flagenc = FLAGS.E
    else:
        flagenc = "utf-8"

    if FLAGS.h:
        flagh = True
    else:
        flagh = False

    if FLAGS.ver:
        flagver = True
    else:
        flagver = False

    if FLAGS.o:
        flagout = "output\\"+FLAGS.o+".png"
    else:
        opnm1 = random.randint(0,99)
        opnm2 = random.randint(0,99)
        opnm3 = random.randint(0,99)
        opnm4 = random.randint(0,99)
        randout = "output\\"+str(opnm1)+str(opnm2)+str(opnm3)+str(opnm4)+".png"
        flagout = randout

    # change flag name into simply names
    #
    # Variable naming rules:
    # Use four bits to interpretation where this variable from,
    # and three bits to interpretation what will this variable do.
    #
    # example:  flag|bag-----This variable is use to define wordcloud's background.
    #           |            To be distinguish "flagbag" and "flagbac", made some diffrences between them.    
    #           |
    #       this variable is from a flag      

    if flagh == False:
        if flagver == False:
            jwcKernel.jwcKernel_Invoke(flagbag, flagwid, flaghei, flagbac, flagfon, flagdoc, flagenc, flagout)
            
        else:
            print("Jasonwordcloud(CLI) version:"+"       "+jwcVer.jwcCLI_version)
            print("Jasonwordcloud(Kernel) version:"+"    "+jwcVer.Kernel_version)
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
        print('\n\n-----ABOUT-----\nSoftware by Jasonmo <jasonmo2009@hotmail.com>\n\nOpen Source licence:Apache2.0\n\nUse "-ver" flag for version and realeases.')

if __name__ == '__main__':
        app.run(main)