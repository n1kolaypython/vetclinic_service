import react from 'react'

const ClientItem = ({full_name, phone_number, email}) => {
    return (
        <li className='list-group-item d-flex flex-column px-2 my-2'>
            <span className='fs-5'> {full_name} </span>
            <span className='fs-6 mt-2'> <b>Phone number:</b> {phone_number} </span>
            <span className='fs-6'> <b>Email:</b> {email} </span>
        </li>
    )
}

export default ClientItem;