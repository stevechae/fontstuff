# program that extracts ttc into ttf files using fonttools
# usage: python ttctottf.py <ttcfile> <ttfdir>

from fontTools.ttLib import TTCollection
import argparse

parser = argparse.ArgumentParser(description='extract ttf files from ttc.')
parser.add_argument('ttc', help='ttc file')
parser.add_argument('outdir', help='ttf output directory')

args = parser.parse_args()

ttc = TTCollection(args.ttc)
for i in range(len(ttc)):
    # nameID reference: https://learn.microsoft.com/en-us/typography/opentype/spec/name#name-ids
    # postscript name format is <fontname>-<style>
    fontName = ttc[i]['name'].getDebugName(6)
    ttc[i].save(args.outdir + '/' + fontName + '.ttf')

