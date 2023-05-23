import csv
import requests
from sys import argv

if __name__ == "__main__":
    idEmp = argv[1]
    idURL = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(idEmp)
    nameURL = 'https://jsonplaceholder.typicode.com/users/{}'.format(idEmp)

    sessionReq = requests.Session()

    employee = sessionReq.get(idURL)
    employeeName = sessionReq.get(nameURL)

    json_req = employee.json()
    name = employeeName.json()['username']

    csv_filename = '{}.csv'.format(idEmp)

    with open(csv_filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for task in json_req:
            task_id = task['id']
            task_title = task['title']
            task_completed = task['completed']

            csv_writer.writerow([idEmp, name, task_completed, task_title])

    print("Data exported to '{}' successfully.".format(csv_filename))
