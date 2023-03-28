import os.path
import re
import csv

def main():
    from_list = []
    subject_list = []
    x_dspam_list = []

    while True:
        file_name = input("Input file name: ")
        try:
            in_file = open('files/'+file_name.strip(),'r')
        except FileNotFoundError:
            print('File does not exist!')
        except Exception:
            print('Other Error Type')
        else:
            break

    out_file_name = input("Output file name: ").strip()
    ovw_prompt = 'File exist, overwrite existing file (y/n): '
    while True:
        if os.path.isfile('files/'+out_file_name):
            ovw = input(ovw_prompt).strip()
            print(ovw)
            if ord(ovw) == 89 or ord(ovw) == 121: #if y/Y is selected
                break
            elif ord(ovw) == 78 or ord(ovw) == 110: #if n/N is selected
                out_file_name = 'files/' + input("New output file name: ").strip()
                ovw_prompt = 'File exist, overwrite existing file (y/n): '
                continue
            else:
                ovw_prompt = 'Enter (y/n): '
                continue
        else:
            break

    lines = in_file.readlines()
    in_file.close()

    for line in lines:
        if len(re.findall('^From: (\S+@\S+)', line)) > 0:
            from_list.append(re.findall('^From: (\S+@\S+)', line)[0])
        elif len(re.findall('Subject: ', line)) > 0:
            r_start = line.find('r39')
            subject_list.append(line[r_start:r_start + 6])
        elif len(re.findall('^X-DSPAM-Confidence:', line)) > 0:
            x_dspam_list.append(re.findall('\d+.+\d', line)[0])


    with open(out_file_name, 'w', newline='') as out_file:
        cell = csv.writer(out_file)
        cell.writerow(['Email', 'Subject', 'Confidence'])
        for i in range(len(from_list)):
            cell.writerow([from_list[i], subject_list[i], x_dspam_list[i]])
    out_file.close()
    print('Data Stored!')

if (__name__ == '__main__'):
    main()