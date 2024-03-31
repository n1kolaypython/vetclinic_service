import react from 'react'

const PetItem = ({nickname, species, breed}) => {
    return (
        <li className='list-group-item d-flex flex-column px-2 my-2'>
            <span className='fs-5'> {nickname} </span>
            <span className='fs-6 mt-2'> <b>Species:</b> {species} </span>
            <span className='fs-6'> <b>Breed:</b> {breed} </span>
        </li>
    )
}

export default PetItem;