import './styles.css'
import api from '../../services/api'
import { useEffect, useState } from 'react'

const Home = () => {

    const [file, setFile] = useState(undefined)

    useEffect(() => {
        console.log(file)
    }, [file])

    const handleSubmit = (e) => {
        e.preventDefault()
        const formData = new FormData();
        formData.append('file', file)
        const config = {
            headers: {"Content-Type": `multipart/form-data`}
        }

        api.post('/transaction', formData, config)
        .then(data => console.log('data: ', data))
        .catch(erro => console.log(erro))
    }
  

    return (
        <>
        <form onSubmit={handleSubmit}>
            <input type="file" onChange={e => setFile(e.target.files[0])} name="upload_file" />
            <button type="submit">Enviar arquivo</button>
        </form>
        </>
    );
}

export default Home