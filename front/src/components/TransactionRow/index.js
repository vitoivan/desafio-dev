const TransactionRow = ({item}) => {
    return (
        <tr>
            <td>{item.type}</td>
            <td>{item.value}</td>
            <td>{item.date}</td>
            <td>{item.time}</td>
            <td>{item.owner}</td>
            <td>{item.shop}</td>
            <td>{item.cpf}</td>
            <td>{item.card}</td>
        </tr>
    )
}   
export default TransactionRow