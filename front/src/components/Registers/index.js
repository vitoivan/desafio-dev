import './styles.css'
import Header from '../Header'
import Filter from '../Filter'
import Transactions from '../Transactions'
import { useState } from 'react'
import { useUser } from '../../providers/user'
import { Redirect } from 'react-router'


const Registers = () => {

    const [perPage, setPerPage] = useState(15);
    const [pageNumber, setPageNumber] = useState(1);
    const { user, setUser } = useUser(1);

    const usr = localStorage.getItem('@bycoders-desafio-dev')
    if(usr && !user)
    {
        setUser(JSON.parse(usr))
    }
    if(!user?.profileObj){
        return <Redirect to='/login' />
    }

    return (
        <div className="registers-container">
            <Header />
            <Filter
                perPage={perPage}
                setPageNumber={setPageNumber}
                setPerPage={setPerPage}
                pageNumber={pageNumber}/>
            <Transactions />
            
        </div>
    );
}

export default Registers