import django
import os,sys
import os.path

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "forlesenapp.settings")
django.setup()

from read_text.models import Word

fname = str(sys.argv[1])

if os.path.isfile(fname):
    f = open(fname,'r')
    for line in f:
        if not line in ['\n','\r\n']:
            if not Word.objects.filter(word=line.replace("\n","")).exists():
                wrd = Word(word=line.replace("\n",""))
                wrd.save()
#                print line.replace("\n","")
    f.close()
else:
    print fname
    print '\nfile does not exist'
