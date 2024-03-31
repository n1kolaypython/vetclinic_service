import react from 'react'

const AppointmentItem = ({ start_date, end_date, cabinet }) => {

    return (
        <li className='list-group-item d-flex flex-column px-2 my-2'>
            <span className='fs-5'> {cabinet} </span>
            <span className='fs-6'>{start_date} - {end_date}</span>
        </li>
    )
}

export default AppointmentItem;