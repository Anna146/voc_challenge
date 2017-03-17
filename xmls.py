from PIL import Image
import os
import json
from lxml import etree

imgdir_path = 'C:/DVD_Potocnik_31.08.2016/real_tif/'
mode_to_bpp = {'1':1, 'L':8, 'P':8, 'RGB':24, 'RGBA':32, 'CMYK':32, 'YCbCr':24, 'I':32, 'F':32}
path_box = 'C:/Users/tigunova/PycharmProjects/untitled1/'
classes = ['pzip', 'aftertax', 'commission', 'tripdate', 'duedate', 'traveller', 'voucherdate', 'pretax', 'pstreet', 'pcity']

for name in os.listdir(imgdir_path):
    # create XML
    root = etree.Element('annotation')
    # another child with text
    child = etree.Element('folder')
    child.text = 'aurebu'
    root.append(child)
    child = etree.Element('filename')
    child.text = name
    root.append(child)
    child = etree.Element('source')
    child2 = etree.Element('database')
    child2.text = 'aurebu'
    child.append(child2)
    child2 = etree.Element('annotation')
    child2.text = 'aurebu'
    child.append(child2)
    child2 = etree.Element('image')
    child2.text = '1'
    child.append(child2)
    child2 = etree.Element('flickrid')
    child2.text = '1'
    child.append(child2)
    root.append(child)
    child = etree.Element('owner')
    child2 = etree.Element('flickrid')
    child2.text = '1'
    child.append(child2)
    child2 = etree.Element('name')
    child2.text = 'anna'
    child.append(child2)
    root.append(child)
    im = Image.open(imgdir_path + name)
    child = etree.Element('size')
    child2 = etree.Element('width')
    child2.text = str(im.width)
    child.append(child2)
    child2 = etree.Element('height')
    child2.text = str(im.height)
    child.append(child2)
    child2 = etree.Element('depth')
    child2.text = str(mode_to_bpp[im.mode])
    child.append(child2)
    root.append(child)
    im.close()
    child = etree.Element('segmented')
    child.text = '0'
    root.append(child)
    for cl in classes:
        boxx = path_box + 'boxes_' + cl + '/test_boxes1.json'
        with open(boxx, 'r') as jf:
            js = json.load(jf)
            for rec in js:
                if name == rec['image_path'][6:]:
                  for sqr in rec['rects']:
                    child = etree.Element('object')
                    child2 = etree.Element('name')
                    child2.text = str(cl)
                    child.append(child2)
                    child2 = etree.Element('pose')
                    child2.text = 'Unspecified'
                    child.append(child2)
                    child2 = etree.Element('truncated')
                    child2.text = str(0)
                    child.append(child2)
                    child2 = etree.Element('difficult')
                    child2.text = str(0)
                    child.append(child2)
                    child2 = etree.Element('bndbox')
                    child3 = etree.Element('xmin')
                    child3.text = str(sqr['x1'])
                    child2.append(child3)
                    child3 = etree.Element('ymin')
                    child3.text = str(sqr['y1'])
                    child2.append(child3)
                    child3 = etree.Element('xmax')
                    child3.text = str(sqr['x2'])
                    child2.append(child3)
                    child3 = etree.Element('ymax')
                    child3.text = str(sqr['y2'])
                    child2.append(child3)
                    child.append(child2)
                    root.append(child)
    f = open('annotations/' + name[:-4] + '.xml', 'w')
    f.write(etree.tostring(root))
    f.close()
    # pretty string
    #s = etree.tostring(root, pretty_print=True)
    #print s