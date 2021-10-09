import { useTransactions } from "../../providers/transactions"
import TransactionRow from '../TransactionRow'
import './styles.css'

const Transaction = () => {

    const { transactions } = useTransactions();

    const parseReal = (value) => {
        const configs = {
            style: 'currency', 
            currency: 'BRL'
        };
        const number = parseFloat(value)
        return number.toLocaleString('pt-br', configs)
    }

    const get_number_with_signal = (obj) => {
        const negative_types = ['Boleto', 'Financiamento', 'Aluguel'];

        if (negative_types.includes(obj.type)) {
            return obj.value * -1;
        }
        return obj.value;
    }
    return (
       <>
        <p className='sum'>
            <span>Saldo em conta: <br /></span>
            {
                parseReal(
                    transactions?.reduce((acc, curr) => (
                        acc + get_number_with_signal(curr)
                    ), 0)
                )
            }
        </p>
         <table className='transaction-container'>
            <thead>
                <tr>
                    <th>Tipo</th>
                    <th>Valor</th>
                    <th>Data</th>
                    <th>Hora</th>
                    <th>Dono</th>
                    <th>Loja</th>
                    <th>CPF</th>
                    <th>Cartão</th>
                </tr>
            </thead>
            <tbody>
                {
                    transactions?.map( (item, index) => {
                        const real = parseReal(item.value)
                        return (<TransactionRow key={index} item={{...item, value: real}}/>)
                    })
                }
            </tbody>
            
        </table>
       </>
    )
}

export default Transaction