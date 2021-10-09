import './styles.css'
import Header from '../Header'
import Filter from '../Filter'
import Transactions from '../Transactions'
import api from '../../services/api'
import { useEffect, useState } from 'react'


const Registers = () => {

    const [perPage, setPerPage] = useState(15);
    const [pageNumber, setPageNumber] = useState(1);

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