from PyPDF2 import PdfFileReader
import os
import glob
from datetime import datetime

pdf_files = glob.glob(os.path.join(os.getcwd(),'*.pdf'))


'''
PickTicket attreibutes: 
    OrdrNo, Time Created, Via
    Was it Reprinted - Boolean
    email Attachment 

    Track if in Picked Stage

'''
class Pickticket():

    def __init__(self, orderNo, via, isReprinted=False, emailAttachment=None):
        self.orderNo = orderNo
        self.via = via
        self.created = datetime.now()
        self.isReprinted = isReprinted
        self.emailAttachment = emailAttachment


class Ticket(Pickticket):
    pass

pick1 = Ticket('7181234-00', 'FastFreight')

