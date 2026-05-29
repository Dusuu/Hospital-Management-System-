import datetime

#Imported date and time , for appointment purposes.
#Creating blank dictionaries for patients, doctors, appointments

patients = {}
doctors = {}
appointments = {}

#Creating a user defined function to store data of a patient/registering patient.

def register_patient():
    patient_id = input("Enter patient ID: ")
    name = input("Enter patient name: ")
    age = int(input("Enter patient age: "))
    gender = input("Enter patient gender: ")
    current_illness = input("Enter the Current illness of patient: ")
    t=datetime.datetime.now()
    a=t.strftime("%d/%m/%Y")
    q=t.strftime("%H:%M %p")
    if patient_id in patients:
        print("Patient is already registered.")
    else:
        
        patients[patient_id] = {"patient_id": patient_id, "name": name, "age": age, "gender": gender, "current illness":current_illness,
                                "Date of registration":a,"Time of registration":q}
        print("Patient is registered successfully.")
        
#Using this statement we created a dictionary where in the key there is patient_id and 
#the values are again in form of key-value pair as a subset of Patienet_Id
        
#User defined fuction for registration of a Doctor
        
def register_doctor():
    doctor_id = input("Enter doctor ID: ")
    name = input("Enter doctor name: ")
    age=int(input("Enter doctor age: "))
    gender=input("Enter doctor gender: ")
    speciality = input("Enter doctor speciality: ")
    if doctor_id in doctors:
        print("Doctor is already registered.")
    else:
        doctors[doctor_id] = {"doctor_id": doctor_id,"name": name,"gender" : gender,"age" : age,"speciality": speciality}
        print("Doctor registered successfully.")

#User defined fucntion for appointment schedule

    
def schedule_appointment():
    appointment_id = input("Enter appointment ID: ")
    patient_id = input("Enter patient ID: ")
    doctor_id = input("Enter doctor ID: ")
    Date=input("Enter date for appointment: ")
    Time=input("Enter time of appointment: ")
    
    if appointment_id in appointments:
        print("Appointment ID already exists.")
    elif patient_id not in patients:
        print("Patient ID does not exist.")
    elif doctor_id not in doctors:
        print("Doctor ID does not exist.")
    else:
        appointments[appointment_id] = {
            "appointment_id": appointment_id,
            "patient": patients[patient_id],
            "doctor":doctors[doctor_id],
            "Date of Appointment":Date,
            "Time of Appointment":Time}
        print("Appointment scheduled successfully.")


#Function to see the names of patient already registered
        
def view_patient():
    patient_id = input("Enter patient ID to view: ")
    if patient_id in patients:
        patient = patients[patient_id]
        print(f'''
------------------------------------------------------------------
1) Patient ID: {patient['patient_id']}
2) Name: {patient['name']}
3) Age: {patient['age']}
4) Gender: {patient['gender']}
5) Date of registration: {patient['Date of registration']}
6) Time of registration:{patient['Time of registration']}
------------------------------------------------------------------''')
    else:
        print("Patient ID does not exist.")

#Function to see the scheduled appointments

def view_appointments():
    appointment_id = input("Enter Appoitnment ID to view: ")
    if appointment_id in appointments :
        appointment=appointments[appointment_id]
        print(f'''
---------------------------------------------------------------
1)Appointment ID: {appointment['appointment_id']}                  
2)Patient: {appointment['patient']['name']}                     
3)Doctor: {appointment['doctor']['name']}                         
4)Date of Appointment:{appointment['Date of Appointment']}    
5)Time of Appointment:{appointment['Time of Appointment']}       
----------------------------------------------------------------''')
    else:
       print("No Appointment is scheduled")



#Function to see list of already registered doctors

def view_doctor():
    doctor_id = input("Enter Doctor ID to view: ")
    if doctor_id in doctors:
        doctor = doctors[doctor_id]
        print(f'''
---------------------------------------------------
1)Doctor ID: {doctor['doctor_id']}
2) Name: {doctor['name']}
3) Age: {doctor['age']}
4) Gender: {doctor['gender']}
5) speciality: {doctor["speciality"]}
---------------------------------------------------''')
    else:
        print("Doctor ID does not exist.")




#User defined function for creation of main menu
        
def main():
    while True:
        print(''' 
                   ---"WELCOME TO MY HOSPITAL"---
                   ʘʘʘʘʘʘʘʘʘʘʘʘʘʘʘʘʘʘʘʘʘʘʘʘʘʘʘʘʘʘ
                   

                    What are you looking for ??
                    ----------------------------''')

        print("1. New Patient Registration")
        print("2. New Doctor Registration")
        print("3. Schedule Appointment")
        print("4. View Registered Patient")
        print("5. View Registered Doctors")
        print("6. View Scheduled Appointments")
        print("7. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            register_patient()
        elif choice == '2':
            register_doctor()
        elif choice == '3':
            schedule_appointment()
        elif choice == '4':
            view_patient()
        elif choice == '5':
            view_doctor()
        elif choice == '6':
            view_appointments()
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please try again.")

main()
