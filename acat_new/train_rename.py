#!/usr/bin/python

import sys, os, shutil

################################################################################
# main
################################################################################

def main():
  if len(sys.argv) < 3 or len(sys.argv) > 5:
    help(DEFAULT_NAMESPACE, DEFAULT_TYPE_DIR);
    sys.exit(-1)

  inPath = sys.argv[1]
  outPath = sys.argv[2]

  print "Searching for files..."
  files = []
  for filename in os.listdir(inPath):
    filepath = os.path.join(inPath, filename)
    if not os.path.isfile(filepath):
      print "Ignoring file: " + filename
      continue

    (name, ext) = os.path.splitext(filename)
    if ext.lower() != ".png" or name.rfind("_color") < 0:
      print "Ignoring file: " + filename
      continue
    files.append(filepath)
    files.sort()

#  names = [ ("pipette", 8)
#          , ("bottle_500ml", 6)
#          , ("bottle_cap", 3)
#          , ("pipette_tips_box", 8)
#          , ("trash_box", 4)
#          #, ("tube_50ml", 5) #rack
#          #, ("tube_50ml", 10) #tube
#          , ("tube_50ml", 15) #together
#          , ("tube_50ml_cap", 3)
#          , ("tube_10ml", 16)
#          , ("tube_10ml_cap", 3)
#          ]
  names = [ ("tubes_rack", 10)
          , ("trash_box", 13)
          , ("bottle_500ml", 8)
          , ("pipette", 12)
          , ("pipette_tips_box", 12)
          , ("lid_10ml_red",6)
          , ("lid_10ml_blue",7)
          , ("bottle_500ml_cap",6)
          ]
  counter = 0
  index = 0

  for filename in files:
    if counter >= names[index][1]:
      counter = 0
      index += 1

    outName = "{}_{:02d}.png".format(names[index][0], counter)
    outName = os.path.join(outPath, outName)

    print "copy: {} to {}".format(os.path.basename(filename), os.path.basename(outName))
    shutil.copy(filename, outName)
    counter += 1

  return 0


################################################################################
# __main__
################################################################################

if __name__ == "__main__":
  ret = main()
  sys.exit(ret)
