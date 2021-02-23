# if order no ['original_print'] == True:
# add "_reprint"
from datetime import datetime
from jsonMod import load_json, add_to_json, update_values 


def reprint_dates(order_no, jsonfile, json_dict_to_verify, json_data):
    '''
    order_no = OrderNo from pickticket
    jsonfile = main json file ("master_pick_tickets.json")
    json_dict_to_verify = "json_dict_to_add" in read_file()
    json_data = loaded json data (load everytime before calling "read_file" function)
    '''
    target = json_data[order_no[:10]]['reprintDate']
    if not order_no in json_dict_to_verify:
        try:
            target.append(str(datetime.now()))
        except:
            target = []
            target.append(str(datetime.now()))
        update_values(jsonfile, order_no[:10], "reprintDate", target)
        
    

def if_order_as_originalPrint(order_no, json_data):
    '''
    order_no = OrderNo from pickticket
    json_data = loaded json data (load everytime before calling "read_file()" function)
    '''
    if order_no in json_data:
        return json_data[order_no]["originalPrint"]
        


def if_order_exists_return_renamed(order_no, json_data):
    '''
    order_no = OrderNo from pickticket
    json_data = loaded json data (load everytime before calling "read_file()" function)
    '''
    while order_no in json_data:
        order_no = order_no + "_reprint"
    return order_no 



def append_data(originalPrint, reprintDate, dateReceived, 
                emailAttachment, shipTo, via, fileDirectory, 
                status="Just Received", shippedDate=None, billedDate=None, 
                isExcelUpdated=False, isShippedExcelUpdated=False, isBilledExcelUpdated=False):
    '''
    all mandatory data
    contains all the data {keys:values} required for each pick ticket.
    '''
    return_dict = {
                    "dateReceived" : dateReceived,
                    "originalPrint" : originalPrint,
                    "reprintDate" : reprintDate,
                    "emailAttachment" : emailAttachment,
                    "shipTo" : shipTo,
                    "via": via,
                    "fileDirectory" : fileDirectory,
                    "status" : status,
                    "shippedDate" : shippedDate,
                    "billedDate" : billedDate,
                    "isExcelUpdated" : isExcelUpdated,
                    "isShippedExcelUpdated" : isShippedExcelUpdated,
                    "isBilledExcelUpdated" : isBilledExcelUpdated,
                    }
    return return_dict




def ship_via(jsonfile, narrowed_text):
    '''
    jsonfile = main json file ("ALL_SHIP_VIA.json")
    narrowed_text = is narrowed_text in read_file() function
    
    matches "via" with SX data for "ship via"
    '''
    via_json = load_json(jsonfile)
    via_return = "NOT FOUND"
    for via_name in via_json["Signode_Ship_Via"]:
        if via_name in narrowed_text:
            via_return = via_name
    return via_return