
import React, { useState } from 'react'
import AppointmentItem from './AppointmentItem';

const Appointments = () => {


    const [appointments, setAppointments] = useState([
        { start_date: new Date("2023-03-14T10:00:00").toISOString(), end_date: new Date("2023-03-14T11:00:00").toISOString(), cabinet: "A-101" },
        { start_date: new Date("2023-03-14T14:00:00").toISOString(), end_date: new Date("2023-03-14T15:00:00").toISOString(), cabinet: "B-425" },
        { start_date: new Date("2023-03-15T09:00:00").toISOString(), end_date: new Date("2023-03-15T10:00:00").toISOString(), cabinet: "C-645" },
        { start_date: new Date("2023-03-15T12:00:00").toISOString(), end_date: new Date("2023-03-15T13:00:00").toISOString(), cabinet: "A-262" },
        { start_date: new Date("2023-03-14T10:00:00").toISOString(), end_date: new Date("2023-03-14T11:00:00").toISOString(), cabinet: "A-101" },
        { start_date: new Date("2023-03-14T14:00:00").toISOString(), end_date: new Date("2023-03-14T15:00:00").toISOString(), cabinet: "B-425" },
        { start_date: new Date("2023-03-15T09:00:00").toISOString(), end_date: new Date("2023-03-15T10:00:00").toISOString(), cabinet: "C-645" },
    ]);


    return (
        <div className='container bg-light rounded border w-100 vh ps-2 py-3 m-1 w-100 col'>
            <ul className='list-group'>
                {appointments.map(appointment =>
                    <AppointmentItem
                        start_date={appointment.start_date}
                        end_date={appointment.end_date}
                        cabinet={appointment.cabinet}
                    />
                )}
            </ul>
        </div>
    )
}

export default Appointments;