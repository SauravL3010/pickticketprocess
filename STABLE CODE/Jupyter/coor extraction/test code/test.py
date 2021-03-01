import pdfquery

# import xml.etree.ElementTree as ET


# test_file = r"C:\Users\0235124\OneDrive - University of Waterloo\Desktop\signodeProjects\pdfParse\pyPDF2\python_code\STABLE CODE\Jupyter\coor extraction\test files\IRS_1040A.pdf"
test_file = r"C:\Users\0235124\OneDrive - University of Waterloo\Desktop\signodeProjects\pdfParse\pyPDF2\python_code\STABLE CODE\Jupyter\coor extraction\test files\7183439-00.pdf"
pdf = pdfquery.PDFQuery(test_file)
pdf.load()
# label = pdf.pq('LTTextLineHorizontal:contains("Your first name and initial")')
# left_corner = float(label.attr('x0'))
# bottom_corner = float(label.attr('y0'))
# name = pdf.pq('LTTextLineHorizontal:in_bbox("%s, %s, %s, %s")' % (left_corner, bottom_corner-30, left_corner+150, bottom_corner)).text()


# # print(name)
# test = pdf.extract( [
#  ('with_parent','LTPage[pageid=\'1\']'),
#  ('with_formatter', 'text'),
#  ('last_name', 'LTTextLineHorizontal:in_bbox("315,680,395,700")'),
#  ('spouse', 'LTTextLineHorizontal:in_bbox("170,650,220,680")'),
#  ('with_parent','LTPage[pageid=\'2\']'),
#  ('oath', 'LTTextLineHorizontal:contains("perjury")'),
#  ('year', 'LTTextLineHorizontal:contains("Form 1040A (")', lambda match: int(match.text()[-5:-1]))
#  ])

pdf.tree.write("test2.xml", pretty_print=True, encoding='utf-8')
# test_case1 = pdf.pq('LTPage[pageid=\'1\'] :contains("Your first name and initial")')
# print(test['oath'])
# lambda match: match.text()[:30]+"..."

test = pdf.extract([
    ('with_parent', 'LTPage[pageid=\'1\']'),
    # ('with_formatter', 'text'),
    ('order no', 'LTTextLineHorizontal:in_bbox("640, 450, 700, 560")'),
    # ('test', 'LTTextLineHorizontal:contains("Order #")'),
    ('test', 'LTTextLineHorizontal:contains("Line")'),
])

# print(test['order no'])
# root = test['order no'].getroot()

# print(test['order no'])

# xy = [float(x) for x in test['test'][0].get('bbox')[1:-1].split(',')]
# x0_test = xy[0] 
# x1_test = xy[2]



# print(x0_test, x1_test)



print(test['order no'], '\n')

for elm in test['order no']:
    print(elm.attrib)



# print(len(test['order no']))

# for i in range(len(test['order no'])):
#     print(test['order no'][i])
#     print(test['order no'][i].get('bbox'), test['order no'][i].text) 
    # if test['order no'][i].text:
    #     print(test['order no'][i].get('bbox'), test['order no'][i].text)
    # else:
    #     try:
    #         while

# print(test['order no'][0].attr.bbox)

# label = pdf.pq('LTTextLineHorizontal:contains("718")')
# left_corner = float(label.attr('x0'))
# bottom_corner = float(label.attr('y0'))
# name = pdf.pq('LTTextLineHorizontal:in_bbox("%s, %s, %s, %s")' % (left_corner, bottom_corner-30, left_corner+150, bottom_corner)).text()


# print(label)

# x0 = float(label.attr.x0)
# y0 = float(label.attr('y0'))
# x1 = float(label.attr('x1'))
# y1 = float(label.attr('y1'))

# bbox="[649.92, 544.887, 693.417, 553.887]"
# 649.92, 475.407

# print(x0, y0, x1, y1)

# [582.24 545.184 609.36 553.184]

# <LTTextLineHorizontal y0="475.407" y1="484.407" x0="649.92" x1="681.411" width="31.491" height="9.0" bbox="[649.92, 475.407, 681.411, 484.407]" word_margin="0.1">
#     <LTTextBoxHorizontal y0="475.407" y1="484.407" x0="649.92" x1="681.411" width="31.491" height="9.0" bbox="[649.92, 475.407, 681.411, 484.407]" index="3">
#         Demark 
#     </LTTextBoxHorizontal>
# </LTTextLineHorizontal>
# <LTTextLineHorizontal y0="455.487" y1="464.487" x0="649.92" x1="695.91" width="45.99" height="9.0" bbox="[649.92, 455.487, 695.91, 464.487]" word_margin="0.1">
#     <LTTextBoxHorizontal y0="455.487" y1="464.487" x0="649.92" x1="695.91" width="45.99" height="9.0" bbox="[649.92, 455.487, 695.91, 464.487]" index="5">
#         Net 30 Days 
#     </LTTextBoxHorizontal>
# </LTTextLineHorizontal>
# <LTTextLineHorizontal y0="544.887" y1="553.887" x0="649.92" x1="693.417" width="43.497" height="9.0" bbox="[649.92, 544.887, 693.417, 553.887]" word_margin="0.1">
#     7183439-00 
# </LTTextLineHorizontal>
# <LTTextLineHorizontal y0="524.967" y1="533.967" x0="649.92" x1="696.918" width="46.998" height="9.0" bbox="[649.92, 524.967, 696.918, 533.967]" word_margin="0.1">
#     BC20-21201 
# </LTTextLineHorizontal>
# <LTTextLineHorizontal y0="505.167" y1="514.167" x0="649.92" x1="689.916" width="39.996" height="9.0" bbox="[649.92, 505.167, 689.916, 514.167]" word_margin="0.1">
#     PREPAID 
# </LTTextLineHorizontal>


