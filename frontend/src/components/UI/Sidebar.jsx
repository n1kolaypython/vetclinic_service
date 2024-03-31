import React from 'react'
import 'bootstrap-icons/font/bootstrap-icons.css'
import {Link} from 'react-router-dom'


function Sidebar() {
    return (
        <div className='sidebar d-flex flex-column justify-content-between bg-dark text-white p-4 vh-100 position-sticky'>
            <div>
                <a className='d-flex align-items-center nav-link link-light link-offset-2 link-underline-opacity-25 link-underline-opacity-100-hover'>
                    <i className='bi bi-hospital fs-5 me-2'></i>
                    <span className='fs-4'>VetClinic</span>
                </a>
                <hr className='text-secondary mt-2' />
                <ul className='nav nav-pills flex-column p-0 m-0'>
                    <li className='nav-item p-1'>
                        <Link to='/appointments' className='nav-link link-light link-offset-2 link-underline-opacity-25 link-underline-opacity-100-hover'>
                            <i className='bi bi-file-ruled me-2 fs-5'></i>
                            <span className='fs-5'>Appointments</span>
                        </Link>
                    </li>
                    <li className='nav-item p-1'>
                        <Link to='/clients' className='nav-link link-light link-offset-2 link-underline-opacity-25 link-underline-opacity-100-hover'>
                            <i className='bi bi-people me-2 fs-5'></i>
                            <span className='fs-5'>Clients</span>
                        </Link>
                    </li>
                    <li className='nav-item p-1'>
                        <Link to='/pets' className='nav-link link-light link-offset-2 link-underline-opacity-25 link-underline-opacity-100-hover'>
                            <i className='bi bi-backpack me-2 fs-5'></i>
                            <span className='fs-5'>Pets</span>
                        </Link>
                    </li>

                </ul>
            </div>
            <div>
                <hr className='text-secondary' />
                <i className='bi bi-person me-2 fs-5'></i>
                <span className='fs-5'>Some Client</span>
            </div>
        </div>


    )
}

export default Sidebar;