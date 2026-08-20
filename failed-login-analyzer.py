def reportFailedLogins(file_path, threshold):
    dictionary = {}
    resultIPs = []
    resultIPsString = ""
    userThreshold = threshold
    print(f"Threshold: {userThreshold}")

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            fields = line.split()

            IP = fields[3]
            status = fields[4]

            if status == "FAILED":
                if IP in dictionary:
                    dictionary[IP] = dictionary[IP] + 1
                else:
                    dictionary[IP] = 1


        for IP in dictionary:
            if dictionary[IP] >= threshold:
                resultIPs.append(IP)
                resultIPsString ="Suspicious IPs\n" "----------------\n"

        sortedResultIPs = sorted(resultIPs, key=lambda IP: dictionary[IP], reverse=True)

        for IP in sortedResultIPs:
             resultIPsString += f"{IP} - {dictionary[IP]} failed attempts\n"
    return resultIPsString

if __name__ == "__main__":
    print(reportFailedLogins("test.log", 2))
