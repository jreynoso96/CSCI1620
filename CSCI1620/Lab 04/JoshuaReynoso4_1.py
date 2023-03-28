import re
import csv

def main():

    file = open('files/input.txt', 'r')
    x_spam_txt = open('files/output.txt', 'w')

    email = {}
    tot_emails = 0
    x_spam_tot = 0
    x_counter = 0
    lines = file.readlines()

    for line in lines:
        if len(re.findall('^From (\S+@\S+)', line)) > 0:
            y = re.findall('^From (\S+@\S+)', line)
            if y[0] not in email:
                email[y[0]] = 1
            else:
                email[y[0]] += 1
        if len(re.findall('^X-DSPAM-Confidence: \d+.+\d', line)) > 0:
            x = re.findall('(\d+.+\d)', line)
            x_spam_tot += float(x[0])
            x_counter += 1
            x_spam_txt.write(re.findall('^X-DSPAM-Confidence: \d+.+\d\n', line)[0])
    for name in email:
        tot_emails += email[name]

    with open('output.csv', 'w', newline ='') as emails_txt:
        cell = csv.writer(emails_txt)
        cell.writerow(['Email', 'Count'])
        for name in email:
            cell.writerow([name, email[name]])
        cell.writerow(['TOTAL', tot_emails])

    x_spam_tot_txt = 'Total DSPAM Confidence = ' + str(format(x_spam_tot,".2f")) + '\n'
    x_avg_txt = 'Average DSPAM Confdience = ' + str(format(x_spam_tot/x_counter,".2f")) + '\n'
    x_spam_txt.write('-------------------------------------------------\n')
    x_spam_txt.write(x_spam_tot_txt)
    x_spam_txt.write(x_avg_txt)

    file.close()
    x_spam_txt.close()
    emails_txt.close()

if (__name__ == '__main__'):
    main()