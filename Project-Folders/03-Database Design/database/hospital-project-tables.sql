
-- Patient
CREATE TABLE patients (
	patient_id SERIAL PRIMARY KEY,
	patient_name VARCHAR(100),
	patient_gender VARCHAR(10) CHECK (patient_gender IN ('Male', 'Female')),
	patient_birthdate DATE,
	patient_contact_number VARCHAR(100)
);

-- Hospital
CREATE TABLE hospitals(
	hospital_id SERIAL PRIMARY KEY,
	hospital_name VARCHAR(100) NOT NULL,
	hospital_address VARCHAR(100)
);

-- specializations
CREATE TABLE specializations(
    specialization_id SERIAL PRIMARY KEY,
    specialization_name VARCHAR(100) UNIQUE NOT NULL,
    specialization_desc TEXT
);

-- Doctors
CREATE TABLE doctors(
	doctor_id SERIAL PRIMARY KEY,
	hospital_id INT NULL,
	specialization_id INT NULL,
	doctor_name VARCHAR(100),
	CONSTRAINT fk_specializations
		FOREIGN KEY(specialization_id)
		REFERENCES specializations(specialization_id)
		ON UPDATE CASCADE
		ON DELETE SET NULL,
	CONSTRAINT fk_hospitals
		FOREIGN KEY(hospital_id)
		REFERENCES hospitals(hospital_id)
		ON UPDATE CASCADE
		ON DELETE SET NULL
);


-- Doctor Schedule
CREATE TABLE doctor_schedule(
	schedule_id SERIAL PRIMARY KEY,
	doctor_id INT,
	day_of_week VARCHAR(10),
	start_time TIME,
	end_time TIME,
	CONSTRAINT fk_doctors
		FOREIGN KEY(doctor_id)
		REFERENCES doctors(doctor_id)
		ON DELETE CASCADE
		ON UPDATE CASCADE
);

-- Tabel Appointment slot
CREATE TABLE appointment_slots(
	slot_id SERIAL PRIMARY KEY,
	schedule_id INT,
	start_time TIME,
	end_time TIME,
	CONSTRAINT fk_doctor_schedule
		FOREIGN KEY(schedule_id)
		REFERENCES doctor_schedule(schedule_id)
		ON DELETE CASCADE
		ON UPDATE CASCADE
);

-- appointment
CREATE TABLE appointments(
	appointment_id SERIAL PRIMARY KEY,
	patient_id INT,
	slot_id INT NULL,
	appointment_date DATE,
	appointment_status VARCHAR(20) CHECK (appointment_status IN ('Scheduled', 'Completed', 'Cancelled'))
	DEFAULT 'Scheduled',
	CONSTRAINT fk_patient
		FOREIGN KEY(patient_id)
		REFERENCES patients(patient_id)
		ON UPDATE CASCADE 
		ON DELETE CASCADE,
	CONSTRAINT fk_appointment_slot
		FOREIGN KEY(slot_id)
		REFERENCES appointment_slots(slot_id)
		ON UPDATE CASCADE
		ON DELETE SET NULL, 
	CONSTRAINT unique_appointment_slot UNIQUE (slot_id, appointment_date)
);

-- medical records
CREATE TABLE medical_records(
	appointment_id INT PRIMARY KEY,
	diagnosis TEXT,
	treatment TEXT,
	CONSTRAINT fk_appointments
		FOREIGN KEY(appointment_id)
		REFERENCES appointments(appointment_id)
		ON UPDATE CASCADE 
		ON DELETE CASCADE
);