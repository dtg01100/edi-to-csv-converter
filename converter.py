import upc_check_digit


def edi_convert(edi_process, output_filename, calc_upc, inc_arec, inc_crec, inc_headers, filter_ampersand):

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
    work_file_lined = [n for n in work_file.readlines()]


    if conv_inc_headers != 0:
        f = open(output_filename, "w")

        f.write("{}" "," "{}" "," "{}" "," "{}" "," "{}" "," "{}" "," "{}\n".format("UPC", "Qty. Shipped", "Cost",
                "Suggested Retail", "Description", "Case Pack", "Item Number"))
        f.close()

    f = open(output_filename, "a")
    for line_num, line in enumerate(work_file_lined):
        if n.startswith('A'):
            f.write("{}".format(line[:]))
        if n.startswith('B'):
            if line_num < cut_off:
                # print line[1:12]
                if conv_calc_upc != 1 and filter_ampersand != 1:
                    f.write("{}\t" "," "{}\t" "," "{}\t" "," "{}\t" "," "{}" "," "{}\t" "," "{}\t" ",\n".format(line[1:12],
        line[60:62], line[45:47] + "." + line[47:49], line[63:65] + "." + line[65:67], line[12:37], line[55:57], line[38:43]))
                elif conv_calc_upc != 0 and filter_ampersand != 1:
                    f.write("{}\t" "," "{}\t" "," "{}\t" "," "{}\t" "," "{}" "," "{}\t" "," "{}\t" ",\n".format(upc_check_digit.add_check_digit(line[1:12]),
        line[60:62], line[45:47] + "." + line[47:49], line[63:65] + "." + line[65:67], line[12:37], line[55:57], line[38:43]))
                elif conv_calc_upc !=0 and filter_ampersand != 0:
                    f.write("{}\t" "," "{}\t" "," "{}\t" "," "{}\t" "," "{}" "," "{}\t" "," "{}\t" ",\n".format(upc_check_digit.add_check_digit(line[1:12]),
        line[60:62], line[45:47] + "." + line[47:49], line[63:65] + "." + line[65:67], line.replace("&", "AND")[12:37], line[55:57], line[38:43]))
                elif conv_calc_upc !=1 and filter_ampersand !=0:
                    f.write("{}\t" "," "{}\t" "," "{}\t" "," "{}\t" "," "{}" "," "{}\t" "," "{}\t" ",\n".format(line[1:12],
        line[60:62], line[45:47] + "." + line[47:49], line[63:65] + "." + line[65:67], line.replace("&", "AND")[12:37], line[55:57], line[38:43]))
        if n.startswith('C'):
            f.write("{}".format(line[:]))
    f.close()
