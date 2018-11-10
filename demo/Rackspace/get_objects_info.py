"""
Get table frm soup and extract the key value from html table
## format of row in table:
#<tr>
# <th class="tdright sticker" width="50%">FQDN:</th>
# <td class="tdleft"><a  href="ssh://mail8.webfaction.com">mail8.webfaction.com</a></td>
#</tr>
# In <th> tag is the key and in <td> tag is the value we are using to create dictionary
"""

def get_objects_info(beauty_soap):
    """ Return dictionary with Rackspace objects info """

    key_list = []
    value_list = []

    div = beauty_soap.find("div", {"class":"portlet"})
    table = div.find("table")
    rows = table.find_all("tr")

    for row in rows:
        if hasattr(row.th, 'text'):
            key_list.append(str(row.th.text.strip().strip(":").replace(" ", "_")))
        else:
            key_list.append("No_key")

        if hasattr(row.td, 'text'):
            value_list.append(str(row.td.text.strip()))
        else:
            value_list.append("No_value")

    return dict(zip(key_list, value_list))
