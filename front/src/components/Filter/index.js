import './styles.css'
import api from '../../services/api'
import { useTransactions } from '../../providers/transactions'

const Filter = ({perPage, setPerPage, pageNumber, setPageNumber}) => {

    const { setTransactions } = useTransactions()

    const filter = (e) => {
        e.preventDefault()
        
        const perpage = `perpage=${perPage}`;
        const pagenumb = `pagenumber=${pageNumber}`;
        api.get(`/transaction?${perpage}&${pagenumb}`)
        .then( data => setTransactions(data.data))
        .catch( error => console.log('error'));
    }
    return (
        <>
            <form onSubmit={filter} className="filter-container">
                <h3>Filter</h3>
                <label htmlFor="pgNumber">Número da página</label>
                <input
                    type="number"
                    value={pageNumber}
                    onChange={ e => setPageNumber(e.target.value)}
                    id='pgNumber'
                    min={1}/>
                <br />
                <label htmlFor="perPg">Quantidade por página</label>
                <input
                    type="number"
                    value={perPage}
                    onChange={ e => setPerPage(e.target.value)}
                    id='perPg'
                    min={1}/>
                <button type='submit'>Filtrar</button>
            </form>
        </>
    );
}

export default Filter;