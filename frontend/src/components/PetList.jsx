import React, { useEffect, useState } from 'react'
import PetItem from './PetItem';

const Clients = () => {

    const [pets, setPets] = useState([
        { nickname: "Humberto", species: "bird", breed: "Labrador Retriever" },
        { nickname: "Bella", species: "dog", breed: "Golden Retriever" },
        { nickname: "Whiskers", species: "cat", breed: "Siamese" },
        { nickname: "Chirpy", species: "bird", breed: "Parakeet" },
    ]);


    return (
        <div className='container bg-light rounded border w-100 vh ps-2 py-3 m-1 w-100 col'>
            <ul className='list-group'>
                {pets.map(pet =>
                    <PetItem
                        nickname={pet.nickname}
                        species={pet.species}
                        breed={pet.breed}
                    />
                )}
            </ul>
        </div>
    )
}

export default Clients;