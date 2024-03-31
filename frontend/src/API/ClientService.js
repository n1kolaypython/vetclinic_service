import axios from 'axios'

export default class ClientService {

    static async getAll(limit, offset) {
        const response = await axios.get('http://backend:8000/client', {
            params: {
                _limit: limit,
                _offset: offset
            }
        })
        return response.data
    }     

}