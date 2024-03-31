import React, { useEffect, useState } from 'react'
import ClientItem from './ClientItem';

const Clients = () => {

    const [clients, setClients] = useState([
        {full_name: "Henry Osborn", phone_number: "123-526-4252", email:"henry.gehton@mail.ru"},
        {full_name: "Emma Frost", phone_number: "456-789-0123", email:"emma.frost@mail.ru"},
        {full_name: "John Doe", phone_number: "789-012-3456", email:"john.doe@mail.ru"},
        {full_name: "Jane Smith", phone_number: "345-678-9012", email:"jane.smith@mail.ru"},
    ]);


    return (
        <div className='container bg-light rounded border w-100 vh ps-2 py-3 m-1 w-100 col'>
            <ul className='list-group'>
                {clients.map(client =>
                    <ClientItem
                        full_name={client.full_name}
                        phone_number={client.phone_number}
                        email={client.email}
                    />
                )}
            </ul>
        </div>
    )
}

export default Clients;