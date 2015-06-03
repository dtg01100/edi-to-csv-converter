import upc_check_digit


def edi_convert(edi_process, output_filename, calc_upc, inc_arec, inc_crec, inc_headers):

    column1 = []
    column2 = []
    column3 = []
    column4 = []
    column5 = []
    column6 = []
    column7 = []
    column_append = []
    column_prepend = []
    conv_calc_upc = calc_upc
    conv_inc_arec = inc_arec
    conv_inc_crec = inc_crec
    conv_inc_headers = inc_headers


    work_file = open(edi_process)
    work_file_count = open(edi_process)
    cut_off = sum(1 for line in work_file_count)
    work_file = [n for n in work_file.readlines() if not n.startswith('A') if not n.startswith('C')]
    for line_num, line in enumerate(work_file):
        if line_num < cut_off:
            #print line[1:12]
            if conv_calc_upc != 1:
                column1.append(line[1:12])
            else:
                column1.append(upc_check_digit.add_check_digit(line[1:12]))
    #print (column1)

    work_file = open(edi_process)
    work_file_count = open(edi_process)
    cut_off = sum(1 for line in work_file_count)
    work_file = [n for n in work_file.readlines() if not n.startswith('A') if not n.startswith('C')]
    for line_num, line in enumerate(work_file):
        if line_num < cut_off:
            #print line[12:37]
            column2.append(line[12:37])
    #print (column2)

    work_file = open(edi_process)
    work_file_count = open(edi_process)
    cut_off = sum(1 for line in work_file_count)
    work_file = [n for n in work_file.readlines() if not n.startswith('A') if not n.startswith('C')]
    for line_num, line in enumerate(work_file):
        if line_num < cut_off:
            #print line[38:43]
            column3.append(line[38:43])
    #print (column3)

    work_file = open(edi_process)
    work_file_count = open(edi_process)
    cut_off = sum(1 for line in work_file_count)
    work_file = [n for n in work_file.readlines() if not n.startswith('A') if not n.startswith('C')]
    for line_num, line in enumerate(work_file):
        if line_num < cut_off:
            #print line[45:49]
            column4.append(line[45:47] + "." + line[47:49])
    #print (column4)

    work_file = open(edi_process)
    work_file_count = open(edi_process)
    cut_off = sum(1 for line in work_file_count)
    work_file = [n for n in work_file.readlines() if not n.startswith('A') if not n.startswith('C')]
    for line_num, line in enumerate(work_file):
        if line_num < cut_off:
            #print line[55:57]
            column5.append(line[55:57])
    #print (column5)

    work_file = open(edi_process)
    work_file_count = open(edi_process)
    cut_off = sum(1 for line in work_file_count)
    work_file = [n for n in work_file.readlines() if not n.startswith('A') if not n.startswith('C')]
    for line_num, line in enumerate(work_file):
        if line_num < cut_off:
            #print line[63:67]
            column6.append(line[63:65] + "." + line[65:67])
    #print (column6)

    work_file = open(edi_process)
    work_file_count = open(edi_process)
    cut_off = sum(1 for line in work_file_count)
    work_file = [n for n in work_file.readlines() if not n.startswith('A') if not n.startswith('C')]
    for line_num, line in enumerate(work_file):
        if line_num < cut_off:
            #print line[60:62]
            column7.append(line[60:62])
    #print (column7)

    if conv_inc_arec != 0:
        f = open(output_filename, "w")
        work_file = open(edi_process)
        work_file_count = open(edi_process)
        cut_off = sum(1 for line in work_file_count)
        work_file = [n for n in work_file.readlines() if not n.startswith('B') if not n.startswith('C')]
        for line_num, line in enumerate(work_file):
            if line_num < cut_off:
                #print line[:]
                column_prepend.append(line[:])
        #print (column_prepend)
        f.seek(0, 0)
        for i in xrange(len(column_prepend)):
            f.write("{}".format(column_prepend[i]))
        f.close()

    if conv_inc_headers != 0:
        if conv_inc_arec != 0:
            f = open(output_filename, "a")
        else:
            f = open(output_filename, "w")

        f.write("{}" "," "{}" "," "{}" "," "{}" "," "{}" "," "{}" "," "{}\n".format("UPC", "Qty. Shipped", "Cost", "Suggested Retail", "Description", "Case Pack", "Item Number"))
        f.close()


    if conv_inc_arec != 0 or conv_inc_headers != 0:
        f = open(output_filename, "a")
    else:
        f = open(output_filename, "w")


    for i in xrange(len(column1)):
        f.write("{}" "," "{}" "," "{}" "," "{}" "," "{}" "," "{}" "," "{}\n".format(column1[i], column7[i], column4[i], column6[i], column2[i], column5[i], column3[i]))
    f.close()

    if conv_inc_crec != 0:
        f = open(output_filename, "a")

        work_file = open(edi_process)
        work_file_count = open(edi_process)
        cut_off = sum(1 for line in work_file_count)
        work_file = [n for n in work_file.readlines() if not n.startswith('A') if not n.startswith('B')]
        for line_num, line in enumerate(work_file):
            if line_num < cut_off:
                #print line[1:14] + " " + line[33:35] + "." + line[35:-2]
                column_append.append(line[:1] + " " + line[1:14] + " " + line[-5:-3] + "." + line[-3:-1])
        #print (column_append)
        f.seek(0, 0)
        for i in xrange(len(column_append)):
            f.write("{}".format(column_append[i]))
        f.close()
