def reportFailedLogins(file_path, threshold):
    dictionary = {}
    resultIPs = []

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            fields = line.split()
            print(fields)

            IP = fields[3]
            status = fields[4]

            if status == "FAILED":
                if IP in dictionary:
                    dictionary[IP] = dictionary[IP] + 1
                else:
                    dictionary[IP] = 1

            print(dictionary)

        for IP in dictionary:
            if dictionary[IP] >= threshold:
                resultIPs.append(IP)

    return resultIPs

if __name__ == "__main__":
    print(reportFailedLogins("test.log", 3))
