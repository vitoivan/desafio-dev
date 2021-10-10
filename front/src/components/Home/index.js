import './styles.css'
import api from '../../services/api'
import { useState } from 'react'
import { Redirect } from 'react-router'
import { useUser } from '../../providers/user'
import Header from '../Header'
import toast from 'react-hot-toast'
import Loading from '../Loading'
import { useTransactions } from '../../providers/transactions'
import Transactions from '../Transactions'

const Home = () => {

    const [file, setFile] = useState(undefined)
    const { user, loading, setLoading, setUser } = useUser();
    const { setTransactions, transactions } = useTransactions();

    const handleSubmit = (e) => {
        e.preventDefault()
        setLoading(true)
        const formData = new FormData();
        formData.append('file', file)

        const config = {
            headers: {"Content-Type": `multipart/form-data`}
        }

        api.post('/register', formData, config)
        .then(data => {
            setLoading(false)
            setTransactions(data.data)
        })
        .catch(error => 
            {
                setLoading(false)
                return toast('Verifique o tipo de arquivo enviado',
                {
                    icon: '❌',
                    style: {
                    borderRadius: '10px',
                    background: '#333',
                    color: '#fff',
                    fontSize: '.8rem'
                    },
                })
            }
        )
    }

    const usr = localStorage.getItem('@bycoders-desafio-dev')
    if(usr && !user)
    {
        setUser(JSON.parse(usr))
    }
    if(!user?.profileObj){
        return <Redirect to='/login' />
    }

    return (
        <>
        <Header />
        <div className="home-container center">
            <form onSubmit={handleSubmit} className='center'>
                <label htmlFor="file" className='upload-area center'>
                    Selecionar arquivo
                </label>
                {
                    file && (<p className='file'>Arquivo: <span>{file.name}</span></p>)
                }
                <input id='file' type="file" onChange={e => setFile(e.target.files[0])} name="upload_file" />
                { loading === true ? (<Loading />) : (<button type="submit">Enviar</button>)}
            </form>
            { transactions && (<Transactions />) }
        </div>
        </>
    );
}

export default Home