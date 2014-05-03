import re, difflib
def split(text):
  return re.split(r"(\s+)", text)
doc1 = split(open(filename1).read())
doc2 = split(open(filename2).read())
s = difflib.SequenceMatcher(None, doc1, doc2)
for op, i1, i2, j1, j2 in s.get_opcodes():
  if op == "delete":
    print "doc1's elements doc1[%d:%d] are deleted" % (i1, i2)
  if op == "insert":
    print "doc2's elements doc2[%d:%d] are inserted at
           position %d in doc1" % (j1, j2, i1)
  if op in ("equal", "replace"):
    print "doc1[%d:%d] are aligned with doc2[%d:%d]" % (i1, j2, j1, j2)

