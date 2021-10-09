import { useContext, useState, createContext } from 'react'

const transactionsCTX = createContext({})

export const TransactionsProvider = ({children}) => {
    const [transactions, setTransactions] = useState(undefined);

    return (
        <transactionsCTX.Provider value={{transactions, setTransactions}}>
            {children}
        </transactionsCTX.Provider>
    );
}

export const useTransactions = () => useContext(transactionsCTX)