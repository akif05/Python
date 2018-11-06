def get_objects_info(beauty_soap):

    key_list = []
    value_list = []
    object_dict = {}
    line = "=" * 50

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

    # object_dict = dict(zip(key_list, value_list))
    return dict(zip(key_list, value_list))


