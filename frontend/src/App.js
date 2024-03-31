import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import Sidebar from './components/UI/Sidebar';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import Clients from './components/ClientList';
import Appointments from './components/AppointmentList'
import Pets from './components/PetList'

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <div className='d-flex vh-100 w-100'>
          <div className='col-auto vh-100'>
            <Sidebar />
          </div>
          <div>
            <Routes>
              <Route path="/" element={<Home />}></Route>
              <Route path="/appointments" element={<Appointments />}></Route>
              <Route path="/clients" element={<Clients />}></Route>
              <Route path="/pets" element={<Pets />}></Route>
            </Routes>
          </div>
        </div>
      </BrowserRouter>
    </div>
  );
}

export default App;

function Home() {
  return (
    <h2>Hello From Home</h2>
  )
}
