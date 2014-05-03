import urllib, re, difflib, os.path
def urlopen(url): # MIRROR FILE LOCALLY
  fn = "diff/" + url.split("/")[-1]
  if not os.path.exists(fn):
    with open(fn, "w") as f:
      f.write(urllib.urlopen(url).read())
  return open(fn) # END OF MIRROR FUNCTION
def get_file(url):
  text = urlopen(url).read()   # next line: GPO wraps text in HTML container
  text = text.replace("<html><body><pre>\n", "").replace("\n</pre></body></html>", "")
  return re.split(r"(\s+)", text) # split on spaces to do a word-by-word comparison
# main program starts here
doc1 = get_file("http://www.gpo.gov/fdsys/pkg/BILLS-112s193is/html/BILLS-112s193is.htm")
doc2 = get_file("http://www.gpo.gov/fdsys/pkg/BILLS-112s193rs/html/BILLS-112s193rs.htm")
s = difflib.SequenceMatcher(
  lambda x : " " in x, # avoid aligning on words containing only space characters
  doc1, doc2)
op_map = { "delete": "<", "insert": ">", "equal": " ", "replace": "|" }
col_width = 38
for op, i1, i2, j1, j2 in s.get_opcodes():
  left = "".join(doc1[i1:i2]).split("\n")
  right = "".join(doc2[j1:j2]).split("\n")
  for i in xrange(max(len(left), len(right))):
    sleft = left[i] if i < len(left) else ""
    sright = right[i] if i < len(right) else ""
    print sleft[0:col_width].ljust(col_width), op_map[op], sright[0:col_width].ljust(col_width)
